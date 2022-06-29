
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    body = forms.CharField (
        label='',
        widget=forms.Textarea(attrs={
            'rows' :'3',
            'placeholder' : 'LOUDERR!!!'
    }))

    image = forms.ImageField(required=False)




    class Meta:
        model = Post 
        fields = ['body', 'image']