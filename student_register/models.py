from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.code})"
class Exam(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='exams')
    title = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title} - {self.course.name} on {self.date}"

class Registration(models.Model):
    student_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registrations')
    Reg_number = models.CharField(max_length=100, default='DEFAULT_VALUE')
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='registrations')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(default=now)

    class Meta:
        unique_together = ('student_name', 'exam','course','registration_date')

    def __str__(self):
        return f"{self.student_name.username} registered for {self.exam.title}"
