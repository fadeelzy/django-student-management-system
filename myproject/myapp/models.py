from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):  
    student_name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.student_name


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="enrollments")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="enrollments")
    duration = models.CharField(max_length=50) 
    fee = models.DecimalField(max_digits=10, decimal_places=2,  null=True, blank=True)  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.student_name} → {self.course.name}  →  {self.duration} → {self.fee}"

    
class Member(models.Model):
    PLAN_CHOICES = [
        ("Basic", "Basic Plan"),
        ("Premium", "Premium Plan"),
    ]

    member_name = models.CharField(max_length=250)
    plan = models.CharField(max_length=50, choices=PLAN_CHOICES)
    duration = models.CharField(max_length=50, blank=True, null=True)
    enrollment_fee = models.DecimalField(max_digits=10, decimal_places=2,  null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.member_name}  →  ({self.plan}  →  {self.duration} → {self.enrollment_fee})"