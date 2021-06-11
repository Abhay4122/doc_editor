from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('text_data_post', text_data_post, name='text_data_post'),
    path('doc_list', doc_list, name='doc_list'),
    path('get_text_data/<int:id>', get_text_data, name='get_text_data'),
]