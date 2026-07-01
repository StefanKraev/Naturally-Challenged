from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CodeSnippetForm
from .models import CodeSnippet

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

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def about(request):
    return render(request, 'about.html')

@login_required
def create_snippet(request):
    if request.method == 'POST':
        form = CodeSnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.developer = request.user
            snippet.save()
            messages.success(request, 'Кодът беше успешно качен!')
            return redirect('home')
    else:
        form = CodeSnippetForm()
    return render(request, 'create_snippet.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def all_snippets(request):
    snippets = CodeSnippet.objects.all().order_by('-id')
    return render(request, 'all_snippets.html', {'snippets': snippets})