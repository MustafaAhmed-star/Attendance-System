from django.contrib import admin, messages
from .models import User
from django.contrib.auth.hashers import make_password
from core.models import Student, Doctor, Subject, Department, Level, Attendance, TimeTable
from datetime import date
from .admin_site import admin_site  # Import the custom admin site

class StudentFilter(admin.SimpleListFilter):
    title = 'student'
    parameter_name = 'student'

    def lookups(self, request, model_admin):
        students = set([a.student for a in Attendance.objects.all()])
        return [(s.idc, s.name) for s in students]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(student__idc=self.value())
        return queryset

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_student', 'is_doctor', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Roles', {'fields': ('is_student', 'is_doctor')}),
    )
    def save_model(self, request, obj, form, change):
        if 'password' in form.changed_data:
            obj.password = make_password(obj.password)
        super().save_model(request, obj, form, change)
admin_site.register(User, CustomUserAdmin)

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'date', 'status', 'count_attendance')
    list_filter = (StudentFilter, 'subject', 'date', 'status')
    search_fields = ('student__name', 'subject__sname')
    
    def save_model(self, request, obj, form, change):
        if Attendance.objects.filter(student=obj.student, subject=obj.subject, date=date.today()).exists():
            messages.error(request, "Attendance for this student and subject has already been recorded today.")
        else:
            super().save_model(request, obj, form, change)

    def count_attendance(self, obj):
        return Attendance.objects.filter(student=obj.student, subject=obj.subject,status = True).count()
    count_attendance.short_description = 'Total Attendance for Subject'

# Register your models here.
admin_site.register(Student)
admin_site.register(Doctor)
admin_site.register(Subject)
admin_site.register(Department)
admin_site.register(Level)
admin_site.register(TimeTable)
admin_site.register(Attendance, AttendanceAdmin)  # Register Attendance with AttendanceAdmin
