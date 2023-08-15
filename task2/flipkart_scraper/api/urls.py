from django.urls import path
from .views import ScrapingView

urlpatterns = [
    path('scrape/', ScrapingView.as_view(), name='scrape-flipkart'),
]
