from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class AdminBackend(ModelBackend):
    def has_perm(self, user_obj, perm, obj=None):
        if user_obj.is_student or user_obj.is_doctor:
            return False
        return super().has_perm(user_obj, perm, obj)

    def authenticate(self, request, username=None, password=None, **kwargs):
        user = super().authenticate(request, username, password, **kwargs)
        if user is not None:
            if user.is_student or user.is_doctor:
                return None
        return user
