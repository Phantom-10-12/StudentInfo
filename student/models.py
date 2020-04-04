from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    sex = models.BooleanField()
    group = models.IntegerField(blank=True, null=True)  # 组别
    grade_id = models.ForeignKey(to="Grade", null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        db_table = "t_student"

    def __str__(self):
        return self.name


class Grade(models.Model):
    Grade_name = models.CharField(max_length=40)
