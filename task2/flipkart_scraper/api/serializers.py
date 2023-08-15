from rest_framework import serializers
from .models import ScrapedProduct

class ScrapedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrapedProduct
        fields = '__all__'
