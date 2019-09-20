from django.shortcuts import render,HttpResponse
import time
from app01.models import *
from django.db.models import Avg,Min,Sum,Max,Count
from django.db.models import F,Q
# Create your views here.

def register(request):
    t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    li = [
        "陈飞",
        "付景海",
        "周重凯",
        "周婧",
    ]

    return render(request,"index.html",locals())
def login(request):
    return render(request,"login.html",locals())
def index (request):
    return render(request,"index111.html")
def add(request):
    # 第一种方法：
    # b = Book(name="python基础",price=99,author="seajay",pub_date="2017-12-12")
    # b.save()
    # 推荐使用 ：第二种方法
    # Book.objects.create(name="狼图腾",price=99,author="这个庆才",pub_date="2019-09-06",publish_id=3)#这种方法不用保存即可存入
    #批量存的话 循环即可
    # price = 99
    # for i in range(0, 5):
    #     price += i
    #     Book.objects.create(name="狼图腾%s" % i, price=price, author="崔庆才", pub_date="2017-02-11", publish_id=2)
    # 一对多的情况 增加一本书 多了一个外键字段
    #一对多 第一种添加记录 含外键 的方式
    # Book.objects.create(name="linux运维",price=99,pub_date="2017-12-12",publish_id=45)
    #一对多 第二种添加记录 含外键 的方式
    # publish_obj = Publish.objects.filter(name="机械出版社")[0]
    # print(type(publish_obj))
    # Book.objects.create(name="羊皮卷", price=3999, pub_date="2011-8-14",publish= publish_obj) #将id号拿过来 赋值过去
    # Book.objects.create(name="墨菲定律", price=8999, pub_date="2011-1-31",publish= publish_obj) #将id号拿过来 赋值过去
    # Book.objects.create(name="我的成功可以复制", price=25, pub_date="2013-1-21",publish= publish_obj) #将id号拿过来 赋值过去
    # Book.objects.create(name="雨人", price=3999, pub_date="2001-1-11",publish= publish_obj) #将id号拿过来 赋值过去
    # 推荐外键表查询方法：第三种情况 查找关联表的其它字段的信息  book_obj.publish为一个点外键  拿出来的一定为一个对象。多对多拿出来的则为多个对象。
    # book_obj = Book.objects.get(name="python")
    # print(book_obj.publish.name)
    # 查询人民出版社出版的书籍及其价格 方法一（正向查询）：
    # pub_obj = Publish.objects.filter(name="人民出版社")[0]
    # print(pub_obj)
    # ret = Book.objects.filter(publish=pub_obj).values("name","price")
    # print(ret)
    # 上述方法有点麻烦 直接通过外键拿到所有关联的对象  于是有了方法二（逆向查询）：
    # publish_obj = Publish.objects.filter(name="人民出版社")[0]
    # print(publish_obj.book_set.all())
    # print(publish_obj.book_set.all().values("name","price"))
    # 推荐使用：  还有一个查询方法更快更实用 即 双下划线 需求假设不变 找人民出版社出版的书籍 方式三：万能的双下划线
    # ret =Book.objects.filter(publish__name="人民出版社").values("name","price")
    # print(ret)
    # 新需求 查询python出版社的名字
    # ret2 = Publish.objects.filter(book__name="python").values("name")#这是基于Publish
    # ret3 = Book.objects.filter(name="python").values("publish__name") #这是基于外键
    # print(ret2)
    # 查询北京的出版社出版的所有的书
    #其它需求
    # ret4 = Book.objects.filter(publish__city="北京").values("name") #这种方式非常方便快捷
    # ret5 = Book.objects.filter(pub_date__lt="2017-07-01",pub_date__gt="2017-01-02").values("name")
    # print(ret5)
    #ret5 = Book.objects.filter(pub_date__lt="2017-07-01",price__gt="2017-01-01").values("publish__name")
    #多对多的关系：
    # 不能通过orm直接对新建的多对多的表进行创建新记录，只能通过对象的方式绑定
    # book_obj = Book.objects.get(id=3).authors.all()
    # print(book_obj)
    # 反向查询
    # author_obj = Author.objects.get(id = 2)
    # print(author_obj.book_set.all())
    #正向反向可以查询了 现在来绑定
    # book_obj = Book.objects.get(id = 6) #找到一本书
    # author_obj = Author.objects.all()
    # book_obj.authors.add(*author_obj)
    #如果添加一个 则不用加*
    # book_obj = Book.objects.get(id = 5) #找到一本书
    # author_obj = Author.objects.get(name="付景海")
    # book_obj.authors.add(author_obj)
    #如果删除一个关系 则用remove
    # book_obj = Book.objects.get(id = 5) #找到一本书
    # author_obj = Author.objects.get(name="付景海")
    # book_obj.authors.remove(author_obj)
    #多对多查询  某作者出过的书籍名称及价格
    # ret = Book.objects.filter(authors__name="陈飞").values("name","price")
    # print(ret)
    # 聚合函数计算所有价格的平均值或者和
    # ret = Book.objects.all().aggregate(Avg("price"))
    # ret2 = Book.objects.all().aggregate(Sum("price"))
    # print(ret)
    # print(ret2)
    # 结合多表查询 查询付景海出的所有的书的价格总和
    # ret3 = Book.objects.filter(authors__name="付景海").aggregate(Sum("price"))
    # print(ret3)  # -->  {'price__sum': 359}
    #如果想自定义输出键的名字 则需要aggregate(seajay=Sum("price")
    #先进行分组 再筛选  就可以确认每个作者出的书的价格的总和
    # ret4 = Book.objects.values("authors__name").annotate(Sum("price"))
    # print(ret4)
    #查询每个出版社价格最低的
    # ret5 = Publish.objects.values("name").annotate(Min("book__price"))
    # print(ret5)
    #修改每本书的价格增加10元钱  涉及F查询与Q查询 先在表头引入
    ret6 = Book.objects.all().update(price=F("price")+10)
    #Q 语句的使用 配合管道夫|和|~使用 实现与和非的效果 波浪号怎么输入
    # 如果Q查询和关键字查询一起配合使用，Q查询需要放在前面。
    ret7 = Book.objects.filter(Q(name="狼图腾")|Q(price="87"))
    ret7 = Book.objects.filter(Q(name="狼图腾")|Q(price="87"))
    return HttpResponse("查询外键表的内容成功 已经打印")
