from django.shortcuts import render


def signin(request):
  url_template = 'accounts/signin.html'

  return render(request, url_template)