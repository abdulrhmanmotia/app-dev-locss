# students/forms.py
from django import forms

class ThankYouForm(forms.Form):
    student_name = forms.CharField(label='اسم الطالب', max_length=100)
    email = forms.EmailField(label='البريد الإلكتروني')
    message = forms.CharField(label='الرسالة', widget=forms.Textarea)
