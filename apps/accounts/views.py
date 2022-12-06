from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from django.db import IntegrityError
from django.views.generic import CreateView, TemplateView, ListView, UpdateView, DeleteView, DetailView

from .forms import SigninForm, CreateUserForm
from .models import UserProfile

# Register your views here.

class signinView(TemplateView):
  pass

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


@login_required()
def dashboard(request):
  if request.method == 'GET':
    return render(request, 'accounts/dashboard.html')

# terminar
@login_required()
def create_user(request):
  if request.method == 'GET':
    return render(request, 'accounts/create_user.html', {"form": CreateUserForm})
  else:
    if request.POST.get('is_admin') == 'on':
      role = 'ADMIN'
    else:
      role = 'EMPLOYEE'
    if request.POST["password1"] == request.POST["password2"]:

      try:
        user = UserProfile.objects.create_user(
          username = request.POST["username"],
          password = request.POST["password1"],
          first_name = request.POST["first_name"],
          last_name = request.POST["last_name"],
          email = request.POST["email"],
          img_profile = request.FILES.get("img_profile", None),
          business = request.user.business,
          role = role
        )

        user.save()
        return redirect('accounts:users')

      except IntegrityError:
        return render(request, 'accounts/create_user.html', {"form": CreateUserForm, "error": "Nombre de usuario ya existe"})

    return render(request, 'accounts/create_user.html', {"form": CreateUserForm, "error": "Las contraseñas no coninciden"})


@login_required()
def get_users(request):
  if request.method == 'GET':
    users = UserProfile.objects.filter(business=request.user.business)
    return render(request, 'accounts/users.html', {'users': users})


@login_required()
def user_detail(request, uname):
  if request.method == 'GET':
    user = get_object_or_404(UserProfile, username=uname)
    form = CreateUserForm(instance=user)

    return render(request, 'accounts/user_detail.html', {'form': form})


@login_required()
def delete_user(request, uname):
  if request.method == 'GET':
    user = get_object_or_404(UserProfile, username=uname)
    user.delete()
    return redirect('accounts:users')
