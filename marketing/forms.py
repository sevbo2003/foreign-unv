from django import forms
from .models import Subscribers


class EmailForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        fields = ('email',)

    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': "Emailni kiriting",
        'type': 'text',

    }), label='')
