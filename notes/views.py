from django.shortcuts import render
from . models import Notes
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView
from .forms import NotesForm

class ListNotes(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = 'notes_list.html'

class NotesDetail(DetailView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes_detail.html"

class CreateNotes(CreateView):
    model = Notes
    form_class = NotesForm
    success_url = '/notes/notes_list'
    template_name = "notes_form.html"

# Create your views here.
#def list_notes(request):
#    all_notes = Notes.objects.all()
#    return render(request, 'notes_list.html',{'notes':all_notes})

#def notes_detail(request,pk):
#    try:
#        details= Notes.objects.get(pk=pk)
#    except Notes.DoesNotExist:
#        raise Http404("Note dosen't exist")
#    return render(request, 'notes_detail.html',{'notes':details})