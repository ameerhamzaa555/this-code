from django.shortcuts import render
from .models import student
from .serializers import studentSerializer
from django.http import JsonResponse

def info(request):
    stu = student.objects.all()
    serializer= studentSerializer(stu,many=True)
    return JsonResponse(serializer.data,safe=False)

def infoo(request,id):
    stu = student.objects.get(pk=id)
    serializer= studentSerializer(stu,many=False)
    return JsonResponse(serializer.data,safe=True)