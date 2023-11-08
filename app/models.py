from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(max_length=200, default="Description")

    def __str__(self):
        return self.name




# class BlogPost(models.Model):
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     author = models.CharField(max_length=100)
#     pub_date = models.DateField()

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=100)
    publication_date = models.DateField()

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=100)
    company = models.CharField(max_length=100)

    def __str__(self):
        return self.author

class TeamMember(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    bio = models.TextField()
    image = models.ImageField(upload_to='team_images/')

    def __str__(self):
        return self.name

class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class ContactInfo(models.Model):
    address = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.email  # You can use any field as a representation