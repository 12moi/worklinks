from rest_framework import serializers
from .models import  Apply, Employer, EmployerProfile, MpesaPayment,Job,UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email','name','password']
        extra_kwargs = {
          'password': {'write_only':True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class EmployerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = [ 'website','company_bio','company_name', 'company_pic', 'address','email', 'contact', 'location', ]

# class ApplicantsSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Applicants
#         fields = ['Full_Name', 'Email', 'Contact', 'Salary_Expectations']

class ApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Apply
        fields = ['Full_Name', 'Email', 'Contact', 'Salary_Expectations']

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
        fields = ['name','contact', 'email','location','address', 'company_bio', 'company_pic']

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
        fields = '__all__'

class JobseekerSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        fields = ['username',  'email', 'password']