from django.db import models

# Create your models here.


#抽象父类 转换queryset对象为json数据再序列化成字符串
class BaseModel(models.Model):
    def to_json(self,querset):
        import json

        res = json.dumps(querset.values()) #values 将queryset对象转换为字典 再通过系统内置json 类序列化为json字符串
        return res
    class Meta:
        abstract = True


class Team(models.Model):
    tname = models.CharField(max_length=20)

    def __str__(self):
        return self.tname

    class Meta:
        db_table = 'team'

class Student(models.Model):
    sname = models.CharField(max_length=30)
    team = models.ForeignKey(Team,on_delete=models.CASCADE)

    def __str__(self):
        return  self.sname

    class Meta:
        db_table = 'student'