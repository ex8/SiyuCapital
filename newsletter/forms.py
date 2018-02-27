from django import forms
from newsletter.models import Recipient, Comment


class RecipientForm(forms.ModelForm):
    class Meta:
        model = Recipient
        fields = ('first', 'last', 'email')
        widgets = {
            'first': forms.TextInput(attrs={'placeholder': 'First Name',
                                            'label': ''}),
            'last': forms.TextInput(attrs={'placeholder': 'Last Name',
                                           'label': ''}),
            'email': forms.TextInput(attrs={'placeholder': 'Email Address',
                                            'label': ''})
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name',
                                           'label': ''}),
            'body': forms.Textarea(attrs={'placeholder': 'Comment Body',
                                          'label': ''})
        }
