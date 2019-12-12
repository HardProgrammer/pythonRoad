from django.shortcuts import render
from django.http import HttpResponse
from blog.models import BlogModel
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

# Create your views here.
def hello(request):
    return HttpResponse("Hello world ! ")

# 模板返回
def helloTmp(request):
    context = {}
    blog = BlogModel.objects.all()[0]
    title = blog.title
    bref_content = blog.bref_content
    content = blog.content
    publish_time = blog.publish_time
    context["name"] = blog.title
    context["content"] = blog.content
    return render(request, 'hello.html', context)

# 返回相关模型信息
def return_modules(request):
    # 获取第一个文章数据
    blog = BlogModel.objects.all()[0]
    title = blog.title
    bref_content = blog.bref_content
    content = blog.content
    publish_time = blog.publish_time
    return_str = 'title: %s,bref_content: %s,content: %s,publish_time:%s' % (
        title, bref_content, content, publish_time)
    return HttpResponse(return_str)

# 返回列表
def return_list(request):
    blogList = BlogModel.objects.all()
    return render(request, "index.html", {"blog_list": blogList})

# 根据Id获取当前文章
def detail_by_id(request, id):
    blogList = BlogModel.objects.all()
    for blog in blogList:
        if blog.id == id:
            # 封装一下文本
            return render(request, 'detail.html', {"article": blog})


# 实现文章分页
def page_list(request):
    pageSize = 10
    currenPage = request.GET.get('page')
    blogList = BlogModel.objects.all()
    #传入总数据和每页显示的数据
    paginator = Paginator(blogList, pageSize)
    try:
        # 返回当前页面的数据
        blogList = paginator.page(currenPage)
    
    except PageNotAnInteger:
         # 返回第一页的数据
        blogList = paginator.page(1) 

    except EmptyPage:
        # 返回最后一个页面的数据
        blogList = paginator.page(paginator.num_pages)
    
    return HttpResponse(blogList)

