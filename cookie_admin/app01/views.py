from django.shortcuts import render,redirect,HttpResponse
import datetime
from django.views import View
# Create your views here.
def login(request):
    print("第一次进来cookie",request.COOKIES)
    print("第一次进来session",request.session)
    if request.method == "POST":
        name = request.POST.get("user")
        pwd = request.POST.get("pwd")
        if name == "seajay" and pwd == "123":
            # ret = redirect("/index/")
            # # #在这里自己设置cookie cookie想象成钱包  redirect是有返回值的。所以可以在这里设置cookie的字典键值对
            # ret.set_cookie("bilibili","acfine",max_age=10)# 设置十秒钟为十秒内可以登录 超过10秒就不行了
            # ret.set_cookie("bilibili","acfine",expires=datetime.datetime.utcnow()+datetime.timedelta(days=3))# 设置从现在开始三天有效
            # # print("第二次进来",request.COOKIES)
            # return ret
            request.session["is_login"] = True #默认session在服务端保存15天
            request.session["user"] = name
            request.session.set_expiry(10)# 设置有效期限
            return  redirect("/index/")
    return render(request,"login.html",locals())
def index(request):
    # if request.COOKIES.get("bilibili",None):
    #     name = "付景海"
    #     return render(request,"index.html",locals())
    if request.session.get("is_login",None):
        name = request.session.get("user",None)
        return render(request,"index.html",locals())
    else:
        return redirect("/login/")

class CBV(View):
    def get(self,request):
        return HttpResponse("CBV.GET")
    def post(self,request):
        return HttpResponse("CBV.POST")

def hello(request):
    return HttpResponse("hello")
def end(request):
    return HttpResponse("end")
def computer(request):
    return HttpResponse("computer")