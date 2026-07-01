from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CodeSnippetForm
from .models import CodeSnippet
from .models import Category
from django.shortcuts import get_object_or_404

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('home')
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
    category_name = request.GET.get('category')
    
    if category_name:
        snippets = CodeSnippet.objects.filter(category__name=category_name).order_by('-id')
    else:
        snippets = CodeSnippet.objects.all().order_by('-id')
        
    categories = Category.objects.all()
    
    return render(request, 'all_snippets.html', {
        'snippets': snippets,
        'categories': categories,
        'selected_category': category_name
    })

@login_required
def my_snippets(request):
    snippets = CodeSnippet.objects.filter(developer=request.user).order_by('-id')
    return render(request, 'my_snippets.html', {'snippets': snippets})

@login_required
def delete_snippet(request, snippet_id):
    snippet = get_object_or_404(CodeSnippet, id=snippet_id)
    
    if snippet.developer == request.user:
        if request.method == 'POST':
            snippet.delete()
            return redirect('my_snippets')
        return render(request, 'confirm_delete.html', {'snippet': snippet})
    else:
        return redirect('my_snippets')
    
@login_required
def edit_snippet(request, snippet_id):
    snippet = get_object_or_404(CodeSnippet, id=snippet_id, developer=request.user)
    
    if request.method == 'POST':
        form = CodeSnippetForm(request.POST, instance=snippet)
        if form.is_valid():
            form.save()
            return redirect('my_snippets')
    else:
        form = CodeSnippetForm(instance=snippet)
        
    return render(request, 'edit_snippet.html', {'form': form, 'snippet': snippet})