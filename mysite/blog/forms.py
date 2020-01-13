from django import forms
from .models import Comment


class Shared_form(forms.Form):
    name = forms.CharField(max_length=30)
    send_email = forms.EmailField()
    to_email = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('submit_user', 'email', 'body')




