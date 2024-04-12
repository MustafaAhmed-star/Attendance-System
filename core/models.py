from django.db import models
from users.models import User
class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,  related_name='%(class)s_user',null = True , blank=True)
    name = models.CharField(max_length=100)
    idc = models.IntegerField(primary_key=True)
    department = models.ForeignKey('Department', related_name='%(class)s_department', on_delete=models.CASCADE)
    class Meta:
        abstract = True
class Doctor(Person):
    subject = models.ManyToManyField('Subject', related_name='doctor_subject')
    level = models.ManyToManyField('Level', related_name='doctor_level')
    
    def __str__(self):
        return self.name
class Student(Person):
    level = models.ForeignKey('Level', related_name='student_level', on_delete=models.CASCADE)
    subject = models.ManyToManyField('Subject', related_name='student_subject')
    
    def __str__(self):
        return self.name
class Subject(models.Model):
    sname = models.CharField(max_length=100)
    level = models.ForeignKey('Level', related_name='subject_level', on_delete=models.CASCADE,null=True,blank=True)

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
# class Attendance(models.Model):
#     student = models.ForeignKey('Student', related_name='attendance_student', on_delete=models.CASCADE)
#     date = models.DateField(auto_now_add=True)
#     status = models.BooleanField(default=False)
    
#     def __str__(self):
#         return f'{self.student} - {self.date} - {self.status}'
   
class Attendance(models.Model):
    student = models.ForeignKey('Student', related_name='attendance_student', on_delete=models.CASCADE,null=True, blank=True)
    subject = models.ForeignKey('Subject', related_name='attendance_subject', on_delete=models.CASCADE,null=True, blank=True)  # حقل جديد للمادة
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.student} - {self.subject} - {self.date} - {self.status}'
        
        
# class Session(models.Model):
#     title = models.CharField(max_length=100)
#     start_date = models.DateField()
#     end_date = models.DateField()
#     subjects = models.ManyToManyField('Subject', related_name='sessions')

#     def __str__(self):
#         return self.title