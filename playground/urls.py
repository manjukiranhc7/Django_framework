from django.urls import path
from . import views

urlpatterns = [
    path("hello/",views.PlaygroundTemplate.as_view()),
    path("authorized/",views.AuthorizedView.as_view())
]