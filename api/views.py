
from django.urls import path
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import *
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema

@csrf_exempt
@api_view(['GET'])
def student_list(request):
    if request.method == 'GET':
        student = Student.objects.all()
        serializers = StudentSerializer(student,many=True)
        return JsonResponse(serializers.data, safe=False)
        

@swagger_auto_schema(method='POST', request_body=StudentSerializer)
@api_view(['POST'])
def create_student(request):
    if request.method == 'POST':
        serializers = StudentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return JsonResponse(serializers.data, status=201)
        return JsonResponse(serializers.errors, status=400)


@swagger_auto_schema(method='PUT', request_body=StudentSerializer)
@api_view(['PUT'])
def update_student(request,pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'PUT':
        serializers = StudentSerializer(student,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return JsonResponse(serializers.data)
        return JsonResponse(serializers.errors, status=400)
    
    

@api_view(['DELETE'])
def delete_student(request,pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'DELETE':
        student.delete()
        return HttpResponse('Deleted Successfully')