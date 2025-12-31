from django.urls import path
from .views import register_page

app_name = 'user'

urlpatterns = [
    path('register/',register_page,name='register_page')
]