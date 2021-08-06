from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from .models import account1
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from sign.serializer import EmpSerializer
from sign.forms import *

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Empviewset(viewsets.ModelViewSet):
    queryset = account1.objects.all()
    serializer_class = EmpSerializer

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#        print(Token.objects.create(user=instance))
#

# Create your views here.

def home(request):
    return render(request, 'home.html')


def dash(request):
    if 'user' in request.session:
        current_user = request.session['user']
        u = account1.objects.get(email = current_user)
        param = {'current_user': current_user,'users':u}
        return render(request, 'dashboard.html', param)
    else:
        return redirect('login')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        # form=Employee2(request.POST)
        # print(form)

        form = sign1(request.POST,request.FILES)
        if account1.objects.filter(email= id).count() > 0:
            return HttpResponse('Email Id already exists.')
        else:

            if form.is_valid():
                try:
                    # email = form.cleaned_data('email')
                    # print(email)
                    # token = Token.objects.create(user=email)
                    # print(token.key)

                    form.save()
                    return redirect('/login')
                except Exception as e:
                    print(e)
                    return redirect('/')

    else:
        form = sign1()

    return render(request, 'signup.html')





def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        check_user = account1.objects.filter(email=email, password=password)
        if check_user:
            request.session['user'] = email
            return redirect('dash')
        else:
            return HttpResponse('Please enter valid Username or Password.')

    return render(request, 'login.html')



def logout(request):
    try:
        del request.session['user']
    except:
        return redirect('login')
    return redirect('login')



def edit(request,id):
    # g1 = account1.objects.get(id=id)
    # return render(request,'dashboard.html',{'g1':g1})
    if 'user' in request.session:
        current_user = request.session['user']
        u = account1.objects.get(email = current_user)
        param = {'current_user': current_user,'users':u}
        return render(request, 'edit.html', param)
    else:
        return redirect('login')
    return render(request, 'login.html')


def update(request,id):
  user = account1.objects.get(id=id)
  if request.method == 'POST':
      first_name = request.POST.get('first_name')
      last_name = request.POST.get('last_name')
      email  = request.POST.get('email')
      dob = request.POST.get('dob')
      nationality = request.POST.get('nationality')
      gender = request.POST.get('gender')
      mobile = request.POST.get('mobile')
      address = request.POST.get('address')
      image = request.FILES['image']

      user.first_name = first_name
      user.last_name = last_name
      user.email = email
      user.dob = dob
      user.nationality = nationality
      user.gender = gender
      user.mobile = mobile
      user.address = address
      user.image = image
      user.save()
      return  HttpResponse('Updated Successfully')
  return HttpResponse('Updation failed')


def family2(request,id):
    user = account1.objects.get(id=id)
    if request.method == 'POST':
        form = sign2(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            return HttpResponse("Data Inserted Successfully!!")

            #user = Family.objects.get(id=id)
            #user = Family.objects.get(id=id)
            # return render(request,'demo.html',{'user': user})
        else:
            return  HttpResponse("Invalid Form")
    else:
        pass


