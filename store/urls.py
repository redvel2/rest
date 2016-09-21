from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import AuthorView, PublisherView, BookView



router = DefaultRouter()
router.register("authors", AuthorView)
router.register("books", BookView)
router.register("publishers", PublisherView)


urlpatterns = [url("^", include(router.urls)),
               url("^api-auth/", include('rest_framework.urls', namespace='rest_framework'))]