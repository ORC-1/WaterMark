from rest_framework import viewsets
from threading import Thread

from core.models import Document

from wm import serializers, watermarker


class GetDocByTicketId(viewsets.ModelViewSet):
    """List Document in the database by ticketid"""
    queryset = Document.objects.all()
    serializer_class = serializers.DocumentSerializer

    def get_queryset(self):
        """Return objects for the specified tickket ID"""
        ticketid = self.request.query_params.get('ticketid')
        return self.queryset.filter(ticket_id=ticketid)


class PostDocForWaterMark(viewsets.ModelViewSet):
    """Manage documents in the database"""
    serializer_class = serializers.DocumentSerializer

    def perform_create(self, serializer):
        """Async Create and watermark a new document"""
        Thread(target=watermarker.watermarkdoc(serializer)).start()
