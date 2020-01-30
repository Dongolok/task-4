from .apiviews import CourseList, CourseById
from django.urls import path

urlpatterns = [
    path('course/', CourseList.as_view()),
    path('course/<int:pk>/', CourseById.as_view())
]
