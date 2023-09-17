from django.urls import path
from .views import HomePageView, AboutPageView, SettingsPageView

urlpatterns = [
    path('settings/', SettingsPageView.as_view(), name='settings'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home')
]
