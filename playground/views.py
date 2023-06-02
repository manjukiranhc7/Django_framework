from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class PlaygroundTemplate(TemplateView):
    template_name = 'report.html'
    extra_context = {"name":"Manju Kiran"}

class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'authorized.html'
    login_url = '/admin'

    
#def say_hello(request):
#    return render(request,'report.html',{"name":"Manju Kiran"})

#@login_required(login_url='/admin')
#def authorized(request):
#    return render(request, 'authorized.html',{})