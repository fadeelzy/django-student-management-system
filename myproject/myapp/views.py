from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Sum, Count
from .models import Student, Course
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from io import BytesIO
from datetime import datetime
import calendar
from django.db.models.functions import TruncMonth
from django.db.models.functions import ExtractMonth

# Create your views here

def home(request):
    # --- Summary Cards ---
    total_students = Student.objects.count()
    total_courses = 5
    total_revenue = Student.objects.aggregate(total=Sum('enrollment_fee'))['total'] or 0

    # --- Active vs Inactive Students ---
    students_by_status = (
        Student.objects
        .values('status')
        .annotate(total=Count('id'))
    )
    student_data = {
        item['status']: item['total']
        for item in students_by_status
    }

    # --- Revenue per Month (Jan - Dec) ---
    monthly_revenue = (
        Student.objects
        .annotate(month=ExtractMonth('created_at'))
        .values('month')
        .annotate(total=Sum('enrollment_fee'))
        .order_by('month')
    )

    revenue_data = [0] * 12
    for entry in monthly_revenue:
        month_index = entry['month'] - 1  # Jan=0
        revenue_data[month_index] = float(entry['total'] or 0)

    context = {
        "total_students": total_students,
        "total_courses": total_courses,
        "total_revenue": total_revenue,
        "student_data": student_data,      
        "revenue_data": revenue_data,    
    }
    return render(request, "dashboard.html", context)


def student(request):
    if request.method == "POST":
        name = request.POST.get('studentName')
        course_of_interest = request.POST.get('courseInterest')
        course_duration = request.POST.get('courseDuration')
        enrollment_fee = request.POST.get('enrollmentFee')

        student_obj = Student.objects.create(
            student_name=name,
            course_of_interest=course_of_interest,
            course_duration=course_duration,
            enrollment_fee=enrollment_fee
        )

        return redirect('success', student_id=student_obj.id)
    
    return render(request, 'student.html')

def registration_success(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":
        email = request.POST.get("email")

        # render HTML for receipt
        html = render_to_string("receipt_template.html", {"student": student})

        # convert to PDF
        result = BytesIO()
        pisa_status = pisa.CreatePDF(html, dest=result)

        if pisa_status.err:
            return render(request, "error.html", {"message": "Error generating PDF"})

        # email with PDF attachment
        mail = EmailMessage(
            subject="Your Course Registration Receipt",
            body="Please find your receipt attached.",
            from_email=None,
            to=[email],
        )
        mail.attach(f"receipt_{student.id}.pdf", result.getvalue(), "application/pdf")
        mail.send()

        return render(request, "email_sent.html")

    return render(request, "success.html", {"student": student})

def course(request):
    return render(request, 'course.html')
    
def revenue(request): 
    # --- Revenue by Course ---
    revenue_by_course = (
        Student.objects
        .values('course_of_interest')
        .annotate(total=Sum('enrollment_fee'))
    )
    revenue_summary = {
        item['course_of_interest']: float(item['total'] or 0)
        for item in revenue_by_course
    }

    # --- Monthly Revenue Trend ---
    monthly_revenue = (
        Student.objects
        .annotate(month=TruncMonth('created_at'))
        .values('month')
        .annotate(total=Sum('enrollment_fee'))
        .order_by('month')
    )
    monthly_revenue_data = {
    item['month'].strftime("%b %Y"): float(item['total'] or 0)
    for item in monthly_revenue if item['month']
}

    # --- Summary Cards ---
    total_revenue = sum(revenue_summary.values())
    student_count = Student.objects.count()
    course_count = Course.objects.count()

    context = {
        "revenue_summary": revenue_summary,
        "monthly_revenue": monthly_revenue_data,
        "total_revenue": total_revenue,
        "student_count": student_count,
        "course_count": course_count,
    }
    return render(request, "revenue.html", context)
   
   
def settings(request):
    return render(request, 'settings.html')

def logout(request):
    return render(request, 'logout.html')


