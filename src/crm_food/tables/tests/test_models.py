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


class BranchModelTest(TestCase):
    @classmethod
    def setUp(cls):
        category_fk = Category.objects.create(name='Bla bla bla', imgpath='some string')
        course_1 = Course.objects.create(name='Something',
                                         logo='SomethingAsWell',
                                         description='description',
                                         category=category_fk,
                                         )
        branch_1 = Branch.objects.create(latitude='latitude', longitude='longitude', address='address', branches=course_1)

    def test_latitude(self):
        branch1 = Branch.objects.get(id=1)
        max_length = branch1._meta.get_field('latitude').max_length
        self.assertEquals(max_length, 120)

    def test_longitude(self):
        branch1 = Branch.objects.get(id=1)
        max_length = branch1._meta.get_field('longitude').max_length
        self.assertEquals(max_length, 120)

    def test_address(self):
        branch1 = Branch.objects.get(id=1)
        self.assertTrue('address' in branch1.address)



