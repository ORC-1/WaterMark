from django.test import TestCase

from core import models

class ModelTest(TestCase):
    def test_document_str(self):
        """Test the document string representation"""
        doc = models.Document.objects.create(
            ticket_id='123944-2399403-11s',
            content='book',
            title='The Dark Code',
            author='Bruce Wayne',
            topic='Science',
            water_mark=True
        )
        self.assertEqual(str(doc), doc.title)
