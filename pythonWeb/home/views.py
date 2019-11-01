from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import CusFormSea
import os
from django import forms
from sqlite3 import Error
import sqlite3
#from .functions import  generateInsertCommand # generateUpdateCommand, generateSelectCommand, generateDeleteCommand, convertFieldLisTToSQL
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
######
from django import template
from django.contrib.auth.models import Group, User
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict

# Create your views here.

# views home page
def home(request):
    return render(request, 'pages/home.html')
# views contact page
@login_required(login_url='/login/')
def contact(request):
    user=request.user.get_username()
    users_in_group = Group.objects.get(name="even").user_set.all()
    print(user)
    print(users_in_group)
    print (type (user))
    k=0
    print(k)   
    for i in range(0,len(users_in_group)):
        one_user_in_group = users_in_group[i]
        one_user = str(one_user_in_group)
        print(type(one_user))
        print(one_user)
        if user == one_user:
            k=k+1
    if k>0:
        print(k)
        return render(request, 'pages/contact1.html')
    else:
        k=0
        print(k)
        return render(request, 'pages/contact.html')

# views about page
def about(request):
    return render(request, 'pages/about.html')

# views form logictis sea
@login_required(login_url='/login/')
def launchCusFormSea(request):
    form = CusFormSea()
    if request.method == 'POST':
        form = CusFormSea(request.POST)
        if form.is_valid():
            if 'Confirm' in request.POST['Save']:
                form.save()
            return HttpResponseRedirect('/')
    return render(request, 'pages/cusformsea.html', {'form': form})