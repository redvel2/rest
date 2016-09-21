from __future__ import unicode_literals

from django.db import models



class Author(models.Model):

    name = models.CharField(max_length=200)
    age = models.IntegerField()
    country = models.CharField(max_length=50)

    def __str__(self):
        return "Author: {name}".format(**{"name":self.name})


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    short_description = models.TextField(max_length=200, default="")
    code = models.CharField(max_length=50)

    def __str__(self):
        return "Publisher <{name}> id:{id}".format(**{"name":self.name, "id":self.id})


class Book(models.Model):
    author = models.ForeignKey(Author, related_name="books")
    publishers = models.ManyToManyField(Publisher, related_name="books")
    release_date = models.DateField()
    barcode = models.CharField(max_length=100)
    title = models.CharField(max_length=250)
    short_description = models.TextField(max_length=500)
    long_description = models.TextField(max_length=1500)

    def __str__(self):
        return "Book <{title}> id:{id}".format(**{"title":self.title, "id":self.id})
