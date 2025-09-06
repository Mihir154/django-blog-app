from django import forms
from blog.models import Category, Blog

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields = '__all__'

class PostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'category', 'image', 'description', 'body', 'status', 'is_featured')