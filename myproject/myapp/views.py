from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Sum, Count
from .models import Student, Course, Enrollment, Member
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from io import BytesIO
import xhtml2pdf.pisa as pisa
from datetime import datetime
import calendar
from django.db.models.functions import TruncMonth
from django.db.models.functions import ExtractMonth

# Create your views here

def home(request):
    # --- Summary Cards ---
    total_students = Student.objects.count()
    total_courses = Course.objects.count()
    total_members  = Member.objects.count()
    total_student_revenue = Enrollment.objects.aggregate(total=Sum('fee'))['total'] or 0  
    total_member_revenue = Member.objects.aggregate(total=Sum('enrollment_fee'))['total'] or 0  
    total_revenue = total_student_revenue + total_member_revenue


    # --- Revenue per Month (Jan - Dec) ---
    monthly_revenue = (
        Enrollment.objects
        .annotate(month=ExtractMonth('created_at'))
        .values('month')
        .annotate(total=Sum('fee'))
        .order_by('month')
    )

    revenue_data = [0] * 12
    for entry in monthly_revenue:
        month_index = entry['month'] - 1  # Jan=0
        revenue_data[month_index] = float(entry['total'] or 0)

    context = {
        "total_students": total_students,
        "total_courses": total_courses,
        "total_members": total_members,
        "total_revenue": total_revenue,    
        "revenue_data": revenue_data,    
    }
    return render(request, "dashboard.html", context)


def students_list(request):
    students = Student.objects.all()
    return render(request, 'students_list.html', {'students': students})

def members_list(request):
    members = Member.objects.all()
    return render(request, 'members_list.html', {'members': members})

def courses_list(request):
    courses = Course.objects.all()
    return render(request, 'courses_list.html', {'courses': courses})

def student(request):
    if request.method == "POST":
        name = request.POST.get('studentName')
        course_id = request.POST.get('courseInterest')
        course_duration = request.POST.get('courseDuration')
        enrollment_fee = request.POST.get('enrollmentFee')

        course = get_object_or_404(Course, id=course_id)

        student_obj = Student.objects.create(
            student_name=name
        )
        Enrollment.objects.create(
            student=student_obj,
            course=course,
            duration=course_duration,
            fee=enrollment_fee
        )

        return redirect('success', student_id=student_obj.id)

    courses = Course.objects.all()
    return render(request, "student.html", {"courses": courses})

def registration_success(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":
        email = request.POST.get("email")

        # render HTML for receipt
        enrollment = student.enrollments.last() 
        html = render_to_string("receipt_template.html", {
            "student": student,
            "enrollment": enrollment
        })

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

def members(request):
    if request.method == "POST":
        member_name = request.POST.get('memberName')
        plan = request.POST.get('plan')
        duration = request.POST.get('duration')
        enrollment_fee = request.POST.get('enrollmentFee')

        # Create new Member object
        member_obj = Member.objects.create(
            member_name=member_name,
            plan=plan,
            duration=duration,
            enrollment_fee=enrollment_fee
        )

        return redirect('success_member', member_id=member_obj.id)

    return render(request, "member.html")

def success_member(request, member_id):
    member = get_object_or_404(Member, id=member_id)

    
    if request.method == "POST":
        email = request.POST.get("email")

        # render HTML for receipt
        enrollment = member.enrollment_fee
        html = render_to_string("receipt_member.html", {
            "member": member,
            "enrollment": enrollment
        })

        # convert to PDF
        result = BytesIO()
        pisa_status = pisa.CreatePDF(html, dest=result)

        if pisa_status.err:
            return render(request, "error.html", {"message": "Error generating PDF"})

        # email with PDF attachment
        mail = EmailMessage(
            subject="Your Membership Registration Receipt",
            body="Please find your receipt attached.",
            from_email=None,
            to=[email],
        )
        mail.attach(f"receipt_{member_id}.pdf", result.getvalue(), "application/pdf")
        mail.send()

        return render(request, "email_sent.html")

    return render(request, "success_member.html", {"member": member})

def course(request):
    return render(request, 'course.html')
    
def revenue(request): 
    # --- Revenue by Course ---
    revenue_by_course = (
    Enrollment.objects
    .values('course__name')
    .annotate(total=Sum('fee'))
)
    revenue_summary = {
        item['course__name']: float(item['total'] or 0)
        for item in revenue_by_course
}

    monthly_revenue = (
    Member.objects
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
        "monthly_member_revenue": monthly_revenue_data, 
        "total_revenue": total_revenue,
        "student_count": student_count,
        "course_count": course_count,
    }
    return render(request, "revenue.html", context)
   
   
def settings(request):
    return render(request, 'settings.html')

def logout(request):
    return render(request, 'logout.html')


