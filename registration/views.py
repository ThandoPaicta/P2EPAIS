from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
from .forms import UserRegistrationForm

def send_email_confirmation(request, user):
    current_site = get_current_site(request)
    mail_subject = 'Activate your AI Robot Learning account'
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    activation_link = reverse('verify_account', args=[uid, token])
    activation_url = f'http://{current_site.domain}{activation_link}'

    message = render_to_string(
        'registration/activation_email.html',
        {
            'user': user,
            'activation_url': activation_url,
        }
    )
    email = EmailMessage(mail_subject, message, to=[user.email])
    email.send()

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            # Send email confirmation
            send_email_confirmation(request, user)

            # Redirect to the login page after successful registration
            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})
