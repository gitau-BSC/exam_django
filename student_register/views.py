from django.shortcuts import render, get_object_or_404
from .models import Course,Exam,Registration
from .forms import RegistrationFormSet
# Create your views here.
def base(request):
    return render(request, '../templates/base.html')
def upload(request):
    return render(request,'upload.html')
def details(request):
    return render(request,'details.html')
def update(request):
    return render(request,'update.html')
def delete(request):
    return render(request,'delete.html')
def student_form(request):
    form = RegistrationFormSet()
    return render(request,'student_form.html',{'form':form})
