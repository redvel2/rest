from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated


from .serializers import AuthorSerializer, PublisherSerializer, BookSerializer
from .models import Author, Publisher, Book


class AuthorView(ModelViewSet):
    """
    Book authors
    """
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = (IsAuthenticated,)


class PublisherView(ModelViewSet):
    """
    Publishers
    """
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()
    permission_classes = (IsAuthenticated,)


class BookView(ModelViewSet):
    """
    Books
    """
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = (IsAuthenticated,)