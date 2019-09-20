"""cookie_admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from app01 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('index/', views.index),
    path('hello', views.hello),
    path('end/', views.end),
    re_path(r'computer$', views.computer),#注意 这里必须引入并应用re_path才能使$起作用。不然就是简单的字符$了。
    path('cbv', views.CBV.as_view()),#注意 这里必须有括号 才可以
]
#总结得出结论：路由的地址，view中有杠就必须浏览器地址中加，没有就必须不加。不然都会报错。
