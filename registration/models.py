from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    ROLES = (
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    
    role = models.CharField(max_length=10, choices=ROLES)
    groups = models.ManyToManyField(Group, verbose_name='groups', blank=True, related_name='registration_user_set')
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='registration_user_set',
        help_text='Specific permissions for this user.',
        related_query_name='registration_user',
    )


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    bio = models.TextField()
    subject = models.CharField(max_length=100)
    # Add any additional fields specific to the Teacher model
    
    # Add any additional methods or functionality for the Teacher model


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    grade = models.CharField(max_length=10)
    parent_email = models.EmailField()
    # Add any additional fields specific to the Student model
    
    # Add any additional methods or functionality for the Student model
