from django.urls import path
from . import views

urlpatterns = [
    path("notes_list/",views.ListNotes.as_view(), name="notes.list"),
    path("<int:pk>/",views.NotesDetail.as_view(), name = "notes.detail"),
    path("new/",views.CreateNotes.as_view(),name="notes.new")
]