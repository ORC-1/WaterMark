from rest_framework import serializers

from core.models import Document


class DocumentSerializer(serializers.ModelSerializer):
    """Serializer for Document objects"""

    class Meta:
        model = Document
        fields = ('id', 'ticket_id', 'content', 'title',
                  'topic', 'author','water_mark'
        )
        extra_kwargs = {'water_mark': {'required': False}}
        read_only_fields = ('id',)

        

        # def validate_topic(self, value):
        # """
        # Check that the blog post is about Django.
        # """
        # if 'django' not in value.lower():
        #     raise serializers.ValidationError("Blog post is not about Django")
        # return value
