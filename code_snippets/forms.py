from django import forms
from .models import CodeSnippet

class CodeSnippetForm(forms.ModelForm):
    class Meta:
        model = CodeSnippet
        
        fields = ['title', 'content', 'category']
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }