from django.contrib import admin
from django.utils.html import format_html
from gtts import gTTS
from io import BytesIO
from .models import User, Lesson, Exam, StudyMaterial, Achievement, Notification

from .models import LearningAnalytics

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'payment_status', 'subscription_status')
    list_filter = ('role', 'payment_status', 'subscription_status')
    search_fields = ('username', 'email')

admin.site.register(User, UserAdmin)

class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'updated_at', 'text_to_speech_button')
    search_fields = ('title', 'description')

    def text_to_speech_button(self, obj):
        tts_text = obj.title + ' ' + obj.description
        tts = gTTS(text=tts_text, lang='en')
        mp3_file = BytesIO()
        tts.save(mp3_file)
        mp3_file.seek(0)
        return format_html('<audio controls src="data:audio/mp3;base64,{}" type="audio/mpeg">Your browser does not support the audio element.</audio>',
                           mp3_file.read().encode('base64'))

    text_to_speech_button.short_description = 'Text to Speech'

admin.site.register(Lesson, LessonAdmin)

class ExamAdmin(admin.ModelAdmin):
    list_display = ('title', 'lesson', 'created_at', 'updated_at')
    list_filter = ('lesson',)
    search_fields = ('title', 'lesson__title')

admin.site.register(Exam, ExamAdmin)

class StudyMaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'lesson', 'content_type', 'created_at', 'updated_at')
    list_filter = ('lesson', 'content_type')
    search_fields = ('title', 'lesson__title')

admin.site.register(StudyMaterial, StudyMaterialAdmin)

class AchievementAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'achieved_at')
    list_filter = ('user',)
    search_fields = ('user__username', 'title')

admin.site.register(Achievement, AchievementAdmin)

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'created_at')
    list_filter = ('user',)
    search_fields = ('user__username', 'title')

admin.site.register(Notification, NotificationAdmin)




class LearningAnalyticsAdmin(admin.ModelAdmin):
    list_display = ('user', 'progress', 'achievement_count', 'exam_count')
    list_filter = ('user',)
    search_fields = ('user__username',)

    def achievement_count(self, obj):
        return obj.achievements.count()

    achievement_count.short_description = 'Achievements Count'

    def exam_count(self, obj):
        return obj.exams.count()

    exam_count.short_description = 'Exams Count'

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        # Add any additional filtering or ordering logic here
        return queryset

    def has_add_permission(self, request):
        # Customize whether to allow adding new LearningAnalytics objects
        return False

    def has_delete_permission(self, request, obj=None):
        # Customize whether to allow deleting LearningAnalytics objects
        return False

    def get_actions(self, request):
        # Customize the available actions for LearningAnalytics objects
        actions = super().get_actions(request)
        # Remove or add any actions as needed
        return actions

admin.site.register(LearningAnalytics, LearningAnalyticsAdmin)
