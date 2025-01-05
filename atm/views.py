from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound, AuthenticationFailed, ValidationError
from django.contrib.auth.hashers import check_password, make_password
from decimal import Decimal
from .models import Account


# 登录视图
class LoginView(APIView):
    authentication_classes = []  # 禁用全局的身份验证
    permission_classes = []  # 禁用全局的权限设置

    def post(self, request, *args, **kwargs):
        # 解析请求数据
        data = request.data
        card_id = data.get('cardId')
        password = data.get('password')

        if not card_id or not password:
            raise ValidationError({"message": "Card ID and password are required"})

        try:
            user = Account.objects.get(card_id=card_id)
        except Account.DoesNotExist:
            raise AuthenticationFailed({"message": "Invalid card"})

        if check_password(password, user.password):
            # 保存到 session
            request.session['card_id'] = user.card_id
            response = Response({"message": "Login successful", "balance": user.balance}, status=status.HTTP_200_OK)
            response['Access-Control-Expose-Headers'] = "Authentication"
            response['Authentication'] = str(user.card_id)
            return response
        else:
            raise AuthenticationFailed({"message": "Invalid password"})


# 提现视图
class WithdrawView(APIView):
    def post(self, request, *args, **kwargs):
        # 获取自定义头部信息 'Authentication'
        card_id = request.headers.get('Authentication')

        if not card_id:
            raise AuthenticationFailed({"error": "User not logged in"})

        try:
            current_user = Account.objects.get(card_id=card_id)
        except Account.DoesNotExist:
            raise NotFound({"error": "User not found"})

        # 解析提现金额
        try:
            withdrawmoney = request.data.get('withdrawmoney')
            withdrawmoney = Decimal(withdrawmoney)
        except (TypeError, ValueError):
            raise ValidationError({"error": "Invalid withdraw amount"})

        if withdrawmoney > current_user.balance:
            return Response({"message": "Withdraw failure", "new_balance": current_user.balance},
                            status=status.HTTP_200_OK)

        # 更新余额
        try:
            current_user.balance -= withdrawmoney
            current_user.save()
            return Response({"message": "Withdraw successful", "new_balance": current_user.balance},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "Failed to update balance"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# 查询余额视图
class BalanceView(APIView):
    def get(self, request, *args, **kwargs):
        # 获取自定义头部信息 'Authentication'
        card_id = request.headers.get('Authentication')

        if not card_id:
            raise AuthenticationFailed({"error": "User not logged in"})

        try:
            current_user = Account.objects.get(card_id=card_id)
        except Account.DoesNotExist:
            raise NotFound({"error": "User not found"})

        return Response({"balance": current_user.balance}, status=status.HTTP_200_OK)


# 转账视图
class TransferView(APIView):
    def post(self, request, *args, **kwargs):
        # 获取自定义头部信息 'Authentication'
        card_id = request.headers.get('Authentication')

        if not card_id:
            raise AuthenticationFailed({"error": "User not logged in"})

        try:
            current_user = Account.objects.get(card_id=card_id)
        except Account.DoesNotExist:
            raise NotFound({"error": "User not found"})

        # 解析转账数据
        data = request.data
        target_account_id = data.get('account')
        transfer_amount = data.get('amount')

        if not target_account_id or not transfer_amount:
            raise ValidationError({"error": "Target account and amount are required"})

        try:
            transfer_amount = Decimal(transfer_amount)
        except (TypeError, ValueError):
            raise ValidationError({"error": "Invalid transfer amount"})

        if transfer_amount > current_user.balance:
            return Response({"message": "Transfer failure", "balance": current_user.balance},
                            status=status.HTTP_200_OK)

        try:
            target_account = Account.objects.get(card_id=target_account_id)
        except Account.DoesNotExist:
            raise NotFound({"error": "Target account not found"})

        # 更新余额
        try:
            current_user.balance -= transfer_amount
            target_account.balance += transfer_amount
            current_user.save()
            target_account.save()
            return Response({"message": "Transfer successful", "new_balance": current_user.balance},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "Failed to update balance"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# 存款视图
class DepositView(APIView):
    def post(self, request, *args, **kwargs):
        # 获取自定义头部信息 'Authentication'
        card_id = request.headers.get('Authentication')

        if not card_id:
            raise AuthenticationFailed({"error": "User not logged in"})

        try:
            current_user = Account.objects.get(card_id=card_id)
        except Account.DoesNotExist:
            raise NotFound({"error": "User not found"})

        # 解析存款金额
        try:
            deposit_amount = request.data.get('amount')
            deposit_amount = Decimal(deposit_amount)
        except (TypeError, ValueError):
            raise ValidationError({"error": "Invalid deposit amount"})

        # 更新余额
        try:
            current_user.balance += deposit_amount
            current_user.save()
            return Response({"message": "Deposit successful", "new_balance": current_user.balance},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "Failed to update balance"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# 修改密码视图
class ChangePasswordView(APIView):
    def post(self, request, *args, **kwargs):
        # 获取自定义头部信息 'Authentication'
        card_id = request.headers.get('Authentication')

        if not card_id:
            raise AuthenticationFailed({"error": "User not logged in"})

        try:
            current_user = Account.objects.get(card_id=card_id)
        except Account.DoesNotExist:
            raise NotFound({"error": "User not found"})

        # 解析新密码
        new_password = request.data.get('newpassword')

        if not new_password:
            raise ValidationError({"error": "New password is required"})

        # 更新密码
        try:
            current_user.password = make_password(new_password)
            current_user.save()
            return Response({"message": "Password changed successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "Failed to update password"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        