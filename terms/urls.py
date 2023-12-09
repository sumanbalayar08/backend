from . import views
from django.urls import path

urlpatterns = [
    path('api/info/', views.get_terms, name='get_terms')
]