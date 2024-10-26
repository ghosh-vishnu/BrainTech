from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('career/', views.career, name='career'),
    path('service/', views.service, name='service'),
    path('software-intern/', views.software_intern, name='software_intern'),
    path('thanks/', views.thanks, name='thanks'),
    path('verify/', views.verify, name='verify'),
    path('web-intern/', views.web_intern, name='web_intern'),
    path('upload-certificate/', views.upload_certificate, name='upload_certificate'),
    path('success/', views.success_view, name='success'),
    path('verify-certificate/', views.verify_certificate, name='verify_certificate'),
    path('download/<str:certificate_number>/', views.download_certificate, name='download_certificate'),
]
