from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from .forms import MyUserCreationForm


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customers/login.html', {})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('base')
            else:
                messages.add_message(request, messages.INFO, 'Неверный пароль или юзернейм')
        return render(request, 'customers/login.html', {})


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = MyUserCreationForm
        return render(request, 'customers/register.html', {form: 'form'})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = MyUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.username = user.username.lower()
                user.save()
                messages.add_message(request, messages.INFO, 'Спасибо за регистрацию')
                login(request, user)
                return redirect('base')
            else:
                messages.add_message(request, messages.INFO, 'Что то пошло не так...')
        return render(request, 'customers/register.html', {'form': form})
