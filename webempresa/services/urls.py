from django.urls import path
from . import views as services_view
urlpatterns = [
    path('', services_view.services, name='services'),
    ]