from blog.models import Comment
from django import forms
from captcha.fields import CaptchaField

class CommentForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Comment
        fields = ['name', 'email', 'subject', 'message']