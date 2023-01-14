from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .models import Student
# Serializers define the API representation.
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields =  '__all__'