from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Student URLs
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.student_create, name='student_create'),
    path('students/<int:student_id>/update/', views.student_update, name='student_update'),
    path('students/<int:student_id>/delete/', views.student_delete, name='student_delete'),
    path('students/<int:student_id>/', views.student_detail, name='student_detail'),
    
    # Faculty URLs
    path('faculty/', views.faculty_list, name='faculty_list'),
    path('faculty/add/', views.faculty_form, name='faculty_form'),
    path('faculty/<int:faculty_id>/', views.faculty_detail, name='faculty_detail'),

    # Department URLs
    path('departments/', views.department_list, name='department_list'),
    path('departments/add/', views.department_form, name='department_form'),
    path('departments/<int:department_id>/', views.department_detail, name='department_detail'),
    
    # Course URLs
    path('courses/', views.course_list, name='course_list'),
    path('courses/add/', views.course_form, name='course_form'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    
    # Enrollment URLs
    path('enrollments/', views.enrollment_list, name='enrollment_list'),
    path('enrollments/add/', views.enrollment_form, name='enrollment_form'),
    path('enrollments/<int:enrollment_id>/', views.enrollment_detail, name='enrollment_detail'),
    
]
