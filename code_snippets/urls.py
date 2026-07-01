from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('about/', views.about, name='about'),
    path('create/', views.create_snippet, name='create_snippet'),
    path('logout/', views.logout_view, name='logout'),
    path('snippets/', views.all_snippets, name='all_snippets'),
    path('my-snippets/', views.my_snippets, name='my_snippets'),
    path('delete/<int:snippet_id>/', views.delete_snippet, name='delete_snippet'),
]