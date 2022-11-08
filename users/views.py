from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DeleteView, UpdateView

from .forms import UserRegisterForm, CustomUserCreationForm
from django.contrib.auth import get_user_model

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'index.html')


class AllUsers(ListView):
    model = User

class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    success_url = '/users'
    template_name = "users/DeleteUser.html"

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    template_name = 'users/UpdateUser.html'
    success_url = '/users'

def UserCreateView(request):
    if request.POST == 'POST':
        form = CustomUserCreationForm()
        if form.is_valid():
            form.save()
    else:
        form = CustomUserCreationForm()
    messages.success(request, 'Account created successfully')
    context = {
        'form': form
    }
    return render(request, 'users/newUser.html', context)
