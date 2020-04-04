from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import json
from student.models import Student, Grade


# Create your views here.

def student_list(request):
    return render(request, "student.html")


def get_student(request):
    student_list = Student.objects.all().order_by('id')
    rows = request.GET.get('rows')
    page = request.GET.get('page', 1)
    pagtor = Paginator(student_list, per_page=rows)  # 分页器对象
    xxx = list(pagtor.page_range)
    if int(page) not in xxx:
        page = 1
    all_page = Paginator(student_list, rows)
    # 获取分页后第一页的对象
    page_obj = Paginator(student_list, rows).page(page).object_list
    page_data = {
        "page": page,
        "total": all_page.num_pages,
        "records": all_page.count,
        "rows": list(page_obj)
    }

    # 对象序列化
    def myDefault(s):
        if isinstance(s, Student):
            if s.sex == False:
                s.sex = "女"
            else:
                s.sex = "男"
            return {"id": s.pk,
                    "name": s.name,
                    "age": s.age,
                    "sex": s.sex,
                    "group": s.group,
                    "grade": s.grade_id.Grade_name}

    data = json.dumps(page_data, default=myDefault)
    return HttpResponse(data)


def get_grade(request):
    values_list = Grade.objects.all().values_list('Grade_name', flat=True)
    select = "<select>"
    for i in values_list:
        html_con = "<option>{}</option>".format(i)
        select += html_con
    select += "</select>"
    return HttpResponse(select)


@csrf_exempt  # 解决csrf
def edit_student(request):
    option = request.POST.get("oper")
    if option == "add":
        name = request.POST.get('name')
        age = request.POST.get('age')
        sex = request.POST.get('sex')
        if sex == "男":
            sex = True
        else:
            sex = False
        group = request.POST.get('group')
        grade = request.POST.get('grade')
        grade_obj = Grade.objects.all().get(Grade_name=grade)
        # 将获取到的表单数据保存到数据库
        Student.objects.create(name=name, age=age, sex=sex, group=group, grade_id=grade_obj)
    elif option == "edit":
        student_id = request.POST.get("id")
        name = request.POST.get('name')
        age = request.POST.get('age')
        sex = request.POST.get('sex')
        if sex == "男":
            sex = True
        else:
            sex = False
        group = request.POST.get('group')
        grade = request.POST.get('grade')
        grade_obj = Grade.objects.all().get(Grade_name=grade)
        # 将获取到的表单数据修改并保存到数据库
        student = Student.objects.get(pk=student_id)
        student.name = name
        student.age = age
        student.sex = sex
        student.group = group
        student.grade_id = grade_obj
        student.save()
    elif option == "del":
        student_id = request.POST.get("id")
        Student.objects.get(pk=student_id).delete()
    return HttpResponse("success")
