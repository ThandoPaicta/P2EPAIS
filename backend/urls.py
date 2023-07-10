from django.urls import include, path
from rest_framework import routers
from todo import admin, views

from django.contrib import admin



router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('lessons', views.LessonViewSet)
router.register('exams', views.ExamViewSet)
router.register('study-materials', views.StudyMaterialViewSet)
router.register('achievements', views.AchievementViewSet)
router.register('notifications', views.NotificationViewSet)
router.register('learning-analytics', views.LearningAnalyticsViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('content/', views.content_generation, name='content_generation'),
    path('personalized-learning/', views.personalized_learning, name='personalized_learning'),
    path('exam-assistance/', views.exam_assistance, name='exam_assistance'),
    path('learning-analytics/', views.learning_analytics, name='learning_analytics'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.user_login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('register/', include(('registration.urls', 'registration'), namespace='registration')),
    path('logout/', views.logout_view, name='logout'),
    path('api/', include(router.urls)),
]
