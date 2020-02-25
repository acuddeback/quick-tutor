from django.shortcuts import render
from django.http import HttpResponse
from allauth.account.views import LoginView, SignupView, LogoutView, PasswordResetView
from django.views import generic
from .models import QTUser

def index(request):
    return render(request, 'QuickTutor/homepage.html', {})
# Create your views here.

class temporaryRedirectView(generic.TemplateView):
    model = QTUser
    template_name = 'QuickTutor/tempredirect.html'
    context_object_name = 'user' #This is the object that is referenced in the HTML script

    