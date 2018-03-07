# _*_ coding:utf8 _*_
from django.shortcuts import render, redirect, render_to_response
from django.views.generic import View
from django.db.models import Q  # 导入或逻辑判断模块
from django.contrib.auth.hashers import make_password  # 导入密码加密模块
from forms import RegForm, LoginForm, CommentForm
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import logout, login, authenticate    #  导入用户登入、出,认证功能
from django.core.urlresolvers import reverse  # 导入reverse 解析模块，用于重定向
from django.http import HttpResponseRedirect, HttpResponse

from blog.models import Blog, Author, User, Comment  #  导入博文数据表

# Create your views here.
class BloListView(View):
    """
    博文列表类
    """
    def get(self, request):
        # 取出所有面经
        all_blogs = Blog.objects.all().order_by('-read_counts')  # 获取所有的博文对象（列表）

        # 点击搜索
        keywords = request.GET.get('keywords', "")
        if keywords:
            all_blogs = all_blogs.filter(Q(title__icontains=keywords) | Q(desc__icontains=keywords) |
                                            Q(content__icontains=keywords))

        # 基于方向分类
        direction = request.GET.get('direction', "")
        if direction:
            all_blogs = Blog.objects.filter(direction=direction)
        # 基于分类的分类
        category = request.GET.get('category', "")
        if category:
            all_blogs = Blog.objects.filter(category=category)

        # 基于年级的分类(基于年级找作者，基于作者找博文)
        year = request.GET.get('year', "")
        if year:
            authors = Author.objects.filter(year=year)
            all_blogs = Blog.objects.none()

            for author in authors:
                blogs = author.blog_set.all()
                all_blogs = all_blogs | blogs

    # 对博文列表进行分页处理
        try:
            page = request.GET.get('page',1)
        except(PageNotAnInteger, EmptyPage):
            page = 1
        p = Paginator(all_blogs, 2, request=request)
        blogs = p.page(page)
        return render(request, "blog_list.html", {
            "all_blogs": blogs,  # 传递模板变量给模板文件
        })


class BloDetailView(View):
    """
    面经详情页类
    """
    def get(self, request, blog_id):
        blog = Blog.objects.get(id=int(blog_id))
        #  增加阅读次数
        blog.read_counts +=1
        blog.save()
        # 推荐博文（同类别）
        recommended_tag = blog.category  # category_tag
        recommended_blogs = Blog.objects.filter(category=recommended_tag).exclude(id=int(blog_id)).order_by('-read_counts')[:3]

        # 推荐博文（同方向）
        recommended_tag2 = blog.direction   # direction_tag
        recommended_blogs2 = Blog.objects.filter(direction=recommended_tag2).exclude(category=recommended_tag).order_by('-read_counts')[:3]
        comments = Comment.objects.filter(blog=blog).order_by("-pub_time")  # 取出该面经所有评论

        return render(request, "blog_detail.html", {
            "blog": blog,
            "recommended_blogs": recommended_blogs,
            "recommended_blogs2" : recommended_blogs2,
            "comments": comments,
        })



class RegView(View):
    """
    用户注册
    """
    def get(self, request):  # 用户访问注册页面
        return render(request, "reg.html", {})

    def post(self, request):
        regform = RegForm(request.POST)  # 通过注册表单获取用户提交的内容(form表单中的name字段),然后创建实例regform
        if regform.is_valid():  # 若表单有效性验证成功
            username = request.POST.get("email", "")  # 获取用户/邮箱/密码信息
            email = request.POST.get("email", "")
            password = request.POST.get("password", "")
            user = User()  # 创建用户实例
            user.username = username  # 为用户名/邮箱/密码数据属性赋值
            user.email = email
            user.password = password
            user.password = make_password(password)  # 将密码加密处理
            user.save()  # 保存到数据库(除了用save,也可以用create方式)
            return render(request, "login.html")  # 验证有效之后,返回登录页面
        else:
            return render(request, "reg.html", {"regform": regform})  # 如果表单验证失败,则停留在注册页面

class LoginView(View):
    """
    用户登录类
    """
    def get(self, request):  # 用户访问登录页
        return render(request, "login.html", {})

    def post(self, request):
        loginform = LoginForm(request.POST)
        if loginform.is_valid():
            username = request.POST.get("email", "")
            password = request.POST.get("password", "")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
            else:
                return render(request, 'login.html', {"error": '登录认证失败'})
            return HttpResponseRedirect(reverse("blolist")) # 重定向到首页
        else:
            return render(request, "login.html", {"error": '登录验证失败'})

class LogoutView(View):
    """
    用户注销
    """
    def get(self,request):
        logout(request)
        return HttpResponseRedirect(reverse("blolist"))


class IndexView(View):
    """
    首页
    """
    def get(self, request):
        all_blogs = Blog.objects.all().order_by('-read_counts')[:6]
        return render(request, "index.html", {
            "all_blogs": all_blogs,
        })

class AddCommentView(View):
    """
    添加评论
    """
    def post(self, request, blog_id):
        blog = Blog.objects.get(id=int(blog_id))
        if request.user.is_authenticated():  # 判断用户是否登录
            comment_form = CommentForm(request.POST)  # 创建表单实例
            if comment_form.is_valid():  # 判断表单输入是否有效
                content = request.POST.get("comment")  # 若有效则获取内容
                comments = Comment()  # 创建评论实例
                comments.comment = content  # 为评论字段赋值
                comments.user = request.user  # 评论用户
                comments.blog = blog # 被评论面经
                comments.save()  # 保存评论
            else:
                return render(request, "login.html", {  # 若用户没登录,则跳转到登录页面
                    "error": "请登录后再评论"
                })
        return redirect(request.META['HTTP_REFERER'])  # 刷新页面(重定向到原来的网址,采用get方法)
