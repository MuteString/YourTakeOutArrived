from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    nickname = models.CharField(max_length=100, blank=True, verbose_name=u"昵称")
    Admin = u'系统管理员'
    Manager = u'商家'
    Customer = u'客户'
    ROLE_CHOICES = (
        (Manager, u'商家'),
        (Customer, u'顾客'),
    )
    role = models.CharField(max_length=100, choices=ROLE_CHOICES, verbose_name=u"角色")

    class Meta(AbstractUser.Meta):
        pass


class Merchant(models.Model):
    username = models.CharField(max_length=100, verbose_name=u"用户名", primary_key=True)
    logo = models.ImageField(verbose_name=u"商家Logo")
    name = models.CharField(max_length=100, verbose_name=u"店名")
    dis_price = models.IntegerField(verbose_name=u"配送费")
    score = models.FloatField(verbose_name=u"评分")
    product_class = models.TextField(verbose_name=u"商品类型")
    avg_time = models.IntegerField(verbose_name=u"平均送达时间")
    month_couter = models.IntegerField(verbose_name=u"月销售量")
    tag_list = models.TextField(verbose_name=u"标签")
    notice = models.TextField(verbose_name=u"公告")


class Dishes(models.Model):
    username = models.CharField(max_length=100, verbose_name=u"所属商家")
    name = models.CharField(max_length=100, verbose_name=u"菜品名")
    price = models.FloatField(verbose_name=u"价格")
    rate = models.FloatField(verbose_name=u"评分")
    pronum = models.IntegerField(verbose_name=u"菜品编号")
