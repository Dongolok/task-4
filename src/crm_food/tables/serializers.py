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
        fields = ['id', 'category', 'name', 'description', 'logo', 'branch', 'contact']

    def create(self, validated_data):
        branches_data = validated_data.pop('branch')
        contacts_data = validated_data.pop('contact')
        course_1 = Course.objects.create(**validated_data)
        for branch_data in branches_data:
            Branch.objects.create(course=course_1, **branch_data)
        Contact.objects.create(course=course_1, **contacts_data)
        return course_1


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
