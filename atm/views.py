from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Account


@csrf_exempt
def login(request):
    # 解析 JSON 请求体
    import json
    data = json.loads(request.body)

    if request.method == "POST":
        # 获取请求数据
        card_id = data.get('cardId')
        password = data.get('password')
        print(card_id, password)

        # 尝试通过 card_id 查找用户
        try:
            user = Account.objects.get(card_id=card_id)
            print('!!!')
            print(user)
        except Account.DoesNotExist:
            # 如果没有找到用户，返回错误响应
            return JsonResponse({"message": "Invalid card"}, status=status.HTTP_401_UNAUTHORIZED)

        # 检查密码是否匹配
        if user.password == password:
            # 密码匹配，登录成功
            request.session['card_id'] = user.card_id
            print("登录成功！")
            return JsonResponse({"message": "Login successful", "balance": user.balance}, status=status.HTTP_200_OK)
        else:
            # 密码不匹配，返回错误响应
            print("密码不匹配")
            return JsonResponse({"message": "Invalid password"}, status=status.HTTP_200_OK)

    # 如果请求方法不是 POST，返回错误响应
    return JsonResponse({"message": "Invalid request method"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@csrf_exempt
def withdraw(request):
    # 获取当前登录用户
    current_user = request.session.get('card_id')

    # 获取请求中的提现金额
    try:
        withdrawmoney = request.POST.get('withdrawmoney')
        # 确保提现金额是有效的数字
        withdrawmoney = float(withdrawmoney)
    except (TypeError, ValueError):
        return JsonResponse({"error": "Invalid withdraw amount"}, status=status.HTTP_400_BAD_REQUEST)

    # 检查用户是否有足够的余额
    if withdrawmoney > current_user.balance:
        return JsonResponse({"error": "Insufficient balance"}, status=status.HTTP_400_BAD_REQUEST)

    # 更新用户的 balance
    try:
        current_user.balance -= withdrawmoney
        current_user.save()
    except Exception as e:
        return JsonResponse({"error": "Failed to update balance"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # 返回成功响应
    print(current_user.balance)
    return JsonResponse({"message": "Withdraw successful", "new_balance": current_user.balance}, status=status.HTTP_200_OK)
