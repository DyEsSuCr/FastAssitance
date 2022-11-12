from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from .forms import SigninForm


def signin(request):
    if request.method == 'GET':
      if request.user.is_authenticated:
        return redirect('accounts:dashboard')
      else:
        return render(request, 'accounts/signin.html', {'signin_form': SigninForm})

    else:
      username = request.POST['username']
      password = request.POST['password']

      user = auth.authenticate(username=username, password=password)

      if user is not None:
        auth.login(request, user)
        return redirect('accounts:dashboard')
      else:
        messages.info(request, 'Credenciales invalidas')
        return redirect('accounts:signin')


@login_required()
def signout(request):
  auth.logout(request)
  return redirect('accounts:signin')


def dashboard(request):
  return render(request, 'accounts/dashboard.html')