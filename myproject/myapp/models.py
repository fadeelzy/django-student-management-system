from django.db import models

# Create your models here.


class Student(models.Model):
    student_name = models.CharField(max_length=250)
    course_of_interest = models.CharField(max_length=250)
    course_duration = models.CharField(max_length=250)
    enrollment_fee = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    def __str__(self):
     return f" Name:{self.student_name} Course:{self.course_of_interest} course_duration:{self.course_duration} enrollment:{self.enrollment_fee} Date:{self.created_at}"


class Course(models.Model):
    name = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    fee = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
         return f" Name:{self.name} Duration:{self.duration} fee:{self.fee}"
    
    
    

