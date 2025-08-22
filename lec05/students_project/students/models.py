from django.db import models
from django.utils import timezone

class Teacher(models.Model):
    """نموذج المعلمين"""
    name = models.CharField('الاسم', max_length=100)
    email = models.EmailField('البريد الإلكتروني', unique=True)
    phone = models.CharField('رقم الهاتف', max_length=15, blank=True)
    subject = models.CharField('المادة', max_length=100)
    hire_date = models.DateField('تاريخ التوظيف', default=timezone.now)
    active = models.BooleanField('نشط', default=True)

    class Meta:
        verbose_name = 'معلم'
        verbose_name_plural = 'المعلمين'
        ordering = ['name']

    def __str__(self):
        return self.name

class Student(models.Model):
    """نموذج الطلاب"""
    GRADE_CHOICES = [
        ('1', 'الصف الأول'),
        ('2', 'الصف الثاني'), 
        ('3', 'الصف الثالث'),
        ('4', 'الصف الرابع'),
        ('5', 'الصف الخامس'),
        ('6', 'الصف السادس'),
        ('7', 'الصف السابع'),
        ('8', 'الصف الثامن'),
        ('9', 'الصف التاسع'),
        ('10', 'الصف العاشر'),
        ('11', 'الصف الحادي عشر'),
        ('12', 'الصف الثاني عشر'),
    ]

    name = models.CharField('الاسم', max_length=100)
    email = models.EmailField('البريد الإلكتروني', blank=True)
    phone = models.CharField('رقم الهاتف', max_length=15, blank=True)
    grade = models.CharField('الصف', max_length=2, choices=GRADE_CHOICES)
    student_id = models.CharField('رقم الطالب', max_length=20, unique=True)
    birth_date = models.DateField('تاريخ الميلاد', null=True, blank=True)
    enrollment_date = models.DateField('تاريخ التسجيل', default=timezone.now)
    active = models.BooleanField('نشط', default=True)

    class Meta:
        verbose_name = 'طالب'
        verbose_name_plural = 'الطلاب'
        ordering = ['name']

    def __str__(self):
        return f"{self.name} - {self.student_id}"
