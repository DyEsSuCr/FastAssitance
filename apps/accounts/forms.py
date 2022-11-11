from django import forms
from .models import User

class SigninForm(forms.ModelForm):
  class Meta:
    model = User

    fields = ('username', 'password')

    help_texts = {
      'username': None,
      'password': None,
    }

    widgets = {
      'username': forms.TextInput(attrs={
        'placeholder': 'Nombre de usuario',
        'class': 'w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md mb-6'
      }),
      
      'password': forms.PasswordInput(attrs={
        'placeholder': 'Contraseña',
        'class': 'w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md mb-6'
      }),
    }