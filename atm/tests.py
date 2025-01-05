from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Account
from decimal import Decimal
from django.test import override_settings
from django.contrib.auth.hashers import make_password

class ATMViewsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = Account.objects.create(card_id="123456", password=make_password("password"), balance=Decimal('1000.00'))
        self.target_user = Account.objects.create(card_id="654321", password=make_password("password"), balance=Decimal('500.00'))

    @override_settings(CSRF_COOKIE_SECURE=False, CSRF_COOKIE_HTTPONLY=False)
    # 测试使用正确的凭据成功登录
    def test_login_success(self):
        response = self.client.post('/api/login/', {'cardId': self.user.card_id, 'password': 'password'}, format='json')
        # 检查状态码和返回数据
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Login successful")
        self.assertEqual(str(response.data['balance']), str(self.user.balance))  # 将 Decimal 转换为字符串比较

        # 检查认证头是否正确返回
        self.assertIn('Authentication', response.headers)
        self.assertEqual(response.headers['Authentication'], str(self.user.card_id))

        # 检查 Session 是否正确设置
        self.assertEqual(str(self.client.session['card_id']), str(self.user.card_id))  # 确保比较的值类型一致

    # 测试使用错误的卡号登录
    def test_login_invalid_card(self):
        response = self.client.post('/api/login/', {'cardId': '000000', 'password': 'password'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # 修改为 403

    # 测试使用错误的密码登录
    def test_login_invalid_password(self):
        response = self.client.post('/api/login/', {'cardId': '123456', 'password': 'wrongpassword'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # 修改为 403

    # 测试在资金充足的情况下成功取款
    def test_withdraw_success(self):
        self.client.credentials(HTTP_AUTHENTICATION='123456')
        response = self.client.post('/api/withdraw/', {'withdrawmoney': '100.00'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Withdraw successful")

    # 测试在资金不足的情况下取款失败
    def test_withdraw_insufficient_funds(self):
        self.client.credentials(HTTP_AUTHENTICATION='123456')
        response = self.client.post('/api/withdraw/', {'withdrawmoney': '2000.00'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Withdraw failure")

    # 测试查询余额
    def test_balance_view(self):
        self.client.credentials(HTTP_AUTHENTICATION='123456')
        response = self.client.get('/api/balance/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(str(response.data['balance']), str(self.user.balance))  # 转换为字符串比较

    # 测试成功转账
    def test_transfer_success(self):
        self.client.credentials(HTTP_AUTHENTICATION='123456')
        response = self.client.post('/api/transfer/', {'account': '654321', 'amount': '100.00'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Transfer successful")

    # 测试转账时目标账户不存在
    def test_transfer_invalid_target(self):
        self.client.credentials(HTTP_AUTHENTICATION='123456')
        response = self.client.post('/api/transfer/', {'account': '000000', 'amount': '100.00'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # 测试转账时资金不足
    def test_transfer_insufficient_funds(self):
        self.client.credentials(HTTP_AUTHENTICATION='123456')
        response = self.client.post('/api/transfer/', {'account': '654321', 'amount': '2000.00'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Transfer failure")

    # 测试存款成功
    def test_deposit_success(self):
        self.client.credentials(HTTP_AUTHENTICATION='123456')
        response = self.client.post('/api/deposit/', {'amount': '100.00'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Deposit successful")

    # 测试修改密码成功
    def test_change_password_success(self):
        self.client.credentials(HTTP_AUTHENTICATION='123456')
        response = self.client.post('/api/change_password/', {'newpassword': 'newpassword'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Password changed successfully")