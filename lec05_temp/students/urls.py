from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.students_list, name='students_list'),
    path('teachers/', views.teachers_list, name='teachers_list'),
    path('thank-you/', views.thank_you_view, name='thank_you'),  # إضافة الفورم الجديد
]
