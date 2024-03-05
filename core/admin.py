from django.contrib import admin
from .models import Student, Doctor, Subject, Department, Level, Attendance
# Register your models here.
admin.site.register(Student)
admin.site.register(Doctor)
admin.site.register(Subject)
admin.site.register(Department)
admin.site.register(Level)
admin.site.register(Attendance)
