from django.shortcuts import render, redirect
from django.db.models import Count
from .models import Student, Teacher
from .forms import ThankYouForm  # استدعاء الفورم الجديد

def home(request):
    """الصفحة الرئيسية"""
    # إحصائيات عامة
    total_students = Student.objects.filter(active=True).count()
    total_teachers = Teacher.objects.filter(active=True).count()

    # إحصائيات الصفوف
    grades_stats = Student.objects.filter(active=True).values('grade').annotate(
        count=Count('id')
    ).order_by('grade')

    context = {
        'total_students': total_students,
        'total_teachers': total_teachers,
        'grades_stats': grades_stats,
    }
    return render(request, 'home.html', context)

def students_list(request):
    """صفحة قائمة الطلاب"""
    students = Student.objects.filter(active=True).order_by('name')

    # فلترة حسب الصف إذا كان موجود في الطلب
    grade_filter = request.GET.get('grade')
    if grade_filter:
        students = students.filter(grade=grade_filter)

    # إحصائيات
    total_students = students.count()
    grades = Student.GRADE_CHOICES

    context = {
        'students': students,
        'total_students': total_students,
        'grades': grades,
        'current_grade': grade_filter,
    }
    return render(request, 'students.html', context)

def teachers_list(request):
    """صفحة قائمة المعلمين"""
    teachers = Teacher.objects.filter(active=True).order_by('name')

    # فلترة حسب المادة إذا كان موجود في الطلب
    subject_filter = request.GET.get('subject')
    if subject_filter:
        teachers = teachers.filter(subject__icontains=subject_filter)

    # قائمة المواد المختلفة
    subjects = Teacher.objects.filter(active=True).values_list('subject', flat=True).distinct()

    context = {
        'teachers': teachers,
        'total_teachers': teachers.count(),
        'subjects': subjects,
        'current_subject': subject_filter,
    }
    return render(request, 'teachers.html', context)

# ===== الفورم الجديد =====
def thank_you_view(request):
    """نموذج الشكر للطلاب"""
    if request.method == 'POST':
        form = ThankYouForm(request.POST)
        if form.is_valid():
            # التعامل مع البيانات، مثلا الطباعة أو إرسال بريد
            print(form.cleaned_data)
            return redirect('students:home')  # إعادة التوجيه للصفحة الرئيسية بعد الإرسال
    else:
        form = ThankYouForm()
    return render(request, 'thank_you.html', {'form': form})
