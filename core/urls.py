
from django.urls import path
from . import views
urlpatterns = [
#     path('students/<int:subject_id>/', views.student_list, name='student-list'),
#     path('attendance/add/', views.AttendanceCreateView.as_view(), name='add-attendance'),
path('lec_attendance/<int:subject_id>', views.lec_attendance, name='lec_attendance'),
path('submit_attendance/<int:subject_id>', views.submit_attendance, name='submit_attendance'),
path('subjects/', views.subjects_by_level, name='subjects_by_level'),
path('view_attendance/', views.view_attendance, name='view_attendance'),
#---------------------------------------------

]   
