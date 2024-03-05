from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
    
    @property
    def is_student(self):
        return hasattr(self, 'student')
    @property
    def is_teacher(self):
        return hasattr(self, 'teacher')
