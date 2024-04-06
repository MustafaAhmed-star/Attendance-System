from django.shortcuts import render
from .models import Doctor, Student, Attendance
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from .models import Doctor, Student
from django.contrib.auth.decorators import login_required

@login_required
def lec_attendance(request):
    if not request.user.is_doctor:
        # إذا لم يكن المستخدم طبيبًا، يمكنك إعادة توجيهه إلى صفحة أخرى أو عرض رسالة خطأ
        return redirect('some_other_view')

    # إذا كان المستخدم طبيبًا، استمر في المعالجة
    doctor = request.user.doctor_user  # افتراض وجود علاقة OneToOne بين User و Doctor
    students = Student.objects.filter(department=doctor.department, level__in=doctor.level.all()).distinct()
    return render(request, 'attendance/lec_attendance.html', {'students': students})
    
    
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required
def submit_attendance(request):
    if request.method == 'POST':
        student_ids = request.POST.getlist('student_ids')
        for student_id in student_ids:
            attendance_status = request.POST.get(f'attendance_{student_id}', 'absent')  # القيمة الافتراضية هي 'absent'
            student = Student.objects.get(idc=student_id)
            # إنشاء أو تحديث سجل الحضور
            Attendance.objects.update_or_create(
                student=student,
                defaults={'status': attendance_status == 'present'}
            )
        return HttpResponseRedirect(reverse('lec_attendance'))
    else:
        # إعادة توجيه إلى صفحة الحضور في حالة عدم إرسال النموذج بطريقة POST
        return HttpResponseRedirect(reverse('lec_attendance'))