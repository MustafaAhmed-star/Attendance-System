from django.contrib.admin import AdminSite
from django.shortcuts import redirect

class MyAdminSite(AdminSite):
    def has_permission(self, request):
        return request.user.is_active and request.user.is_staff and not (request.user.is_student or request.user.is_doctor)

    def login(self, request, extra_context=None):
        if request.user.is_authenticated:
            if not self.has_permission(request):
                return redirect('/')
        return super().login(request, extra_context)

admin_site = MyAdminSite(name='myadmin')
