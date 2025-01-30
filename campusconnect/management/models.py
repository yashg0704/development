from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    head = models.ForeignKey('Faculty', on_delete=models.SET_NULL, null=True , related_name='headed_departments')

    def __str__(self):
        return self.name

class Faculty(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    hire_date = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    enrollment_date = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Course(models.Model):
    code = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    credits = models.IntegerField()
    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField()

    class Meta:
        unique_together = ('student', 'course')

    def __str__(self):
        return f'{self.student} enrolled in {self.course}'
