
from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/', views.home, name='dashboard'),

    path('students-list/', views.students_list, name='students_list'),
    path('members-list/', views.members_list, name='members_list'),
    path('courses-list/', views.courses_list, name='courses_list'),
    path('student/', views.student, name='student'),
    path('success/<int:student_id>/', views.registration_success, name='success'),
    path('members/', views.members, name='members'),
    path('members/success/<int:member_id>/', views.success_member, name='success_member'),
    path('course/', views.course, name='course'),
    path('revenue/', views.revenue, name='revenue'),
    path('settings/', views.settings, name='settings'),
    path('logout/', views.logout_view, name='logout'),
]