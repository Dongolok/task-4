from django.test import TestCase
from django.urls import include, path, reverse
from rest_framework.test import APIClient
from tables.models import Course, Category, Branch, Contact
from tables import apiviews
from django.test import Client
from rest_framework import status
from tables.urls import CourseList
from rest_framework.test import APIRequestFactory


# class TestCourseList(APITestCase):
#     def test_create_account(self):
#         data = {'name': 'DabApps'}
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Account.objects.count(), 1)
#         self.assertEqual(Account.objects.get().name, 'DabApps')


class CourseViewsTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.category_fk = Category.objects.create(name='Bla bla bla', imgpath='some string')
        self.category_fk.save()
        self.course_1 = Course.objects.create(category=self.category_fk,
                                              name='Something',
                                              description='description',
                                              logo='SomethingAsWell',
                                              )
        self.course_1.save()
        self.contact_1 = Contact.objects.create(contact_by_choices=1, value='Some value', course=self.course_1)
        self.contact_1.save()
        self.branch_1 = Branch.objects.create(latitude='latitude', longitude='longitude', address='address', course=self.course_1)
        self.branch_1.save()

    def test_data(self):
        self.assertEqual(self.course_1.name, 'Something')
        self.assertEqual(self.course_1.logo, 'SomethingAsWell')
        self.assertEqual(self.course_1.description, 'description')
        self.assertEqual(self.course_1.category, self.category_fk)
        self.assertEqual(self.course_1.id, self.branch_1.course.id)
        self.assertEqual(self.course_1.id, self.contact_1.course.id)

    def test_get_ok(self):
        response = self.client.get('/course/')
        self.assertEqual(response.status_code, 200)

    def test_get_by_id_ok(self):
        response = self.client.get('/course/1/')
        self.assertEqual(response.status_code, 200)

    def test_get_by_id_not_ok(self):
        response = self.client.get('/course/2/')
        self.assertEqual(response.status_code, 404)

    def test_post_ok(self):
        data = {
            'category': 1,
            'name': 'FLEX',
            'description': 'gym place to build muscles',
            'logo': 'some text',
            'branch': [{'latitude': 'some string',
                        'longitude': 'some numbers',
                        'address': 'CIty of Heroes',
                        'course': 1
                        }],

            'contact': [{'contact_by_choices': 1,
                         'value': 'PHONE',
                         'course': 1
                         }]

        }
        response = self.client.post('/course/', data, format='json')

        self.assertEqual(response.status_code, 201)

    def test_get_by_id_not_ok(self):
        response = self.client.get('/course/100/')
        self.assertEqual(response.status_code, 404)