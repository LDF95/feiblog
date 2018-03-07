# _*_ coding:utf8 _*_

"""feiblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve  # 模板文件图片解析模块
from settings import MEDIA_ROOT   # 模板文件图片解析路径

from blog.views import BloListView, BloDetailView, RegView, LoginView, LogoutView, IndexView,  AddCommentView  #  导入Views函数/类

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),  # 管理媒体文件路径和处理模块
    url(r'^blolist/$', BloListView.as_view(), name="blolist"),  # 博文映射
    url(r'^blodetail/(?P<blog_id>\d+)/$', BloDetailView.as_view(), name="blodetail"), # 面经详情映射
    url(r'^ueditor/', include('DjangoUeditor.urls')),  #   增加编辑器映射
    url(r'^register/$', RegView.as_view(), name="register"),  # 用户注册映射
    url(r'^login/$', LoginView.as_view(), name="login"),  # 用户登录页映射
    url(r'^logout/$', LogoutView.as_view(), name="logout"),  # 用户注销映射
    url(r'^$', BloListView.as_view(), name="blolist"),  # 首页映射
    url(r'^addcomment/(?P<blog_id>\d+)/$', AddCommentView.as_view(), name="addcomment"),  # 用户评论映射
#    url(r'^$', IndexView.as_view(), name="index"),  # 首页映射

]
