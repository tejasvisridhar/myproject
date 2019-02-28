from django.contrib.auth import login, logout, authenticate
#from django.core.urlresolvers import reverse_lazy
from django.urls import reverse_lazy
# from django.views.generic import CreateView
from django.views.generic import *
from django.shortcuts import render
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from . import forms

class SignUp(SuccessMessageMixin,CreateView):
    form_class = forms.UserCreateForm
    


    success_url = reverse_lazy("test")
    template_name = "accounts/signup.html"
    success_message = "User Added"

    def form_valid(self, form):
        valid = super(SignUp, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid


