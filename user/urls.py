from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from rest_framework.routers import DefaultRouter
from .views import    EmployerProfileView, SignUpViewSet, UpdateUserProfileViewSet
from rest_framework import routers
from .views import LogoutView, RegisterView, LoginView, UserView
# from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
# schema_view = get_swagger_view(title='Worklinks API')

# schema_view = get_schema_view(
#    openapi.Info(
#       title="Worlinks API",
#       default_version='v1',
#       description="Test description",
#       terms_of_service="https://www.google.com/policies/terms/",
#       contact=openapi.Contact(email="contact@snippets.local"),
#       license=openapi.License(name="BSD License"),
#    ),
#    public=True,
#    permission_classes=[permissions.AllowAny],
# )


router = routers.DefaultRouter()
router.register('Job', views.JobViewSet)
router.register('MpesaPayment', views.MpesaPaymentViewSet)
router.register('User', views.SignUpViewSet)
# router.register('Jobseeker', views.JobseekerViewSet)
router.register('UpdateUserProfile', views.UpdateUserProfileViewSet)
router.register('EmployerProfile', views.EmployerProfileViewSet)
# router.register('Applicants', views.ApplicantsViewSet)
router.register('Apply', views.ApplyViewSet)


urlpatterns = [
   path('register', RegisterView.as_view()),
   
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    path('employer/profile/', EmployerProfileView.as_view()),
    path('', include(router.urls)),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('MpesaPayment/', views.MpesaPayment, name='MpesaPayment'),
    path('job/', views.Job, name='Job'),
    path('jobseeker/', views.Jobseeker, name='Jobseeker'),
    path('EmployerProfile/', views.EmployerProfile, name='EmployerProfile'),
    path('user/', views.User, name='User'),
    path('profile/', views.UserProfile, name='UpdateUserProfile'),
    # path('Applicants/', views.Applicants, name='Applicants'),
    path('Apply/', views.Apply, name='Apply'),
    

#    path('swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
#    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

   
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
