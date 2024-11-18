from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound, AuthenticationFailed, ValidationError
from django.contrib.sessions.models import Session
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

        if user.password == password:
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
            print(current_user.balance)
            return Response({"message": "Withdraw successful", "new_balance": current_user.balance},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "Failed to update balance"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
