from django.contrib import admin
from app01 import models
# Register your models here.
#自己配置book的类 显示可编辑并且可以在外面显示
class BookAdmin(admin.ModelAdmin):
    # 设置姓名 价格等属性可以显示出来 在主页面 不用点进去看了
    list_display = ("id","name","price","pub_date")
    # 增加设置姓名和价格可以随时方便的修改和保存
    list_editable = ("name","price")
    # 增加一个 作者的两个列表来回移动选择的筛选框 注意必须有逗号 表示元组
    filter_horizontal = ("authors",)
    # 设置每页显示3条
    list_per_page = 3
    #设置可以搜索的字段项目 注意 这里必须有__name关联查询，不然查询什么条件都会报错
    search_fields = ("id","name","publish__name")
    # 过滤
    list_filter = ("pub_date","publish")


admin.site.register(models.Book,BookAdmin)
admin.site.register(models.Author)
admin.site.register(models.Publish)