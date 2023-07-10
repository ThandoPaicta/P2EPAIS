from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    
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
