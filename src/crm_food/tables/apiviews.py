from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Course, Branch, Contact, Category
from .serializers import CourseSerializer, BranchSerializer, ContactSerializer, CategorySerializer

'''GET should retrieve all the courses in database (model: Course)
POST should add a course into DB (model: Course)'''

from rest_framework import generics


class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseById(generics.RetrieveDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


# class CourseById(APIView):
#     def get(self, request):
#         courses = Course.objects.all()
#         data = CourseSerializer(courses, many=True).data
#         return Response(data)
#
#
# class CourseAdd(APIView):
#     def post(self, request):
#         course = Course.objects.all()
#         data = CourseSerializer(course).data
#         if data.is_valid():
#             data.save()
