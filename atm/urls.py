from django.urls import path
from django.contrib.staticfiles.views import serve
from .views import LoginView, WithdrawView, BalanceView, TransferView, DepositView, ChangePasswordView
app_name = 'atm'

urlpatterns = [

    path('static/<path:path>', serve),
    path('login/', LoginView.as_view(), name='login'),  # 登录视图
    path('withdraw/', WithdrawView.as_view(), name='withdraw'),    # 提现视图
    path('balance/', BalanceView.as_view(), name='balance'),    # 查询余额视图
    path('transfer/', TransferView.as_view(), name='transfer'),    # 转账视图
    path('deposit/', DepositView.as_view(), name='deposit'),    # 存款视图
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),    # 修改密码视图

]
