from django.urls import path
from .views import ALBUMViewset

urlpatterns = [
    path("albums/", ALBUMViewset.as_view()),
    path('albums/<int:id>', ALBUMViewset.as_view())
]
