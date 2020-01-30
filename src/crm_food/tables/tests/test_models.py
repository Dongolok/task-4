from django.test import TestCase, SimpleTestCase
from tables.models import Course, Category


class CourseModelTest(TestCase):
    @classmethod
    def setUp(cls):
        cls.course1 = Course.objects.create(name='Something',
                                            logo='SomethingAsWell',
                                            description='description',
                                            )

    def test_name_logo_description(self, *args):
        a = self.course1.get('name')
        b = self.course1.get('logo')
        c = self.course1.get('description')
        self.assertEqual(a, 'Something')
        self.assertEqual(b, "SomeThingAsWell")
        self.assertEqual(c, 'description')

    def test_relationship_to_category(self):
        course1 = self.course1
        course1.save()
        category1 = Category(name='FLEX', course=course1)
        category1.save()
        self.assertEqual()
    #
    #     # assertion example ...
    #     record = Book.objects.get(id=1)
    #     self.assertEqual(record.author.name, "Mazuki Sekida")
    #
    #     self.assertEquals()
