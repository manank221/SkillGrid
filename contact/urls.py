from django.urls import path
from .views import ContactView, contact_ajax

app_name = 'contact'

urlpatterns = [
    path('', ContactView.as_view(), name='contact'),
    path('ajax/', contact_ajax, name='contact_ajax'),
] 