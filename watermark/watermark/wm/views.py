from rest_framework import viewsets

from core.models import Document

from wm import serializers


class GetDocByTicketId(viewsets.ModelViewSet):
    """List Document in the database by ticketid"""
    queryset = Document.objects.all()
    serializer_class = serializers.DocumentSerializer

    def get_queryset(self):
        """Return objects for the specified tickket ID"""
        return self.queryset.filter(ticket_id=self.request.query_params.get('ticketid'))
