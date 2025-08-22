from django.contrib import admin
from .models import Student, Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    """إعدادات admin للمعلمين"""
    list_display = ['name', 'email', 'subject', 'hire_date', 'active']
    list_filter = ['subject', 'active', 'hire_date']
    search_fields = ['name', 'email', 'subject']
    list_editable = ['active']
    ordering = ['name']
    date_hierarchy = 'hire_date'

    fieldsets = (
        ('المعلومات الأساسية', {
            'fields': ('name', 'email', 'phone')
        }),
        ('معلومات العمل', {
            'fields': ('subject', 'hire_date', 'active')
        }),
    )

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    """إعدادات admin للطلاب"""
    list_display = ['name', 'student_id', 'grade', 'email', 'enrollment_date', 'active']
    list_filter = ['grade', 'active', 'enrollment_date']
    search_fields = ['name', 'student_id', 'email']
    list_editable = ['active']
    ordering = ['name']
    date_hierarchy = 'enrollment_date'

    fieldsets = (
        ('المعلومات الأساسية', {
            'fields': ('name', 'student_id', 'email', 'phone')
        }),
        ('معلومات الدراسة', {
            'fields': ('grade', 'enrollment_date', 'active')
        }),
        ('معلومات إضافية', {
            'fields': ('birth_date',),
            'classes': ('collapse',)
        }),
    )
