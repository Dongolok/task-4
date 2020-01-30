from rest_framework import serializers
from .models import Course, Branch, Contact, Category


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    branch = BranchSerializer(many=True)
    contact = ContactSerializer(many=True)

    class Meta:
        model = Course
        fields = '__all__'

    def create(self, validated_data):
        branches_data = validated_data.pop('branch')
        contacts_data = validated_data.pop('contact')
        course = Course.objects.create(**validated_data)
        Branch.objects.create(course=course, **branches_data)
        Contact.ojects.create(course=course, **contacts_data)
        return course


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
