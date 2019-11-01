from django.urls import path
from django.contrib.auth import views as auth_views
from home import  views

urlpatterns = [
    path('', views.home),
    path('contact/', views.contact, name = 'contact'),
    path('about/', views.about, name = 'about'),
    path('login/',auth_views.LoginView.as_view(template_name="pages/login.html"), name="login"),
    path('logout/',auth_views.LogoutView.as_view(next_page='/'), name="logout"),
    path('attend/cusformsea/', views.launchCusFormSea, name = 'cusformsea'),

    ]