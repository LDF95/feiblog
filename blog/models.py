# _*_ coding:utf8 _*_
from __future__ import unicode_literals
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.

class User(AbstractUser):
    """
    用户表
    """

    # username = models.CharField(verbose_name="姓名",max_length=50)
    # email = models.CharField(verbose_name="邮箱",max_length=50)
    # password = models.CharField(verbose_name="密码",max_length=128)
    mobile = models.CharField(verbose_name="手机号码",max_length=11,blank=True,null=True)
    birthday = models.DateField(verbose_name="生日",blank=True,null=True)
    gen = (
        ("male","男"),
        ("female","女")
    )
    gender = models.CharField(verbose_name="性别",choices=gen,default="male",max_length=10)
    image = models.ImageField(verbose_name="头像",upload_to="users/%Y/%m",blank=True,null=True)

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username

class Author(models.Model):
    """
    作者表
    """
    name = models.CharField(verbose_name="姓名",max_length=50)
    desc = models.TextField(verbose_name="简介",max_length=500)
    profession=models.CharField(verbose_name="专业",max_length=50)
    years = (
        ("1","2018年"),
        ("2","2017年"),
        ("3","2016年"),
        ("4","2015年"),
    )
    year = models.CharField(verbose_name="年份", choices=years, default="1", max_length=10)
    class Meta:
        verbose_name = "作者"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

class Blog(models.Model):
    """
    博文表
    """
    title = models.CharField(verbose_name="标题", max_length=50)
    desc = models.CharField(verbose_name="描述", max_length=100)
    # content = models.TextField(verbose_name="内容", max_length=50000)
    content = UEditorField(verbose_name="内容", width=600, height=300, default="",
                           imagePath="content/%(basename)$_%(datetime)$.%(extname)$",
                         filePath="content/%(basename)$_%(datetime)$.%(extname)$")

    image = models.ImageField(verbose_name="封面", upload_to="blog/%Y/%m")
    author = models.ForeignKey(Author,verbose_name="所属作者")
    direction = (
        ("d1", "网络"),
        ("d2", "运维"),
        ("d3", "编程"),
        ("d4", "安全"),
        ("d5", "深度学习"),
        ("d6", "程序人生"),
    )
    direction = models.CharField(verbose_name="岗位方向", choices=direction, default="d1", max_length=10)

    categories = (
        ("t1", "CCIE网络"),
        ("t2", "Linux系统"),
        ("t3", "Python入门"),
        ("t4", "Web安全"),
        ("t5", "Django框架"),
        ("t6", "数据库"),
        ("t7", "前端"),
        ("t8", "其他"),
    )
    category = models.CharField(verbose_name="类别", choices=categories, default="t1", max_length=10)
    pub_time = models.DateTimeField(verbose_name="发布时间", default=datetime.now)
    read_counts = models.IntegerField(verbose_name="阅读次数", default=0)
    class Meta:
        verbose_name = "博文"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    """
    评论
    """
    comment = models.TextField(verbose_name="评论", max_length=600)
    pub_time = models.DateTimeField(verbose_name="发布时间", default=datetime.now)
    blog = models.ForeignKey(Blog, verbose_name="文章外键")
    user = models.ForeignKey(User, verbose_name="用户外键")

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = verbose_name