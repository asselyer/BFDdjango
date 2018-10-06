from .models import Post, Comment
from django import forms


class ListForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["item", "completed"]
