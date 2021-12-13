from django.db import models
from django.core import validators
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Student (models.Model):
    YEAR_IN_SCHOOL = [
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
        ('GR', 'Graduate'),
        ]
    
    class meta :
        abstract = True
    
    studentId = models.PositiveIntegerField(blank=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    schoolyear = models.CharField(max_length=2, choices=YEAR_IN_SCHOOL)
    email = models.EmailField()
    date_created = models.DateTimeField(blank =True, auto_now_add=True)
    date_modified = models.DateTimeField(blank=True)
    
    def _str_ (self):
        return f'{super(Student, self)._str_()}- year:{self.schoolyear}'