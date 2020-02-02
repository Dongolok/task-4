from django.test import TestCase, SimpleTestCase
from tables.models import Course, Category, Branch, Contact


class CourseModelTest(TestCase):
    @classmethod
    def setUp(cls):
        category_fk = Category.objects.create(name='FLEX', imgpath='some string')
        course_db = Course.objects.create(name='Something',
                                          logo='SomethingAsWell',
                                          description='description',
                                          category=category_fk
                                          )
        branch_fk = Branch.objects.create(latitude='12:18:19',
                                          longitude='13:19:20',
                                          address='some stupid address',
                                          branches=course_db)
        contact_fk = Contact.objects.create(value='Positive value',
                                            contacts=course_db)

    def test_category_name(self):
        category1 = Category.objects.get(id=1)
        max_length = category1._meta.get_field('name').max_length
        self.assertEquals(max_length, 120)

    def imgpath(self):
        img_path = Category.objects.get(id=1)
        max_length = img_path._meta.get_field('imgpath').max_length
        self.assertEquals(max_length, 120)

    def test_name(self):
        course1 = Course.objects.get(id=1)
        max_length = course1._meta.get_field('name').max_length
        self.assertEquals(max_length, 120)

    def test_logo(self):
        course1 = Course.objects.get(id=1)
        max_length = course1._meta.get_field('logo').max_length
        self.assertEquals(max_length, 120)

    def test_description(self):
        course1 = Course.objects.get(id=1)
        max_length = course1._meta.get_field('description').max_length
        self.assertEquals(max_length, 120)


