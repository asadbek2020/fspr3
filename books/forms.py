from django import forms

from books.models import BookModel, CategoryModel


class BookModelForm(forms.ModelForm):
    class Meta:
        model = BookModel
        exclude = ['created_at', 'updated_at']


class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = CategoryModel
        fields = ['title']
