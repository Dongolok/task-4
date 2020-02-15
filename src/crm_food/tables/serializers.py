from rest_framework import serializers
from .models import Course, Branch, Contact, Category


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['contact_by_choices', 'value']


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['latitude', 'longitude', 'address']


class CourseSerializer(serializers.ModelSerializer):
    branch = BranchSerializer(many=True)
    contact = ContactSerializer(many=True)

    class Meta:
        model = Course
        fields = ['id', 'category', 'name', 'description', 'logo', 'branch', 'contact']

    def create(self, validated_data):
        branches_data = validated_data.pop('branch')
        contacts_data = validated_data.pop('contact')
        courses = Course.objects.create(**validated_data)

        for branch_data in branches_data:
            lalapooza = Branch.objects.create(course=courses, **branch_data)
            lalapooza.save()

        for contact_data in contacts_data:
            danslapeau = Contact.objects.create(course=courses, **contact_data)
            danslapeau.save()

        return courses


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


