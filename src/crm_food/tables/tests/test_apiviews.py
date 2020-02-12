from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from tables.models import Course, Category, Branch, Contact
from tables import apiviews
from django.test import Client


# class TestCourseList(APITestCase):
#     def test_create_account(self):
#         data = {'name': 'DabApps'}
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Account.objects.count(), 1)
#         self.assertEqual(Account.objects.get().name, 'DabApps')


class CourseViewsTest(TestCase):
    def SetUp(self):
        self.client = Client()
        category_fk = Category.objects.create(name='Bla bla bla', imgpath='some string')
        course_1 = Course.objects.create(name='Something',
                                              logo='SomethingAsWell',
                                              description='description',
                                              category=category_fk,
                                              )
        contact_1 = Contact.objects.create(contact_by_choices=1, value='Some value', contacts=course_1)
        branch_1 = Branch.objects.create(latitude='latitude', longitude='longitude', address='address', branches=course_1)

    # def test_data(self):
    #     self.assertEqual(self.course_1.name, 'Something')
    #     self.assertEqual(self.course_1.logo, 'SomethingAsWell')
    #     self.assertEqual(self.course_1.description, 'description')
    #     self.assertEqual(self.course_1.category, self.category_fk)

    def test_get_ok(self):
        response = self.client.get('/course/')
        self.assertEqual(response.status_code, 200)

    def test_post_ok(self):
        response = self.client.post('/course/', {
                                                "category": 1,

                                                "name": "FLEX",

                                                "description": " gym place to build muscles",

                                                "logo": "some text",

                                                "branch": [{"latitude": "some string",
                                                            "longitude": "some numbers",
                                                            "address": "City of Heroes"}],


                                                "contact": [{"contact_by_choices": 1,
                                                             "contacts": "PHONE"}]

                                                })
        self.assertEqual(response.status_code, 201)

#
# {
#     "category": 1,
#     "name": "FLEX",
#     "description": " gym place to build muscles",
#     "logo": "some text",
#     "branch": [{"latitude": "some string",
#                 "longitude": "some numbers",
#                 "address": "CIty of Heroes"}],
#
#     "contact": [{"contact_by_choices": 1,
#                  "value": "PHONE"}]
#
# }