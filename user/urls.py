from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from . import views
from rest_framework.routers import DefaultRouter
from .views import    SignUpViewSet, UpdateUserProfileViewSet
from rest_framework import routers
# from rest_framework_swagger.views import get_swagger_view
from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi


# schema_view = get_schema_view(
#    openapi.Info(
#       title="Worklinks API",
#       default_version='v1',
#       description="Test description",
#       terms_of_service="https://www.google.com/policies/terms/",
#       contact=openapi.Contact(email="contact@snippets.local"),
#       license=openapi.License(name="BSD License"),
#    ),
#    public=True,
#    permission_classes=[permissions.AllowAny],
#    authentication_classes=[]
# )

# schema_view = get_swagger_view(title='users API')

router = routers.DefaultRouter()
router.register('Job', views.JobViewSet)
router.register('MpesaPayment', views.MpesaPaymentViewSet)
router.register('User', views.SignUpViewSet)
# router.register('Jobseeker', views.JobseekerViewSet)
router.register('UpdateUserProfile', views.UpdateUserProfileViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('MpesaPayment/', views.MpesaPayment, name='MpesaPayment'),
    path('job/', views.Job, name='Job'),
    path('jobseeker/', views.Jobseeker, name='Jobseeker'),
    path('user/', views.User, name='User'),
    path('profile/', views.Profile, name='UpdateUserProfile'),
    
   
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
