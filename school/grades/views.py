from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets, mixins

from .models import Student
from .serializers import StudentSerializer


#class StudentViewSet(viewsets.ModelViewSet):
class StudentViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# def grades(request):
#     if request.method == 'GET':
#         student = Student.objects.first()
#         serializer = StudentSerializer(student)
#         return JsonResponse(serializer.data)
