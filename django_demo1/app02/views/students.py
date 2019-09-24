from django.shortcuts import render,redirect

from app02 import models


def get_students(request):
    stu_list = models.Student.objects.all()
    # for row in stu_list:
    #     print(row.id,row.username,row.cs.title)
    return render(request,"get_students.html",locals())

def add_students(request):
    if request.method == "GET":
        cs_list = models.Classes.objects.all()
        # for row in cs_list:
        #     print(row.id,row.title)
        return render(request,"add_students.html",{"cs_list":cs_list})
    elif request.method == "POST":
        u = request.POST.get("username")
        a = request.POST.get("age")
        g = request.POST.get("gender")
        c = request.POST.get("cs")

        models.Student.objects.create(
            username=u,
            age=a,
            gender=g,
            cs_id=c
        )
        return redirect("/students.html")

def del_students(request):
    nid = request.GET.get("nid")
    models.Student.objects.filter(id=nid).delete()
    return redirect("/students.html")
def edit_students(request):
    #复制来一段
    # if request.method == "GET":
    #     nid = request.GET.get("nid")
    #     obj = models.Classes.objects.filter(id = nid).first()
    #     return render(request,"edit_classes.html",{"obj":obj})
    # elif request.method == "POST":
    #     nid = request.GET.get("nid")
    #     title = request.POST.get("XXOO")
    #     models.Classes.objects.filter(id = nid).update(title=title)
    #     return redirect("/classes.html")
    #上面一段为复制来的class信息
    if request.method == "GET":
        nid = request.GET.get("nid")
        obj = models.Student.objects.filter(id = nid).first()
        return render(request,"edit_students.html",locals())
    elif request.method == "POST":
        nid = request.GET.get("nid")
        username = request.POST.get("username")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        cs_id = request.POST.get("cs")
        models.Student.objects.filter(id = nid).update(username=username,age=age,gender=gender,cs=cs_id)
        return redirect("/get_students.html")


