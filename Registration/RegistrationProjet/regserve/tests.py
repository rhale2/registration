from django.test import TestCase
from django.test.client import Client
from .models import *
import io
from rest_framework.parsers import JSONParser

class DataTest (TestCase): 
    def setUp(self):
        student1 = Student.object.create(
            fristname = "First",
            lastname = "Studnet",
            emailaddreess = "first@student.edu",
            schoolyear = "FB",
            major = "CS",
            gpa = 4.0,
        )
        student2 = Student.object.create(
            fristname = "Second",
            lastname = "Studnet",
            emailaddreess = "second@student.edu",
            schoolyear = "SR",
            major = "ENG",
            gpa = 2.0,
        )
        self.test_client = Client()

    def test_student_api (self):
        students_response = self.test_client.get('/regserve/data/students')
        print(f'TEST_STUDENT_API: Api response content is: {students_response} and the status is {students_response.status_code}')
        self.assertEqual(students_response.status_code, 200)
        print(f'TEST_STUDENT_API: api response content is: {students_response.content}')
        student_stream = io.BytesIO(students_response.content)
        print(f'TEST_STUDENT_API: api response stream is: {student_stream}')
        student_data = JSONParser().parse(student_stream)
        print(f'TEST_STUDENT_API: api response data is: {student_data[0]} and its id is {student_data[id]}') 
        first_student_db = Student.objects.get(id=student_data['id'])
        print(f'TEST_STUDENT_API: api response student object from db is: {students_response.content}')
        first_student_serializer = StudentSerilaizer(first_student_db, data=student_data[0])
        first_student_data = student_data[0]

        first_student_api = first_student_serializer.save()
        self.assertEqual(first_student_db, first_student_api)

    def test_student (self):
        student_list = Student.objects.all()
        for student in student_list:
            self.assertEqual(student.id, 1)
            self.assertEqual(student.full_name, 'First Studnet')
            self.assertEqual(student.idNumber, 100)
    
# Create your tests here.
class SimpleTest(TestCase):
    def setUp(self):
        self.test_client = Client()
        
    def test_response(self):
        response = self.test_client.get('/regserve', {}, True)
        print(f'In simple test, response is {response}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'Hello world from django backend')