from django.shortcuts import render
from django.urls import reverse_laz
from django.views.generic import CreateView

from . import forms
# Create your views here.

class SignUp(CreateView):
  form_class = forms.UserCreateForm
  # redirect to login page
  success_url = reverse_laz('login')
  template_name = 'accounts/signup.html'
