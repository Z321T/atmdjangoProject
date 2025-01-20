from datetime import datetime
from decimal import Decimal
from django.db import models
from django.contrib.auth.hashers import make_password, check_password


# Create your models here.
# Account 类
class Account(models.Model):
    card_id = models.IntegerField(primary_key=True)  # 自动创建的主键字段
    password = models.CharField(max_length=128)  # 密码字段
    balance = models.DecimalField(max_digits=10, decimal_places=2)  # 余额字段，最多10位数字，包括2位小数
    user_id = models.CharField(max_length=50, null=True, blank=True)  # 用户ID
    transaction_history = models.JSONField(default=list, null=True, blank=True)  # 交易明细列表

    def __str__(self):
        return str(self.card_id)

    def set_password(self, raw_password):
        """加密并设置密码"""
        self.password = make_password(raw_password)
        self.save()

    def validate_pin(self, raw_password):
        """验证密码"""
        return check_password(raw_password, self.password)

    def check_balance(self):
        return self.balance

    def update_balance(self, amount):
        self.balance += Decimal(amount)
        self.save()

    def add_transaction(self, transaction):
        self.transaction_history.append(transaction)
        self.save()


# User 类
class User(models.Model):
    user_id = models.CharField(max_length=50, primary_key=True)  # 用户的唯一标识符
    name = models.CharField(max_length=100)  # 用户姓名
    id_number = models.CharField(max_length=20)  # 用户的身份证号
    accounts = models.ManyToManyField(Account)  # 用户关联的账户列表

    def authenticate(self, pin):
        for account in self.accounts.all():
            if account.validate_pin(pin):
                return True
        return False

    def get_account_info(self):
        return self.accounts.all()


# Transaction 类
class Transaction(models.Model):
    transaction_id = models.CharField(max_length=50, primary_key=True)  # 交易的唯一标识符
    type = models.CharField(max_length=20)  # 交易类型（如取款、存款、转账）
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # 交易金额
    date_time = models.DateTimeField(default=datetime.now)  # 交易的日期和时间
    from_account = models.ForeignKey(Account, related_name='from_account', on_delete=models.CASCADE)  # 交易的来源账户
    to_account = models.ForeignKey(Account, related_name='to_account', on_delete=models.CASCADE, null=True, blank=True)  # 交易的目标账户（转账时使用）

    def execute(self):
        if self.type == 'withdraw':
            if self.from_account.balance >= self.amount:
                self.from_account.update_balance(-self.amount)
                self.from_account.add_transaction(self)
                return True
        elif self.type == 'deposit':
            self.from_account.update_balance(self.amount)
            self.from_account.add_transaction(self)
            return True
        elif self.type == 'transfer':
            if self.from_account.balance >= self.amount and self.to_account:
                self.from_account.update_balance(-self.amount)
                self.to_account.update_balance(self.amount)
                self.from_account.add_transaction(self)
                self.to_account.add_transaction(self)
                return True
        return False

    def generate_record(self):
        return f"Transaction ID: {self.transaction_id}, Type: {self.type}, Amount: {self.amount}, Date: {self.date_time}"


# Log 类
class Log(models.Model):
    log_id = models.CharField(max_length=50, primary_key=True)  # 日志的唯一标识符
    action_type = models.CharField(max_length=20)  # 操作类型（如取款、存款）
    content = models.TextField()  # 日志内容
    date_time = models.DateTimeField(default=datetime.now)  # 日志记录的日期和时间

    def record_log(self, action_type, content):
        self.action_type = action_type
        self.content = content
        self.save()

    def export_log(self):
        return f"Log ID: {self.log_id}, Action: {self.action_type}, Content: {self.content}, Date: {self.date_time}"


# BankNetwork 类
class BankNetwork(models.Model):
    system_name = models.CharField(max_length=50)  # 银联系统的名称
    registered_accounts = models.ManyToManyField(Account)  # 已注册的账户列表

    def validate_account(self, account_number):
        return self.registered_accounts.filter(card_id=account_number).exists()

    def update_account_info(self, account):
        account.save()

    def process_transaction(self, transaction):
        return transaction.execute()


# SecurityModule 类
class SecurityModule(models.Model):
    encryption_algorithm = models.CharField(max_length=50)  # 用于加密的算法

    def encrypt_data(self, data):
        # 这里可以实现具体的加密算法
        return f"encrypted_{data}"

    def decrypt_data(self, data):
        # 这里可以实现具体的解密算法
        return data.replace("encrypted_", "")


# ATM 类
class ATM(models.Model):
    atm_id = models.CharField(max_length=50, primary_key=True)  # ATM 的唯一标识符
    location = models.CharField(max_length=100)  # ATM 的位置
    bank_network = models.ForeignKey(BankNetwork, on_delete=models.CASCADE)  # ATM 所属的银联系统
    security_module = models.ForeignKey(SecurityModule, on_delete=models.CASCADE)  # ATM 使用的安全模块

    def authenticate_card(self, card_number, pin):
        if self.bank_network.validate_account(card_number):
            decrypted_pin = self.security_module.decrypt_data(pin)
            return self.bank_network.registered_accounts.get(card_id=card_number).validate_pin(decrypted_pin)
        return False

    def process_transaction(self, transaction):
        return self.bank_network.process_transaction(transaction)

    def update_account_info(self, account):
        self.bank_network.update_account_info(account)
        return True


# Card 类
class Card(models.Model):
    card_number = models.CharField(max_length=50, primary_key=True)  # 卡号
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 持卡人
    account = models.ForeignKey(Account, on_delete=models.CASCADE)  # 关联的账户
    expiration_date = models.DateField()  # 过期日期
    cvv = models.CharField(max_length=3)  # 安全码

    def authenticate(self, pin):
        return self.user.authenticate(pin)

    def check_balance(self):
        return self.account.check_balance()

    def withdraw(self, amount):
        transaction = Transaction(type='withdraw', amount=amount, from_account=self.account)
        if transaction.execute():
            return transaction.generate_record()
        return "Withdrawal failed"

    def deposit(self, amount):
        transaction = Transaction(type='deposit', amount=amount, from_account=self.account)
        if transaction.execute():
            return transaction.generate_record()
        return "Deposit failed"

    def transfer(self, amount, target_account):
        transaction = Transaction(type='transfer', amount=amount, from_account=self.account, to_account=target_account)
        if transaction.execute():
            return transaction.generate_record()
        return "Transfer failed"