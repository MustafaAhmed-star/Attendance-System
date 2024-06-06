from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_student = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    
   
    
    
    
    

class Feedback(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedbacks')
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.subject}"
