from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from .models.accounts import CustomerUser

class CustomerUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(CustomerUserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ["password1", "password2"]:
            self.fields[fieldname].help_text = None

    class Meta:
        model = CustomerUser
        fields = ('email', 'first_name', 'last_name')
        labels = {
            'email': 'Email',
            'first_name': 'First Name',
            'last_name': 'Last Name',
        }

class CustomerUserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput, label='Password')

    def __init__(self, *args, **kwargs):
        # Accept the request in form kwargs
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError('Invalid Credentials')
            if not user.is_active:
                raise forms.ValidationError('User is inactive')
            self.request.user = user

        return cleaned_data

    def get_user(self):
        return getattr(self, 'user', None)  # Return the authenticated user, if any