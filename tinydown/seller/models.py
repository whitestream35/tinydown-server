from django.db import models

# 账号
class Account(models.Model):

    # id
    account_id = models.IntegerField(default=0)
    # 用户名
    account_name = models.CharField(max_length=200)
    # 密码
    account_password = models.CharField(max_length=200)
    # 状态
    state = models.IntegerField(default=0)
    # 创建时间
    create_date = models.DateTimeField('date created')
    # 账户类型
    account_type = models.IntegerField(default=1)
    # 账户价格
    account_price = models.DecimalField(default=1.0, max_digits=100.0, decimal_places=2)
    # 当前使用人数
    current_users = models.IntegerField(default=0)

# 订单
class Order(models.Model):

    # id
    order_id = models.IntegerField(default=0)
    # 关联账户
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    # 创建时间
    create_date = models.DateTimeField('date created')
    # 结束时间
    end_date = models.DateTimeField('date end')
    # 类型
    order_type = models.IntegerField(default=0)
    # 状态
    state = models.IntegerField(default=0)
    # 价格
    price = models.DecimalField(default=1.0, max_digits=100.0, decimal_places=2)
    # 