from django.urls import path, include
import blog.views

# 路由配置
urlpatterns = [
    path('hello/', blog.views.hello),
    path('getBlog/', blog.views.return_modules),
    path('tmp/', blog.views.helloTmp),
    path('list/', blog.views.return_list),
    path('detail/<int:id>', blog.views.detail_by_id),
    # 不需要进行后缀
    path('page/', blog.views.page_list),
]