def update(request):
    Book.objects.filter(name="python基础").update(price=84)
    return HttpResponse("改好价格了")
def delete(request):
    # Book.objects.filter(id="3").delete()
    Book.objects.filter(name="狼图腾0").delete()
    return HttpResponse("删除成功了")
def deleteif(request):
    for i in range(10,18):
        Book.objects.filter(id="%d"%i).delete()
    return HttpResponse("删除成功了")
def select(request):
    #疑问 何时能用到first、last和索引[0]  .values 的时候输出为字典。get的时候会出现输出多个报错的问题。
    #查询所有
    # book_list = Book.objects.all()
    # print(book_list)
    #查询id为2的一条记录 或替换为其它条件
    # book_list = Book.objects.filter(author="崔庆才")
    #切片方式查询第多少条到多少条
    # book_list = Book.objects.all()[:3]
    #间隔取数据
    # book_list = Book.objects.all()[::2]
    # 倒序排列
    # book_list = Book.objects.all()[::-1]
    # 取第一行记录 报错 因为一个对象无法for循环
    # book_list = Book.objects.all().first() #报错 待研究
    # book_list = Book.objects.all().last()  #报错 待研究
    # 如果只想取出作者为seajay的所有书的名字：
    # book_list = Book.objects.filter(author="seajay").values("name")#结果为一个字典
    # print(book_list)  #输出为一个字典 还有一个values_list 可以输出为元组组成的列表
    # 查询排除条件之外的所有数据  如果只显示name，则再加个.values
    # book_list = Book.objects.exclude(name="狼图腾2")
    #按照作者进行去重。但是不能整行记录去重。因为有不同的主键。
    # book_list = Book.objects.all().values("author").distinct()
    # 可以进行计数
    # book_count = Book.objects.all().values("author").distinct().count()
    # print(book_count)
    # 万能的双下划线"__" 查询价格大于等于90的书的名字和价格
    # book_list = Book.objects.filter(price__gt=90).values("name","price")
    # name__contains 包含   icontains 不区分大小写的包含
    book_list = Book.objects.filter(name__icontains="y").values("name", "price")
    # 还有若干模糊查询的 模糊匹配的  这些都为单表查询  id__in  id__range 等等。

    return render(request,"index111.html",{"book_list":book_list})