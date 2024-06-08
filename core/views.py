from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from .models import Doctor, Student, Attendance, Subject, Level,TimeTable
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
# from django.db.models import Q
# from django.utils.timezone import localtime, now


@login_required
def home(request):
    if not request.user.is_student and not request.user.is_doctor:
        return redirect('/admin/')
    return render(request,'home.html',{})

@login_required
def lec_attendance(request, subject_id=None):
    if not request.user.is_doctor:
        return redirect('/')

    doctor = request.user.doctor_user

    if subject_id:
        subject = get_object_or_404(Subject, id=subject_id)
        students = Student.objects.filter(
            department=doctor.department,
            level__in=doctor.level.all(),
            subject=subject
        ).distinct()
        return render(request, 'attendance/lec_attendance.html', {'students': students, 'subject': subject})
    else:
        subjects = Subject.objects.filter(level__in=doctor.level.all())
        return render(request, 'attendance/lec_attendance.html', {'subjects': subjects})

@login_required
def submit_attendance(request, subject_id):
    if request.method == 'POST':
        subject = get_object_or_404(Subject, id=subject_id)
        student_ids = request.POST.getlist('student_ids')
        absent_students = []
        already_recorded = False

        for student_id in student_ids:
            attendance_status = request.POST.get(
                f'attendance_{student_id}', 'absent')
            student = get_object_or_404(Student, idc=student_id)

            if Attendance.objects.filter(student=student, subject=subject, date=date.today()).exists():
                already_recorded = True
                continue

            Attendance.objects.create(
                student=student,
                subject=subject,
                status=attendance_status == 'present'
            )

            if attendance_status == 'absent':
                absent_students.append(student.name)

        if already_recorded:
            messages.warning(
                request, 'Attendance for some students was already recorded today.')

        if absent_students:
            message = f'Number of absent students: {len(absent_students)}. Absent students: {", ".join(absent_students)}.'
            messages.success(request, message)
        else:
            messages.success(request, 'All students are marked present.')

        return HttpResponseRedirect(reverse('lec_attendance', args=[subject_id]))
    else:
        return redirect('subjects_by_level')


@login_required
def subjects_by_level(request):
    if not request.user.is_doctor:

        return redirect('/')
    doctor = request.user.doctor_user
    levels = doctor.level.all()
    subjects = Subject.objects.filter(level__in=levels, doctor_subject=doctor)

     
    subjects_by_level = {level: [
        subject for subject in subjects if subject.level == level] for level in levels}

    return render(request, 'subjects/subject_list.html', {'subjects_by_level': subjects_by_level})



 
 
# Student




@login_required
def view_attendance(request):
    student = request.user.student_user 
    subjects = student.subject.filter(level=student.level) 

    attendance_records = []
    dates_set = set()   

    for subject in subjects:
        records = Attendance.objects.filter(student=student, subject=subject).order_by('date')
        for record in records:
            dates_set.add(record.date)   

        attendance_summary = {
            'subject': subject.sname,
            'records': records,
            'present_count': records.filter(status=True).count(),
            'total': records.count()
        }
        attendance_records.append(attendance_summary)

    dates_list = sorted(list(dates_set))   

    return render(request, 'students/student_attendance.html', {
        'attendance_records': attendance_records,
        'dates_list': dates_list   
    })


### Time Table
@login_required
def user_timetable(request):
    timetable_image = None
     
    if hasattr(request.user, 'doctor_user'):
        doctor = get_object_or_404(Doctor, user=request.user)
        timetable_image = doctor.timeTableImage
 
    elif hasattr(request.user, 'student_user'):
       
        student = get_object_or_404(Student, user=request.user)
        timetable = get_object_or_404(TimeTable, level=student.level, department=student.department)
        timetable_image = timetable.Timage
        

    context = {
        'timetable_image': timetable_image,
    }
    return render(request, 'time_table.html', context)
