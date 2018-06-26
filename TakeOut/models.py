from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100, verbose_name=u"用户名")
    password = models.(max_length=100, )
