
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='dashboard'),
    path('student/', views.student, name='student'),
    path('course/', views.course, name='course'),
    path('revenue/', views.revenue, name='revenue'),
    path('settings/', views.settings, name='settings'),
    path('logout/', views.logout, name='logout'),
    path('success/<int:student_id>/', views.registration_success, name='success'),

]
