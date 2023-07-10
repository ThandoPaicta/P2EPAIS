from rest_framework import serializers
from rest_framework import serializers
from .models import YourModel

from .models import User, Lesson, Exam, StudyMaterial, Achievement, Notification,LearningAnalytics

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'

class StudyMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyMaterial
        fields = '__all__'

class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class YourModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = YourModel
        fields = '__all__'

class LearningAnalyticsSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')

    class Meta:
        model = LearningAnalytics
        fields = ['username', 'progress', 'achievements', 'exams_taken']
