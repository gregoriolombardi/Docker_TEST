from rest_framework import serializers

from .models import Document

class DocumentSerializer(serializers.ModelSerializer):
    """
    Document serializer.
    """  
    
    class Meta:
        model = Document
        fields = ['__all__' ]
        