from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ScrappedProduct(models.Model):
    title=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    description=models.TextField(blank=True,null=True)
    num_reviews=models.IntegerField()
    num_ratings=models.IntegerField()
    ratings=models.FloatField()
    media_count=models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)