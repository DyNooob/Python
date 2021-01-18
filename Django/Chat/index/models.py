from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


# 导入Django自带用户模块

# 文章分类
class Chat(models.Model):
    user_id = models.CharField('用户id', max_length=50, default='')
    user_name = models.CharField('用户名', max_length=50)
    chat_data = models.CharField('聊天数据', max_length=999)
    chat_time = models.DateTimeField('时间', auto_now_add=True)

    class Meta:
        verbose_name = '聊天数据'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user_id
