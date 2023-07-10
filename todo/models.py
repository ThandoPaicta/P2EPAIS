from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):
    ROLES = (
        ('admin', 'Admin'),
        ('student', 'Student'),
    )

    role = models.CharField(max_length=10, choices=ROLES)
    payment_status = models.BooleanField(default=False)
    subscription_status = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group, verbose_name='groups', blank=True, related_name='backend_user_set')
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='backend_user_set',
        help_text='Specific permissions for this user.',
        related_query_name='backend_user',
    )

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        app_label = 'backend'



class Lesson(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Exam(models.Model):
    title = models.CharField(max_length=100)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    questions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class StudyMaterial(models.Model):
    CONTENT_TYPES = (
        ('text', 'Text'),
        ('video', 'Video'),
        ('interactive', 'Interactive'),
    )

    title = models.CharField(max_length=100)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    content_type = models.CharField(max_length=20, choices=CONTENT_TYPES)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Achievement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    achieved_at = models.DateTimeField(auto_now_add=True)


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class YourModel(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()

    def __str__(self):
        return self.field1


class LearningAnalytics(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='learning_analytics')
    progress = models.IntegerField(default=0)
    achievements = models.IntegerField(default=0)
    exams_taken = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username




