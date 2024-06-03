 
from django.contrib import admin
from .models import User
from django.shortcuts import redirect
from django.contrib import admin,messages
from core.models import Student, Doctor, Subject, Department, Level, Attendance,TimeTable
from datetime import date
from .admin_site import admin_site  # Import the custom admin site

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_student', 'is_doctor', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Roles', {'fields': ('is_student', 'is_doctor')}),
    )

admin_site.register(User, CustomUserAdmin)


# Register your models here.
admin_site.register(Student)
admin_site.register(Doctor)
admin_site.register(Subject)
admin_site.register(Department)
admin_site.register(Level)
admin_site.register(TimeTable)

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        
        if Attendance.objects.filter(student=obj.student, subject=obj.subject, date=date.today()).exists():
             
            messages.error(request, "Attendance for this student and subject has already been recorded today.")
        else:
            super().save_model(request, obj, form, change)