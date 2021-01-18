from django.db import models

# Create your models here.
class Music(models.Model):
    id = models.AutoField(max_length=11, db_column='music_id', primary_key=True, verbose_name='id')
    name = models.CharField(max_length=255, db_column='music_name', blank=True, verbose_name='歌曲名称')
    singer = models.CharField(max_length=255, db_column='singer', blank=True, verbose_name='歌手名称')
    came_from = models.CharField(max_length=255, db_column='came_from', blank=True, verbose_name='专辑')
    kbps = models.CharField(max_length=255, db_column='music_kbps', blank=True, verbose_name='码率')
    size = models.CharField(max_length=255, db_column='size', blank=True, verbose_name='文件大小')
    language = models.CharField(max_length=255, db_column='music_language', blank=True, verbose_name='语种')
    released_data = models.CharField(max_length=255, db_column='released_data', blank=True, verbose_name='发行日期')
    url = models.CharField(max_length=255, db_column='bdyun_url', blank=True, verbose_name='百度云链接')
    password = models.CharField(max_length=255, db_column='bdyun_password', blank=True, verbose_name='百度云密码')

    # 内部类
    class Meta:
        db_table = 'music_info'
        verbose_name = '音乐'
        verbose_name_plural = verbose_name
