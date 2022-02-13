from django.urls import path
from wm import views
app_name = 'wm'

urlpatterns = [
    path('doc_by_id', views.GetDocByTicketId.as_view({'get': 'list'}),
     name='doc_by_id'),
    path('watermark', views.PostDocForWaterMark.as_view({'post': 'create'}),
     name='watermark'),
]
