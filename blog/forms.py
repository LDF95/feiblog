# _*_ coding:utf8 _*_
from  django import forms

class RegForm(forms.Form):
    """
    用户注册表单
    """
    email=forms.EmailField(required=True,max_length=100,error_messages={"required" : "用户名不能为空"})
    password=forms.CharField(required=True,min_length=8,error_messages={"required" :"密码不能为空"})

class LoginForm(forms.Form):
    """
    用户登录表单
    """
    email=forms.EmailField(required=True,max_length=100,error_messages={"required" : "用户名不能为空"})
    password=forms.CharField(required=True,min_length=8,error_messages={"required" :"密码不能为空"})


# 用户评论表单
class CommentForm(forms.Form):
    comment = forms.CharField(required=True, max_length=100, error_messages={"required": "内容不能为空"})
