from rest_framework import serializers
from .models import EmployerProfile, MpesaPayment,Job,UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class MpesaPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MpesaPayment
        fields = ['id', 'amount', 'contact']

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['id', 'title','requirements','location', 'jobtype']

class EmployerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployerProfile
        fields = ['user', 'name','contact', 'email','location','address', 'company_bio', 'company_pic']

class UpdateUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['full_name','profile_image','email','bio','resume','skills','work_experience','address','referees']

class SignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployerProfile
        fields = ['user', 'name','contact', 'email','location','address', 'company_bio', 'company_pic']

class JobseekerSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        fields = ['username',  'email', 'password']