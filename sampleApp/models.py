from django.db import models

from teacher.models import Teacher

GENDER = (
    ('MALE', 'MALE'),
    ('FEMALE', 'FEMALE')
)

STUDENT_CLASS = (
    ('Basic 1', 'Basic 1'),
    ('Basic 2', 'Basic 2'),
    ('Basic 3', 'Basic 3'),
)


class Student(models.Model):
    student_id = models.CharField(max_length=5)
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6, choices=GENDER)
    student_class = models.CharField(max_length=7, choices=STUDENT_CLASS)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
