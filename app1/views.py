from django.contrib.auth.models import User
from django.shortcuts import render


def index(request, template_name):
    User.objects.get(id=1).save()
    return render(request, template_name, locals())
