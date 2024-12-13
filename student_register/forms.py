import self
from django import forms
from django.forms.models import inlineformset_factory
from .models import Course, Exam, Registration

RegistrationFormSet = inlineformset_factory(Course,Registration,fields='__all__',extra=1)

class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = '__all__'

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'
        labels = {
            'student_name':'Student Name',
            'Reg_number':'Registration Number',
            'exam':'Exam',
            'course':'Course',
            'registration_date':'Registration Date',
        }

    def __init__(self,*args,**kwargs):
        super(RegistrationForm,self).__init__(*args,**kwargs)
        self.fields['exam'].empty.label='select'
        self.fields['course'].required ='False'


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


