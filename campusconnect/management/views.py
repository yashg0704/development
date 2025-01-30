from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Student, Faculty, Department, Course, Enrollment
from .forms import StudentForm, FacultyForm, DepartmentForm, CourseForm, EnrollmentForm

# Home View
def home(request):
    return render(request, 'management/home.html')

# Student Views
def student_list(request):
    students = Student.objects.all()
    return render(request, 'management/student_list.html', {'students': students})

def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'management/student_detail.html', {'student': student})

def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully!")
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'management/form_template.html', {'form': form, 'title': 'Add Student'})

def student_update(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully!")
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'management/form_template.html', {'form': form, 'title': 'Edit Student'})

def student_delete(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == "POST":
        student.delete()
        messages.success(request, "Student deleted successfully!")
        return redirect('student_list')
    return render(request, 'management/student_confirm_delete.html', {'student': student})

# Faculty Views
def faculty_form(request):
    if request.method == "POST":
        form = FacultyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Faculty member added successfully!")
            return redirect('faculty_list')
    else:
        form = FacultyForm()
    return render(request, 'management/form_template.html', {'form': form, 'title': 'Add Faculty'})

def faculty_list(request):
    faculties = Faculty.objects.all()
    print(f"Faculty count: {faculties.count()}")  # Add this for debugging
    return render(request, 'management/faculty_list.html', {'faculties': faculties})

def faculty_detail(request, faculty_id):
    faculty = get_object_or_404(Faculty, id=faculty_id)
    return render(request, 'management/faculty_detail.html', {'faculty': faculty})

# Department Views
def department_form(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Department added successfully!")
            return redirect('department_list')
    else:
        form = DepartmentForm()
    return render(request, 'management/form_template.html', {'form': form, 'title': 'Add Department'})

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'management/department_list.html', {'departments': departments})

def department_detail(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    return render(request, 'management/department_detail.html', {'department': department})

# Course Views
def course_form(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Course added successfully!")
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'management/form_template.html', {'form': form, 'title': 'Add Course'})

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'management/course_list.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'management/course_detail.html', {'course': course})

# Enrollment Views
def enrollment_form(request):
    if request.method == "POST":
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Enrollment completed successfully!")
            return redirect('enrollment_list')
    else:
        form = EnrollmentForm()
    return render(request, 'management/form_template.html', {'form': form, 'title': 'Enroll Student'})

def enrollment_list(request):
    enrollments = Enrollment.objects.all()
    return render(request, 'management/enrollment_list.html', {'enrollments': enrollments})

def enrollment_detail(request, enrollment_id):
    enrollment = get_object_or_404(Enrollment, id=enrollment_id)
    return render(request, 'management/enrollment_detail.html', {'enrollment': enrollment})
