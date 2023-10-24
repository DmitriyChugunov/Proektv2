from django.contrib import admin
from django.template.backends import django
from django.urls import include, path

from chat import views
from chat.views import profile_view, RegisterView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('chat/', views.my_view, name='registration'),
    path('chat/index.html', views.index, name='glav'),
    path('chat/<str:room_name>/', views.room_view, name='room'),
    path("admin/", admin.site.urls),
    path('profile/', profile_view, name="profile"),
    path('register/', RegisterView.as_view(), name="register"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('accounts/password_chang/', views.password_change, name="reset")
    
]
