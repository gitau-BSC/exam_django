from django.urls import path
from .import views

urlpatterns = [
    path('',views.base,name='index'),
    path('upload/',views.upload,name='upload'),
    path('details/',views.details,name='details'),
    path('update/',views.update,name='update'),
    path('delete/',views.delete,name='delete'),
    path('student_form/',views.student_form,name='student_form'),

]