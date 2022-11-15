from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from django.db import IntegrityError

from .forms import SigninForm, CreateEmployeeForm
from .models import EmployeeProfile

# Register your views here.

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
def create_employee(request):
  if request.method == 'GET':
    return render(request, 'accounts/create_employee.html', {"form": CreateEmployeeForm})
  else:
    if request.POST["password1"] == request.POST["password2"]:
      try:
        user = EmployeeProfile.objects.create_user(
          username = request.POST["username"],
          password = request.POST["password1"],
          first_name = request.POST["first_name"],
          last_name = request.POST["last_name"],
          email = request.POST["email"],
          img_profile = request.FILES.get("img_profile", None),
          business = request.user.business,
        )

        user.save()
        return redirect('accounts:barbers')

      except IntegrityError:
        return render(request, 'accounts/create_employee.html', {"form": CreateEmployeeForm, "error": "Nombre de usuario ya existe"})

    return render(request, 'accounts/create_employee.html', {"form": CreateEmployeeForm, "error": "Las contraseñas no coninciden"})


@login_required()
def get_users(request):
  if request.method == 'GET':
    barbers = EmployeeProfile.objects.filter(business=request.user.business)
    return render(request, 'accounts/barbers.html', {'barbers': barbers})


@login_required()
def edit_user(request):
  if request.method == 'GET':
    return render(request, 'accounts/edit_user.html')