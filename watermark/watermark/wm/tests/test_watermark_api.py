from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Document

from wm.serializers import DocumentSerializer

# TODO:
# 1. make sure get works and tests pass (url, view and serializer)
# 2. make sure posts works and tests pass (url, view and serializer)
# 3. make sure background task and tests pass (function on post)
# 4. make sure that the ticketid is == 23 character and unique
GET_TICKET_URL = reverse('wm:doc_by_id')
WATERMARK_URL = reverse('wm:watermark')


class PublicRecipeApiTests(TestCase):
    """Test unathenticated water mark API access"""

    def setUp(self):
        self.client = APIClient()

    def test_auth_not_required(self):
        """Test that authentication is not required"""
        res = self.client.get(WATERMARK_URL)
        self.assertNotEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_ticket_api(self):
        """Test that the get ticket endpoint returns the right
           data with ticket_id"""
        doc = Document.objects.create(
            ticket_id='1239544503-2029393-2933',
            content='book',
            title='test title',
            topic='test topic',
            author='Chima',
            water_mark=True
        )
        res = self.client.get(GET_TICKET_URL+"?ticketid="+doc.ticket_id)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['author'], doc.author)


    def test_post_to_watermark_doc_api(self):
        """Test that the watermark endpoint posts successfully"""
        # subtest ticket_id
        payload = {
            'ticket_id': '0039544503-2029393-2933',
            'content': 'book',
            'title': 'Dark Code',
            'topic': 'Science',
            'author': 'Wayne'
        }
        res = self.client.post(WATERMARK_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(payload['ticket_id']), 23)


    def test_async_func_works(self):
        """Test that the get watermark service works in a nonblocking manner"""
        payload = {
            'ticket_id': '7779544503-2029393-2933',
            'content': 'book',
            'title': 'Dark Code',
            'topic': 'Science',
            'author': 'Wayne'
        }
        res = self.client.post(WATERMARK_URL, payload)

        exist = Document.objects.filter(
            ticket_id=payload['ticket_id']
        ).exists()

        self.assertFalse(exist)

    def test_jornal_entry_has_no_topic(self):
        """Test that the watermark endpoint handles jornal entry correctly"""
        payload = {
            'ticket_id': '0039544503-2029393-2933',
            'content': 'journal',
            'title': 'Dark Code',
            'topic': 'Science',
            'author': 'Wayne'
        }
        self.client.post(WATERMARK_URL, payload)
        res = self.client.post(WATERMARK_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
