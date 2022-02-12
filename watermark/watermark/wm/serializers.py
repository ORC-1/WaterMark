from rest_framework import serializers

from core.models import Document


class DocumentSerializer(serializers.ModelSerializer):
    """Serializer for Document objects"""
    def validate(self, value):
        """
        Check that the journal post has no topic.
        """
        if value.get('content')=='journal' and value.get('topic') != '':
            raise serializers.ValidationError("Jornals cant have topic")
        return value
    class Meta:
        model = Document
        fields = ('id', 'ticket_id', 'content', 'title',
                  'topic', 'author','water_mark'
        )
        extra_kwargs = {'water_mark': {'required': False},
                        'ticket_id': {'required': False},}
        read_only_fields = ('id',)
