from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import FormView

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from chat.forms import RegisterForm


def profile_view(request):
    return render(request, 'profile.html')


def my_view(request):
    return render(request, 'registration/login.html')


def index(request):
    return render(request, "index.html")


from django.shortcuts import render


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


from django.shortcuts import render


def room_view(request, room_name):
    username = request.user.username  # Get the username of the authenticated user
    return render(request, 'room.html', {
        'room_name': room_name,
        'username': username  # Pass the username to the template context
    })


def password_change(request):
    return render(request, 'registration/password_change.html')
