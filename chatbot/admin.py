from django.contrib import admin
from .models import Conversation, Message, Character, PreBuildMessage


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    """
    Admin site configuration for Conversation model.
    """
    list_display = ('id', 'title', 'user', 'favourite', 'archive', 'created_at', 'updated_at',)
    list_filter = ('created_at', 'updated_at', 'favourite', 'archive',)
    search_fields = ('user__username', 'title',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """
    Admin site configuration for Message model.
    """
    list_display = ('id', 'conversation', 'content', 'is_from_user', 'created_at')
    list_filter = ('is_from_user', 'conversation__user__username', 'created_at')
    search_fields = ('content',)
    ordering = ('-created_at',)

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    """
    Admin site configuration for Character model.
    """
    list_display = ('id', 'name', 'user', 'created_at', 'updated_at',)
    list_filter = ('created_at', 'updated_at',)
    search_fields = ('user__username', 'name',)
    
@admin.register(PreBuildMessage)
class PreBuildMessageAdmin(admin.ModelAdmin):
    """
    Admin site configuration for PreBuildMessage model.
    """
    list_display = ('id', 'content', 'is_active', 'created_at', 'updated_at',)
    list_filter = ('created_at', 'updated_at',)
    search_fields = ('content',)