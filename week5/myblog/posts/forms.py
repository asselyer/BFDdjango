from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=['title', 'body']

    def clean_title(self):
        title = self.cleaned_data['title']

        if title.isdigit():
            raise forms.ValidationError('Исправить')
        return title


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs={'class':'form-control'}

        self.fields['text'].widget.attrs['rows'] = 10
        self.fields['text'].widget.attrs['cols'] = 20

    class Meta:
        model = Comment
        fields = ['name', 'text']

