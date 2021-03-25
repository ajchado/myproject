from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin


app_name = 'myapp'
urlpatterns = [
	
	path('home', views.HomeIndexView.as_view(), name = "home_view"),
	path('index', views.MyappIndexView.as_view(), name = "Index_view"),
	path('login', views.LoginIndexView.as_view(), name = "Login_view"),
	path('registration_user', views.RegistrationIndexView.as_view(), name = "registration_user_view"),
	path('adminlogin', views.AdminLoginIndexView.as_view(), name = "AdminLogin_view"),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpattern += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpattern += static(settings.Static_URL, document_root=settings.STATIC_ROOT)