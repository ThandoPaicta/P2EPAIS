from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import User

UserModel = get_user_model()

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    role = forms.ChoiceField(choices=User.ROLES)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'role')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = False  # Set user as inactive until email confirmation
        if commit:
            user.save()
            self.send_email_confirmation(user)
        return user

    def send_email_confirmation(self, user):
        current_site = get_current_site(self.request)
        mail_subject = 'Activate your AI Robot Learning account'
        message = render_to_string(
            'registration/activation_email.html',
            {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            }
        )
        email = EmailMessage(mail_subject, message, to=[user.email])
        email.send()


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
