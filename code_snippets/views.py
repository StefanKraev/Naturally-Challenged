from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() # Създава потребителя в базата данни
            messages.success(request, 'Account created successfully!')
            return redirect('home') # Пренасочва след регистрация
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
