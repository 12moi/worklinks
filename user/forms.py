from django import forms
from .models import   EmployerProfile, UserProfile
from xml.etree.ElementInclude import include
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import  Comment, Post,Job, Jobseeker


class PaymentForm(forms.ModelForm):
    id = forms.IntegerField()
    name = forms.CharField()
    amount=forms.IntegerField(required=True)
    contact= forms.IntegerField(required=True)

# class EmployerProfileForm(forms.ModelForm):
#      class Meta:
#         model = User
#         fields = ['id','email','name','password']
#         extra_kwargs = {
#           'password': {'write_only':True}
#         }

class EmployerProfileForm(forms.ModelForm):
    class Meta:
        model = EmployerProfile
        fields = '__all__'

class SignupForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.CharField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta(UserCreationForm.Meta):
        model = User
        fields  = '__all__'

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email')


class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['full_name','profile_image','email','bio','resume','skills','work_experience','address','referees']
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title']

# class EmployerForm(forms.ModelForm):
#     class Meta:
#         model = Employer
#         fields = ['user', 'name','contact', 'email','location','address', 'company_bio', 'company_pic']

class JobseekerForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username',  'email', 'password']

    
    def save(self):
        user = super().save(commit=False)
        user.is_jobseeker = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        jobseeker = Jobseeker.objects.create(user=user)
        jobseeker.email = self.cleaned_data.get('email')
        jobseeker.save()

        return jobseeker

# class ApplicantsForm(forms.ModelForm):
#     class Meta:
#         model = Applicants
#         fields = '__all__'
       

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('id', 'Title','Requirements','Location', 'Job Type')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user']