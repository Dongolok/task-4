from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=120)
    imgpath = models.CharField(default='Imagine path', max_length=120)

    def __str__(self):
        return self.name


class Course(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=120)
    logo = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Branch(models.Model):
    latitude = models.CharField(max_length=120)
    longitude = models.CharField(max_length=120)
    address = models.TextField(blank=False, null=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='branch')  # ForeignKey is not one-to-many, but many-to-one relationship

    def __str__(self):
        return self.address


class Contact(models.Model):
    CONTACT_CHOICES = [(1, 'PHONE'),
                       (2, 'FACEBOOK'),
                       (3, 'EMAIL')]
    contact_by_choices = models.IntegerField(choices=CONTACT_CHOICES)
    value = models.CharField(max_length=100, default='')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='contact')

    def __str__(self):
        return self.value
