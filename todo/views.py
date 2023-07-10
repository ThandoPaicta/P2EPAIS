

from multiprocessing import context
from rest_framework import viewsets

from registration.views import send_email_confirmation


from .models import User, Lesson, Exam, StudyMaterial, Achievement, Notification
from .serializers import LearningAnalyticsSerializer, UserSerializer, LessonSerializer, ExamSerializer, StudyMaterialSerializer, AchievementSerializer, NotificationSerializer

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm


from django.contrib.auth import authenticate, login
from .forms import UserLoginForm
from django.contrib.auth import logout



from .models import Exam

from .models import YourModel
from .serializers import YourModelSerializer


from .models import Lesson, StudyMaterial
from django.http import JsonResponse

from .models import LearningAnalytics


from .models import User


class LearningAnalyticsViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = LearningAnalyticsSerializer

class YourModelViewSet(viewsets.ModelViewSet):
    queryset = YourModel.objects.all()
    serializer_class = YourModelSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

class StudyMaterialViewSet(viewsets.ModelViewSet):
    queryset = StudyMaterial.objects.all()
    serializer_class = StudyMaterialSerializer

class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


# #registration



# # import base64
# # from django.contrib.sites.shortcuts import get_current_site
# # from django.template.loader import render_to_string
# # from django.core.mail import EmailMessage
# # from django.shortcuts import render, redirect
# # from .forms import UserRegistrationForm
# # from django.contrib.auth.tokens import default_token_generator


# # def register(request):
# #     if request.method == 'POST':
# #         form = UserRegistrationForm(request.POST)
# #         if form.is_valid():
# #             user = form.save(commit=False)
# #             user.is_active = False
# #             user.save()
            
#             # Send email confirmation
#             current_site = get_current_site(request)
#             mail_subject = 'Activate your AI Robot Learning account'
#             message = render_to_string(
#                 'registration/activation_email.html',
#                 {
#                     'user': user,
#                     'domain': current_site.domain,
#                     'uid': base64.urlsafe_b64encode(str(user.pk).encode()).decode(),
#                     'token': default_token_generator.make_token(user),
#                 }
#             )
#             email = EmailMessage(mail_subject, message, to=[user.email])
#             email.send()
            
#             # Redirect to the login page after successful registration
#             return redirect('login')
#     else:
#         form = UserRegistrationForm()
    
#     return render(request, 'registration/registration.html', {'form': form})





#Login





def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Replace 'dashboard' with your desired redirect URL
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = UserLoginForm(request)
    return render(request, 'login.html', {'form': form})
#Home 
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

#Dashboards

def dashboard(request):
    # Example data for the dashboard table
    data = [
        { 'id': 1, 'name': 'Thando Nogemane', 'email': 'thando@example.com' },
        { 'id': 2, 'name': 'Nomathamsanqa', 'email': 'duka@example.com' },
        { 'id': 3, 'name': 'Dukenceni', 'email': 'duka@example.com' }
    ]

    context = {
        'data': data
    }

    return render(request, 'dashboard.html', context)


#logout

#register from registration app
def registration(request):
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

    context = {
        'form': form
    }

    return render(request, 'registration.html', context)





def logout_view(request):
    logout(request)
    return redirect('home')

#content_generation with content




def content_generation(request):
    # Logic for content generation goes here
    # For example, let's generate study materials for a specific lesson
    lesson_id = 1  # Replace with the lesson ID you want to generate content for

    try:
        lesson = Lesson.objects.get(id=lesson_id)
        study_materials = StudyMaterial.objects.filter(lesson=lesson)

        # Generate a list of study materials' content
        generated_content = [material.content for material in study_materials]

        # Render the content.html template with the generated_content
        return render(request, 'ccontent.html', {'generated_content': generated_content})

    except Lesson.DoesNotExist:
        return render(request, 'content.html', {'error': 'Lesson not found'})

    except Exception as e:
        return render(request, 'content.html', {'error': str(e)})


def personalized_learning(request):
    # 1. Retrieve the user information
    user = request.user

    # 2. Analyze user data
    # Implement  logic to analyze the user's data and determine personalized content
    # For example, you can check the user's progress, preferences, or any other relevant data

    # 3. Generate personalized content
    # Implement logic to generate personalized learning content based on the analysis

    personalized_content = StudyMaterial.objects.filter(lesson__in=user.progress)

    # 4. Prepare the response
    # Convert the personalized content to a list of dictionaries
    content_list = [
        {
            'title': content.title,
            'lesson': content.lesson.title,
            'content_type': content.get_content_type_display(),
            'content': content.content,
            'created_at': content.created_at,
            'updated_at': content.updated_at,
        }
        for content in personalized_content
    ]

    # 5. Return the response
    return JsonResponse({'content': content_list})


#exam assistance 




def exam_assistance(request):
    # Logic for the exam assistance page goes here
    exams = Exam.objects.all()  # Fetching data (assuming you have an Exam model)

    # Render the template with the fetched data
    return render(request, 'exam_assistance.html', {'exams': exams})

#learning anylitcs




def learning_analytics(request):
    # Fetch the learning analytics data for the logged-in user
    user = request.user
    analytics = LearningAnalytics.objects.get(user=user)

    # Perform any necessary calculations or data manipulation
    progress_percentage = (analytics.progress / 100) * 100

    # Pass the analytics data to the template
    context = {
        'analytics': analytics,
        'progress_percentage': progress_percentage,
    }

    return render(request, 'learning_analytics.html', context)
