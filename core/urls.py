
from django.urls import path



from .views import record_attendance



urlpatterns = [
    #  path('',show_record),
     path('record_attendance/', record_attendance, name='record_attendance'),

]