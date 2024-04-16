from django.shortcuts import render
from .models import Doctor, Student, Attendance, Subject, Level
from django.contrib.auth.decorators import login_required
from collections import defaultdict
from django.urls import reverse

from django.shortcuts import render, redirect
from .models import Doctor, Student
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

@login_required
def lec_attendance(request):
    if not request.user.is_doctor:
      
        return redirect('/')

  
    doctor = request.user.doctor_user 
    students = Student.objects.filter(department=doctor.department, level__in=doctor.level.all()).distinct()
    return render(request, 'attendance/tae.html', {'students': students})
    
    

@login_required
def submit_attendance(request):
    if request.method == 'POST':
        student_ids = request.POST.getlist('student_ids')
        print('<<<<<<<<<<<<<<<<<<<<<<<<<<')
        for student_id in student_ids:
            attendance_status = request.POST.get(f'attendance_{student_id}', 'absent') 
            student = Student.objects.get(idc=student_id)
            print('attttttttttttttttttttttttttttt')
            Attendance.objects.update_or_create(
                student=student,
                defaults={'status': attendance_status == 'present'}
            )
            print('doneeeeeeeeeeee')

        return HttpResponseRedirect(reverse('lec_attendance'))
    else:
       
        return HttpResponseRedirect(reverse('lec_attendance'))
        
        
        
@login_required
def subjects_by_level(request):
    if not request.user.is_doctor:
     
        return redirect('/')
    doctor = request.user.doctor_user 
    subjects = Subject.objects.filter(level__in=doctor.level.all())
    levels = doctor.level.all()

    # subjects_by_level = {}
    # for level in levels:
    #     subjects_for_level = subjects.filter(level=level)
    #     subjects_by_level[level] = subjects_for_level
    subjects_by_level = {level: [subject for subject in subjects if subject.level == level] for level in levels}

    return render(request, 'subjects/subject_list.html', {'subjects_by_level': subjects_by_level})