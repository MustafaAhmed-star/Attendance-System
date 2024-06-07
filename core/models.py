from django.db import models
from users.models import User
from django.utils import timezone


class Person(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,  related_name='%(class)s_user', null=True, blank=True)
    name = models.CharField(max_length=100)
    idc = models.IntegerField(primary_key=True)
    department = models.ForeignKey(
        'Department', related_name='%(class)s_department', on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Doctor(Person):
    subject = models.ManyToManyField('Subject', related_name='doctor_subject')
    level = models.ManyToManyField('Level', related_name='doctor_level')

    def __str__(self):
        return self.name


class Student(Person):
    level = models.ForeignKey(
        'Level', related_name='student_level', on_delete=models.CASCADE)
    subject = models.ManyToManyField('Subject', related_name='student_subject')

    def __str__(self):
        return self.name


class Subject(models.Model):
    sname = models.CharField(max_length=100)
    level = models.ForeignKey('Level', related_name='subject_level',
                              on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='subjects/', null=True, blank=True)

    def __str__(self):
        return self.sname


class Department(models.Model):
    dname = models.CharField(max_length=100)

    def __str__(self):
        return self.dname


class Level(models.Model):
    lname = models.CharField(max_length=100)

    def __str__(self):
        return self.lname
 
class Attendance(models.Model):
    student = models.ForeignKey('Student', related_name='attendance_student',
                                on_delete=models.CASCADE, null=True, blank=True)
    subject = models.ForeignKey('Subject', related_name='attendance_subject',
                                on_delete=models.CASCADE, null=True, blank=True)  # حقل جديد للمادة
    date = models.DateField(default=timezone.now)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.student} - {self.subject} - {self.date} - {self.status}'


 
class TimeTable(models.Model):
    Timage = models.ImageField(upload_to='time_table/', null=True, blank=True)
    level = models.ForeignKey('Level', on_delete=models.CASCADE,
                              related_name='timetables', null=True, blank=True)
    department = models.ForeignKey(
        'Department', on_delete=models.CASCADE, related_name='timetables', null=True, blank=True)

    def __str__(self):
        return f'{self.level.lname} - {self.department.dname}'
