from django.contrib import admin
from django.urls import path, include

from chat import views
from chat.views import profile_view, RegisterView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('chat/', views.my_view, name='registration'),
    path('chat/index.html', views.index, name='glav'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('profile', profile_view, name="profile"),
    path('register/', RegisterView.as_view(), name="register"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
