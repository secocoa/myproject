from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50,null=True)
    password = models.CharField(max_length=32)
    ip = models.CharField(max_length=15,null=True)
    allowed = models.BooleanField(default=True)

    def __str__(self):
        return '用户名: ' + self.username +' 密码：' + self.password


