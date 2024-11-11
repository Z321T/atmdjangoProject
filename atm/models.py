from django.db import models


# Create your models here.
class Account(models.Model):
    card_id = models.IntegerField(primary_key=True)  # 自动创建的主键字段
    password = models.CharField(max_length=128)  # 密码字段
    balance = models.DecimalField(max_digits=10, decimal_places=2)  # 余额字段，最多10位数字，包括2位小数

    def __str__(self):
        return str(self.card_id)
