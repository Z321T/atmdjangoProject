import os
import django

# 设置 Django 环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'atmdjangoProject.settings')  # 替换为你的项目名
django.setup()

from atm.models import Account  # 替换为你的应用名和模型名
from decimal import Decimal

# 创建用户 1
user1 = Account(
    card_id=240001,
    balance=Decimal('10000.00'),
    user_id='user1'
)
user1.set_password('24010001')  # 设置加密密码
user1.save()

# 创建用户 2
user2 = Account(
    card_id=240002,
    balance=Decimal('20000.00'),
    user_id='user2'
)
user2.set_password('24010002')  # 设置加密密码
user2.save()

# 创建用户 3
user3 = Account(
    card_id=240003,
    balance=Decimal('1500.00'),
    user_id='user3'
)
user3.set_password('24010003')  # 设置加密密码
user3.save()

print("Users created successfully!")