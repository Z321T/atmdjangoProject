from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import login

from .models import Account


class LoginView(APIView):
    @csrf_exempt
    def post(self, request):
        card_id = request.data.get('cardId')
        password = request.data.get('password')
        print(card_id, password)

        # 尝试通过 card_id 查找用户
        try:
            user = Account.objects.get(card_id=card_id)
            print('!!!')
            print(user)
        except Account.DoesNotExist:
            # 如果没有找到用户，返回错误响应
            return Response({"message": "Invalid card"}, status=status.HTTP_401_UNAUTHORIZED)

        # 检查密码是否匹配
        if user.password == password:
            # 密码匹配，登录成功
            login(request, user)
            print("登录成功！")
            return Response({"message": "Login successful", "balance": user.balance}, status=status.HTTP_200_OK)
        else:
            # 密码不匹配，返回错误响应
            print("密码不匹配")
            return Response({"message": "Invalid password"}, status=status.HTTP_200_OK)


class Withdraw(APIView):
    def post(self, request):
        # 获取当前登录用户
        current_user = request.user

        # 验证用户是否登录
        if not current_user.is_authenticated:
            print("用户未登陆")
            return Response({"error": "User not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)

        # 获取请求中的提现金额
        try:
            withdrawmoney = request.data.get('withdrawmoney')
            # 确保提现金额是有效的数字
            withdrawmoney = float(withdrawmoney)
        except (TypeError, ValueError):
            return Response({"error": "Invalid withdraw amount"}, status=status.HTTP_400_BAD_REQUEST)

        # 检查用户是否有足够的余额
        if withdrawmoney > current_user.balance:
            return Response({"error": "Insufficient balance"}, status=status.HTTP_400_BAD_REQUEST)

        # 更新用户的 balance
        try:
            current_user.balance -= withdrawmoney
            current_user.save()
        except Exception as e:
            return Response({"error": "Failed to update balance"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # 返回成功响应
        print(current_user.balance)
        return Response({"message": "Withdraw successful", "new_balance": current_user.balance}, status=status.HTTP_200_OK)

