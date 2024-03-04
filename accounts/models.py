from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    @property
    def is_student(self):
        return hasattr(self, 'student')
    @property
    def is_teacher(self):
        return hasattr(self, 'teacher')
class User(AbstractUser):
    @property
    def is_student(self):
        if hasattr(self, 'student'):
            return True
        return False

    @property
    def is_teacher(self):
        if hasattr(self, 'teacher'):
            return True
        return False
