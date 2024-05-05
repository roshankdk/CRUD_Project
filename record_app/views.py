from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponseNotAllowed, HttpResponseRedirect, Http404
from django.contrib.auth.models import User
from django.urls import is_valid_path
from .forms import userForm
from .models import user
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = userForm(request.POST)
        if form.is_valid():
            fn = form.cleaned_data['first_name']
            ln = form.cleaned_data['last_name']
            em = form.cleaned_data['email']
            ph = form.cleaned_data['phone']
            reg_user = user(first_name=fn,last_name=ln,email=em,phone=ph)
            reg_user.save()
            form = userForm()   
    else:
        form = userForm()

    record = user.objects.all()
    return render(request,'record_app/index.html',{'form':form, 'record':record})

def update(request,id):
    if request.method == "POST":
        form = user.objects.get(pk=id)
        fm = userForm(request.POST,instance=form)
        if fm.is_valid():
            fm.save()
            fm = userForm()
    else:
        form = user.objects.get(pk=id)
        fm = userForm(instance=form)
    return render(request,'record_app/update.html',{"form":fm})

def delete(request,id):
    if request.method == "POST":
            del_rec = user.objects.get(pk=id)
            del_rec.delete()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseNotAllowed(['POST'])
