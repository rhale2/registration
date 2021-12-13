from rest_framework import serilizers #piip install 
from .models import *

class StudentSerializer(serilizers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'fstname', 'lastname', 'idnumber', 'email', 'schoolyear', 'major', 'gpa', 'datacreated', 'datemodified')#needs more
        read_only_fields = ('datecreated', 'datemodified')

    def create(self, validated_data):
       return Student(**validated_data) #missing 