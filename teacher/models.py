from django.db import models

GENDER = (
    ('MALE', 'MALE'),
    ('FEMALE', 'FEMALE')
)

STUDENT_CLASS = (
    ('Basic 1', 'Basic 1'),
    ('Basic 2', 'Basic 2'),
    ('Basic 3', 'Basic 3'),
)


class Teacher(models.Model):
    teacher_id = models.CharField(max_length=4)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6, choices=GENDER)
    teacher_class = models.CharField(max_length=7, choices=STUDENT_CLASS)

    def __str__(self):
        return self.first_name + " " + self.last_name
