# Generated by Django 3.2.7 on 2022-05-10 12:57

import cloudinary.models
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_jobseeker', models.BooleanField(default=False)),
                ('is_employer', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('userId', models.IntegerField()),
                ('content', models.CharField(max_length=255)),
                ('post', models.CharField(max_length=255)),
                ('like', models.IntegerField()),
                ('dislike', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='EmployerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('contact', models.IntegerField()),
                ('location', models.IntegerField(blank=True)),
                ('address', models.CharField(max_length=255)),
                ('company_bio', models.CharField(max_length=255)),
                ('company_pic', models.FileField(blank=True, upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MpesaPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('type', models.TextField()),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('contact', models.TextField()),
            ],
            options={
                'verbose_name': 'Mpesa Payment',
                'verbose_name_plural': 'Mpesa Payments',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=255)),
                ('contact', models.CharField(blank=True, max_length=30)),
                ('email', models.CharField(max_length=255)),
                ('bio', models.TextField(max_length=255)),
                ('work_experience', models.TextField(choices=[('Less than a year', 'Less than a year'), ('one to three year', '1 to 3'), ('three to five years', '3 to 5 years'), ('Five years and more', '  5+ years')], max_length=30)),
                ('profile_image', models.FileField(blank=True, upload_to='')),
                ('address', models.CharField(max_length=100)),
                ('resume', models.FileField(blank=True, upload_to='')),
                ('skills', models.CharField(blank=True, choices=[('Cognitive', 'Cognitive Skills'), ('Management', 'Management Skills'), ('Interpersonal', 'Interpersonal Skills'), ('Other skills', 'Other skills')], max_length=30)),
                ('referees', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Jobseeker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image')),
                ('bio', models.TextField(blank=True)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('contact', models.CharField(blank=True, max_length=30)),
                ('availability', models.CharField(blank=True, max_length=20)),
                ('salary', models.IntegerField(blank=True)),
                ('name', models.IntegerField()),
                ('phone_no', models.CharField(max_length=50)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='jobseeker', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=255)),
                ('requirements', models.TextField()),
                ('jobtype', models.TextField(choices=[('Part Time', 'Part-Time'), ('Remote', 'Remote'), ('Full Time', 'Full-Time')], max_length=30)),
                ('Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job', to='user.employerprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=15)),
                ('location', models.CharField(blank=True, max_length=120)),
                ('address', models.CharField(max_length=255)),
                ('company_bio', models.CharField(max_length=255)),
                ('company_pic', models.FileField(upload_to='', verbose_name='image')),
                ('website', models.URLField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Applicants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_Name', models.CharField(max_length=255)),
                ('Email', models.CharField(max_length=255)),
                ('Contact', models.IntegerField()),
                ('Availability', models.CharField(max_length=255)),
                ('Salary_Expectations', models.CharField(max_length=255)),
                ('Relate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='relation', to='user.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Advertisements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_name', models.CharField(blank=True, max_length=255)),
                ('company', models.CharField(blank=True, max_length=255)),
                ('link', models.CharField(blank=True, max_length=255)),
                ('ad_content', models.TextField(blank=True, max_length=500)),
                ('ad_image', models.ImageField(null=True, upload_to='', verbose_name='ad_image')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='admin', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
