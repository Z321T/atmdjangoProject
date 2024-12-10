from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Account
from decimal import Decimal
# Create your tests here.


class ATMViewsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = Account.objects.create(card_id="123456", password="password", balance=Decimal('1000.00'))
        self.target_user = Account.objects.create(card_id="654321", password="password", balance=Decimal('500.00'))

    def test_login_success(self):
        response = self.client.post('/login/', {'cardId': '123456', 'password': 'password'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Login successful")

    def test_login_invalid_card(self):
        response = self.client.post('/login/', {'cardId': '000000', 'password': 'password'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_login_invalid_password(self):
        response = self.client.post('/login/', {'cardId': '123456', 'password': 'wrongpassword'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_withdraw_success(self):
        self.client.credentials(HTTP_AUTHENTICATION='123456')
        response = self.client.post('/withdraw/', {'withdrawmoney': '100.00'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Withdraw successful")

    def test_withdraw_insufficient_funds(self):
        self.client.credentials(HTTP_AUTHENTICATION='123456')
        response = self.client.post('/withdraw/', {'withdrawmoney': '2000.00'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Withdraw failure")

    def test_balance_view(self):
        self.client.credentials(HTTP_AUTHENTICATION='123456')
        response = self.client.get('/balance/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['balance'], str(self.user.balance))

    def test_transfer_success(self):
        self.client.credentials(HTTP_AUTHENTICATION='123456')
        response = self.client.post('/transfer/', {'account': '654321', 'amount': '100.00'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Transfer successful")

    def test_transfer_insufficient_funds(self):
        self.client.credentials(HTTP_AUTHENTICATION='123456')
        response = self.client.post('/transfer/', {'account': '654321', 'amount': '2000.00'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Transfer failure")

    def test_deposit_success(self):
        self.client.credentials(HTTP_AUTHENTICATION='123456')
        response = self.client.post('/deposit/', {'amount': '100.00'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Deposit successful")

    def test_change_password_success(self):
        self.client.credentials(HTTP_AUTHENTICATION='123456')
        response = self.client.post('/change_password/', {'newpassword': 'newpassword'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Password changed successfully")
