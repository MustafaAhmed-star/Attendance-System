from django.contrib import admin,messages
from .models import Student, Doctor, Subject, Department, Level, Attendance
from datetime import date

# Register your models here.
admin.site.register(Student)
admin.site.register(Doctor)
admin.site.register(Subject)
admin.site.register(Department)
admin.site.register(Level)
admin.site.register(Attendance)

# @admin.register(Attendance)
# class AttendanceAdmin(admin.ModelAdmin):
    # def save_model(self, request, obj, form, change):
        
    #     if Attendance.objects.filter(student=obj.student, subject=obj.subject, date=date.today()).exists():
             
    #         messages.error(request, "Attendance for this student and subject has already been recorded today.")
    #     else:
    #         super().save_model(request, obj, form, change)