# _*_ coding:utf8 _*_
from django.contrib import admin
from models import User, Author, Blog

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email',)  # 实现展示功能
    list_filter = ('username', 'email',)  # 实现过滤器功能
    search_fields = ('username', 'email',) # 实现搜索功能
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc',)
    list_filter = ('name', 'desc',)
    search_fields =('name', 'desc',)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'direction',)
    list_filter = ('title', 'desc', 'direction',)
    search_fields =('title', 'desc', 'direction',)


admin.site.register(User, UserAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Blog, BlogAdmin)

