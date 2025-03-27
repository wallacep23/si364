from django.urls import path
from solo2 import views

# https://docs.djangoproject.com/en/4.2/topics/http/urls/
app_name = 'solo2'
urlpatterns = [
    path('', views.MainView.as_view(), name='all'),
]
