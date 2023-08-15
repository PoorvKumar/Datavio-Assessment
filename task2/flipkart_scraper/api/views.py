from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ScrapedData
from .scraper_utils import scrape_flipkart_data  # Implement this function

class ScrapeFlipkartAPIView(APIView):
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({"error": "You must be logged in to use this API."}, status=status.HTTP_401_UNAUTHORIZED)
        
        url = request.data.get("url")
        
        if not url:
            return Response({"error": "URL is required in the request payload."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Check if the URL belongs to the logged-in user
        if ScrapedData.objects.filter(user=request.user, url=url).exists():
            return Response({"error": "URL already exists in the database for this user."}, status=status.HTTP_409_CONFLICT)
        
        # Scrape data from Flipkart URL using scraper_utils.scrape_flipkart_data function
        scraped_data = scrape_flipkart_data(url)
        
        if scraped_data is None:
            return Response({"error": "Unable to scrape data from the provided URL."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Save scraped data to the database
        scraped_data['user'] = request.user
        ScrapedData.objects.create(**scraped_data)
        
        return Response({"message": "Scraped data saved successfully."}, status=status.HTTP_201_CREATED)
