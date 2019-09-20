from django.db import models

# Create your models here.
#先写一个类 继承model.Model
class Book(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    pub_date = models.DateField()
    # author = models.CharField(max_length=20,null=False)
    #既然书是一对多的多的一方 一定在多的一方建立外键 书与出版社是一对多关系 书对作者是多对多的关系
    publish = models.ForeignKey("Publish",on_delete=models.CASCADE)  #默认关联附表的主键 django会给你的外键自动赋上一个id,所以自己命名不用加_id
    #必须加引号，"Publish"，不然需要把publish放在上面。
    authors = models.ManyToManyField("Author")
    def __str__(self): # 打印book对象时 能够输出当前引用记录的name属性。
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField("20")
    year = models.IntegerField("40")
    def __str__(self):
        return self.name


class Publish(models.Model):
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)

# class Book_Author(models.Model):
#     #还可以通过自己建立的方式 也可以自己创建多对多的表 用关联两个外键的方式 这时就要去掉上面的Manytomany了
#     book = models.ForeignKey("Book")
#     author = models.ForeignKey("Author")

