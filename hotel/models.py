from django.db import models
 
class GFG(models.Model):
    hotel_name = models.CharField(max_length=50)
    hotel_price = models.IntegerField()
    hotel_description = models.TextField()
    created_at = models.DateField(auto_now_add =True)
    updated_at = models.DateField(auto_now  =True)
     
    def __str__(self) -> str:
        return self.hotel_name

