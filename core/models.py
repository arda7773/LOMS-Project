from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ('ADMIN', 'Administrator'),
        ('FACULTY', 'Faculty Member'),
        ('LECTURER', 'Lecturer'),
        ('STUDENT', 'Student'),
    ]

    role = models.CharField(max_length=30, choices=ROLE_CHOICES)

    # groups & user_permissions çakışma engelleme
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
    )

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"



class Program(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=50, unique=True)
    faculty_manager = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        limit_choices_to={'role': 'FACULTY'}
    )

    def __str__(self):
        return self.name


class Course(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    credit = models.IntegerField()
    year = models.IntegerField()
    semester = models.IntegerField()

    def __str__(self):
        return f"{self.code} - {self.name}"


class ProgramOutcome(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return f"PO{self.order} ({self.program.code})"


class CourseLearningOutcome(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return f"LO{self.order} ({self.course.code})"


class LOToPOMap(models.Model):
    lo = models.ForeignKey(CourseLearningOutcome, on_delete=models.CASCADE)
    po = models.ForeignKey(ProgramOutcome, on_delete=models.CASCADE)


class Syllabus(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE)
    file = models.FileField(upload_to="syllabus/")
    uploaded_at = models.DateTimeField(auto_now=True)


class TeachingAssignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lecturer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'LECTURER'}
    )


class Enrollment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'STUDENT'}
    )
