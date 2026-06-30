from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class CodeSnippet(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField() 
    developer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='snippets')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='snippets')

    def __str__(self):
        return self.title