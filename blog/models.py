from django.db import models

# Create your models here.

class BlogModel(models.Model):
    # 唯一标识符
    id = models.AutoField(primary_key = True)
    # 文章标题
    title = models.TextField()
    # 文章作者
    author = models.TextField()
    # 文章摘要
    bref_content = models.TextField()
    # 文章内容
    content = models.TextField()
    # 发布日期
    publish_time = models.DateTimeField(auto_now = True)

    # 设置文章标题到amdin后台列表中
    def __str__(self):
        return self.title