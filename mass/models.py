from django.db import models


# Create your models here.


class User(models.Model):
    gender = (
        ('male', ' 男'),
        ('female', '女')
    )

    superuser = (
        (0, '超级管理员'),
        (1, '普通用户')
    )

    user_active = (
        (1, '在线'),
        (2, '离线'),
        (3, '隐身')
    )

    username = models.CharField(max_length=128, unique=True, verbose_name='用户名')
    password = models.CharField(max_length=256, verbose_name='密码')
    is_superuser = models.SmallIntegerField(choices=superuser, default=1, verbose_name="超级用户")
    is_active = models.SmallIntegerField(choices=user_active, default=2, verbose_name="状态")
    email = models.EmailField(unique=True, verbose_name='邮箱')
    sex = models.CharField(max_length=32, choices=gender, default='男', verbose_name='性别')
    c_time = models.DateTimeField(auto_now_add=True, verbose_name='时间')

    def __unicode__(self):
        return self.username

    class Meta:
        ordering = ["c_time"]
        verbose_name = "用户表"
        verbose_name_plural = "用户数据"
