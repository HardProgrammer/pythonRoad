from django.contrib import admin

# Register your models here.注册模型进行后台管理
from .models import BlogModel

admin.site.register(BlogModel)
