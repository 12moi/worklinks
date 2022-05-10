import django
from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
# from rest_framework.authtoken.models import Token
# from sqlalchemy import true
# from worklinks.settings import AUTH_USER_MODEL
from cloudinary.models import CloudinaryField
# from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class User(AbstractUser):
    is_jobseeker = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def save_user(self):
        self.save()

    def update_user(self):
        self.update()

    def delete_user(self):
        self.delete()

#     def __str__(self):
#         return self.username


# @receiver(post_save, sender=AUTH_USER_MODEL)



class UserProfile(models.Model):
    EXPRIENCE_LEVEL= [
        ('Less than a year', 'Less than a year'),
        ('one to three year','1 to 3'),
        ('three to five years','3 to 5 years'),
        ('Five years and more','  5+ years'),
      ]
    SKILL_TYPE= [
        ('Cognitive', 'Cognitive Skills'),
        ('Management','Management Skills'),
        ('Interpersonal','Interpersonal Skills'), 
        ('Other skills','Other skills'),
      ]
    # id = models.IntegerField(User, unique=True, primary_key=True)
    id = models.BigAutoField(primary_key=True)
    full_name = models.CharField(max_length=255)
    contact = models.CharField(max_length=30,  blank=True)
    email = models.CharField(max_length=255)
    bio = models.TextField(max_length=255)
    work_experience = models.TextField(max_length=30, choices=EXPRIENCE_LEVEL)
    profile_image =models.FileField(blank=True)
    address = models.CharField(max_length=100)
    resume = models.FileField(blank=True)
    skills =  models.CharField(max_length=30, blank=True, choices=SKILL_TYPE )
    referees = models.CharField(max_length=255, blank=True)


class Jobseeker(models.Model):
    user = models.OneToOneField(
        User, related_name='jobseeker', on_delete=models.CASCADE)
    profile_photo = CloudinaryField('image',  blank=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100,  blank=True)
    contact = models.CharField(max_length=30,  blank=True)
    availability = models.CharField(blank=True,  max_length=20)
    salary = models.IntegerField(blank=True)
    name = models.IntegerField(blank=False)
    phone_no = models.CharField(max_length=50, blank=False)
    email = models.CharField(max_length=50, blank=True)
    password = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name

    def save_jobseeker(self):
        self.save()

    def delete_jobseeker(self):
        self.delete()

    @classmethod
    def update_jobseeker(self):
        self.update()

    @classmethod
    def search_jobseekers_by_job_category(cls, job_category):
        jobseekers = Jobseeker.objects.filter(
            job_category__icontains=job_category)
        return jobseekers


class Employer(models.Model):
    user = models.OneToOneField(
        User, related_name='employers', on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    contact = models.CharField(max_length=15)
    location = models.CharField(max_length=120, blank=True)
    address = models.CharField(max_length=255)
    company_bio = models.CharField(max_length=255)
    company_pic =models.FileField('image')
    website = models.URLField(blank=True)

class Applicants(models.Model):
    Applicant_id = models.AutoField(primary_key=True)
    Full_Name = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    Contact = models.IntegerField()
    Availability= models.CharField(max_length=255)
    Salary_Expectations = models.CharField(max_length=255)



    def save_Applicants(self):
        self.save()

    def delete_Applicants(self):
        self.delete()

class EmployerProfile(models.Model):
    user = models.OneToOneField(
        User, related_name='employer', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    contact = models.IntegerField()
    location = models.IntegerField(blank=True)
    address = models.CharField(max_length=255)
    company_bio = models.CharField(max_length=255)
    company_pic = models.FileField(blank=True)


    def save_employer(self):
        self.save()

    def delete_employer(self):
        self.delete()

    @classmethod
    def search_by_company_name(cls, search_term):
        company = cls.objects.filter(title__icontains=search_term)
        return company

    def __str__(self):
        return self.name


class MpesaPayment(models.Model):
    amount = models.DecimalField(max_digits=10, blank=False, decimal_places=2)
    description = models.TextField()
    type = models.TextField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact = models.TextField()

    class Meta:
        verbose_name = "Mpesa Payment"
        verbose_name_plural = "Mpesa Payments"

    def __str__(self):
        return self.first_name


class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    file = models.FileField()

    def __str__(self):
        return f'{self.title}'

    def delete_post(self):
        self.delete()

    @classmethod
    def search_project(cls, title):
        return cls.objects.filter(title__icontains=title).all()

    @classmethod
    def all_posts(cls):
        return cls.objects.all()

    def save_post(self):
        self.save()


class Comment(models.Model):
    id = models.IntegerField(primary_key=True)
    userId = models.IntegerField()
    content = models.CharField(max_length=255)
    post = models.CharField(max_length=255)
    like = models.IntegerField()
    dislike = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f'{self.user.name} post'

    def delete_user(self):
        self.delete()


class Job(models.Model):
    JOB_TYPE = [
        ('Part Time', 'Part-Time'),
        ('Remote', 'Remote'),
        ('Full Time', 'Full-Time'),
    ]
    Id= models.ForeignKey(EmployerProfile,  on_delete=models.CASCADE, related_name='job')
    title = models.CharField(max_length=30)
    location = models.CharField(max_length=255)
    requirements = models.TextField()
    jobtype = models.TextField(max_length=30, choices=JOB_TYPE)

    def save_job(self):
        self.save()

    def delete_job(self):
        self.delete()

    def __str__(self):
        return self.title


class Advertisements(models.Model):
    user = models.OneToOneField(
        User, related_name='admin', on_delete=models.CASCADE)
    ad_name = models.CharField(max_length=255, blank=True)
    company = models.CharField(max_length=255, blank=True)
    link = models.CharField(max_length=255, blank=True)
    ad_content = models.TextField(max_length=500, blank=True)
    ad_image = models.ImageField('ad_image', null=True)

    def __str__(self):
        return self.ad_name
