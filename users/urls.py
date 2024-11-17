from django.urls import path
from .views import USERViewset

urlpatterns = [
    path("users/", USERViewset.as_view()),
    path('users/<int:id>', USERViewset.as_view())
]
