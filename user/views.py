from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse, Http404,HttpResponseRedirect
from email import message
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from .forms import PostForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .forms import SignupForm, PostForm, UpdateUserForm, UpdateUserProfileForm
from django.http import HttpResponseRedirect
from .models import Post, Comment
import random
import json
from django.contrib.auth import get_user_model

from django.http import HttpResponse  
from .models import MpesaPayment
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from .forms import PaymentForm
import time
from .serializers import  ApplicantsSerializer, ApplySerializer, EmployerProfileSerializer, EmployerSerializer, MpesaPaymentSerializer,JobseekerSerializer, JobSerializer, SignUpSerializer,UpdateUserProfileSerializer
from .models import *
from decouple import config
import json
import requests
from rest_framework import viewsets
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes, force_text  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string  
from django.contrib.auth.models import User  
from django.core.mail import EmailMessage  
from django.contrib.auth import get_user_model
User = get_user_model()
from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from user.serializers import UserSerializer
from .serializers import UserSerializer
from rest_framework.response import Response
from .models import User
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime

# Create your views here.

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class EmployerProfileView(APIView):
    def get_employer_profile(self,request):

        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthorized')
        
        employer = Employer.objects.filter(user_id=payload['id']).first()
        serializer = EmployerProfileSerializer(employer)
        
        return Response(serializer.data)   


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
          'id':user.id,
          'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
          'iat': datetime.datetime.utcnow()
        }

        token = (jwt.encode(payload, 'secret', algorithm='HS256'))
        
        #return token via cookies
        response = Response()

        response.set_cookie(key='jwt', value=token,
                        httponly=True,samesite='none',secure=True)

        response.data = {
            'jwt': token
        }

        return response

        # return Response({
        #   # 'message':'login success',
        #   'jwt': token
        # })


class UserView(APIView):
    def get(self, request):

        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('unauthenticated')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthorized')

        #decode user credentials

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
          'message' : 'logged out successfully'
        }

        return response  


class MpesaPaymentViewSet(viewsets.ModelViewSet):  
      serializer_class = MpesaPaymentSerializer
      queryset = MpesaPayment.objects.all()

class ApplicantsViewSet(viewsets.ModelViewSet):  
      serializer_class = ApplicantsSerializer
      queryset = Applicants.objects.all()
    
class ApplyViewSet(viewsets.ModelViewSet):  
      serializer_class = ApplySerializer
      queryset = Apply.objects.all()

class JobViewSet(viewsets.ModelViewSet):  
      serializer_class = JobSerializer
      queryset = Job.objects.all()

class SignUpViewSet(viewsets.ModelViewSet):  
      serializer_class = SignUpSerializer
      queryset = User.objects.all()

class EmployerViewSet(viewsets.ModelViewSet):  
      serializer_class = EmployerSerializer
      queryset = User.objects.all()

class UpdateUserProfileViewSet(viewsets.ModelViewSet):  
      serializer_class = UpdateUserProfileSerializer
      queryset = UserProfile.objects.all()

class EmployerProfileViewSet(viewsets.ModelViewSet):  
      serializer_class = EmployerProfileSerializer
      queryset = EmployerProfile.objects.all()


@login_required
def profile(request):

    if request.method == 'POST':
        form = UpdateUserProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('dashboard')
    else:
        form = UpdateUserProfileForm()

    return render(request, '', {'form':form})

def user_profile(request, username):
    user_prof = get_object_or_404(User, username=username)
    if request.user == user_prof:
        return redirect('profile', username=request.user.username)
    params = {
        'user_prof': user_prof,
    }
    return render(request, '', params)

@login_required(login_url='login')
def edit_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return redirect('profile', user.username)
    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateUserProfileForm(instance=request.user.profile)
    params = {
        'user_form': user_form,
        'prof_form': prof_form
    }
    return render(request, 'profile', params)

def create_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.post = post
            post.user = request.user.profile
            post.save()
            return redirect('', post.id)
    else:
        form = PostForm()
    return render(request, 'post', {'form': form})

