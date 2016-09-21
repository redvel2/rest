from rest_framework import serializers

from .models import (
    Book,
    Author,
    Publisher
)

class AuthorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Author
        # exclude = ("age",)

class PublisherSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Publisher

class BookSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Book
