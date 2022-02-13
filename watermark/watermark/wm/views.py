from rest_framework import viewsets
from threading import Thread

from core.models import Document

from wm import serializers, watermarker


class BaseWaterMarkAttrViewSet(viewsets.ModelViewSet):
    """Base viewset for Document attributes"""
    serializer_class = serializers.DocumentSerializer


class GetDocByTicketId(BaseWaterMarkAttrViewSet):
    """List Document in the database by ticketid"""
    queryset = Document.objects.all()

    def get_queryset(self):
        """Return objects for the specified tickket ID"""
        ticketid = self.request.query_params.get('ticketid')
        return self.queryset.filter(ticket_id=ticketid)


class PostDocForWaterMark(BaseWaterMarkAttrViewSet):
    """Manage documents in the database"""

    def perform_create(self, serializer):
        """Async Create and watermark a new document"""
        Thread(target=watermarker.watermarkdoc(serializer)).start()
