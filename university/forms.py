from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'comment')

    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mt-3',
        'type': 'text',
        'id': 'name',
        'name': 'name',
        'placeholder': 'Ismingiz'
    }), label='')
    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mt-3',
        'type': 'email',
        'id': 'email',
        'name': 'email',
        'placeholder': 'Email manzilingiz'
    }), label='')

    comment = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control mt-3',
        'placeholder': 'Izoh qoldiring...',
        'rows': 3
    }), label='')
