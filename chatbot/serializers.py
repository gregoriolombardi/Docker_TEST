from rest_framework import serializers

from .models import Conversation, Message
from .utils import time_since


class MessageSerializer(serializers.ModelSerializer):
    """
    Message serializer.
    """
    created_at = serializers.SerializerMethodField()
    
    
    class Meta:
        model = Message
        fields = ['id', 'conversation', 'content', 'is_from_user', 'in_reply_to', 'created_at', ]
        

    def get_created_at(self, obj):
        return time_since(obj.created_at)
    
    
class ConversationSerializer(serializers.ModelSerializer):
    """
    Conversation serializer.
    """
    messages = MessageSerializer(many=True, read_only=True)
    created_at = serializers.SerializerMethodField()
    character = serializers.SerializerMethodField()
    prebuild_messages = serializers.SerializerMethodField()
    
    class Meta:
        model = Conversation
        fields = ['id', 'title', 'favourite', 'archive', 'created_at', 'messages','character','prebuild_messages']

    def get_created_at(self, obj):
        return time_since(obj.created_at)
    def get_character(self, obj):
        try:
            return obj.character.url_image if obj.character.url_image else None
        except:
            return None
    def get_prebuild_messages(self, obj):
        try:
            return obj.character.prebuild_messages.all().filter(is_active=True).values_list('content', flat=True)
        except:
            return None