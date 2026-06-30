from django import forms
from .models import CodeSnippet

class CodeSnippetForm(forms.ModelForm):
    class Meta:
        model = CodeSnippet
        # Тук описваме кои полета да вижда потребителят
        # 'developer' не го добавяме, защото ще го взимаме автоматично от request.user
        fields = ['title', 'content', 'category']
        
        # Можеш да добавиш и малко стил (например за Bootstrap)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }