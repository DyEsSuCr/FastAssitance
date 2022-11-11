from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.views.generic import View
from .forms import SigninForm


class Signin(View):
  def get(self, request, *arg, **kwargs):
    
    url_template = 'accounts/signin.html'

    if request.user.is_authenticated:
      return render(request, url_template, {'form':SigninForm})
      
    return render(request, url_template, {'form':SigninForm})


  def post(self, request, *arg, **kwargs):

     username = request.POST['username']
     password = request.POST['password']
     user = auth.authenticate(username=username, password=password)
     if user is not None:
       auth.login(request, user)
       return redirect('https://www.youtube.com/')
     else:
       messages.info(request, 'Credenciales invalidas')
       return redirect('accounts:signin')