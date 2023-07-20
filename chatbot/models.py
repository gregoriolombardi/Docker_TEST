from django.db import models
from django.conf import settings
import secrets


def generate_secure_random_id():
    min_value = 10 ** 10  # Minimum value of the range (inclusive)
    max_value = 10 ** 11 - 1  # Maximum value of the range (exclusive)
    return secrets.randbelow(max_value - min_value) + min_value

class  Character(models.Model):
    """
    Character model representing a character within a conversation.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default="Empty")
    created_at = models.DateTimeField(auto_now_add=True)
    prompt = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    url_image = models.URLField(blank=True, null=True)
    prebuild_messages = models.ManyToManyField('PreBuildMessage', blank=True)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Character {self.id} - {self.prompt}"


class Conversation(models.Model):
    """
    Conversation model representing a chat conversation.
    """
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('archived', 'Archived'),
        ('ended', 'Ended'),
    ]

    id = models.BigIntegerField(primary_key=True, default=generate_secure_random_id, editable=False)
    title = models.CharField(max_length=255, default="Empty")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    favourite = models.BooleanField(default=False)
    archive = models.BooleanField(default=False)
    character = models.ForeignKey(Character, on_delete=models.CASCADE, null=True, blank=True)

    # status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"Conversation {self.title} - {self.user.username}"


class Message(models.Model):
    """
    Message model representing a message within a conversation.
    """
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_from_user = models.BooleanField(default=True)
    in_reply_to = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='replies')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Message {self.id} - {self.conversation}"

class PreBuildMessage(models.Model):
    """
    Message model representing prebuild message to use in a conversation.
    """
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Prebuild Message {self.content}"

