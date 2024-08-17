from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class catagory(models.Model):
    name = models.CharField(max_length=225 , db_index=True)
    slug = models.SlugField(max_length= 225, unique=True)
    class meta:
        verbose_name_plural = 'catagory'
    def __str__(self):
        return self.name
    
class product(models.Model):
    catagory = models.ForeignKey(catagory,related_name='product',on_delete=models.CASCADE)
    craeted_by = models.ForeignKey(User,related_name='product_author',on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='\images')
    discription = models.TextField(blank=True)
    price = models.DecimalField(max_digits=4 , decimal_places=2)
    created = models.DateTimeField(auto_now_add=True )
    updated = models.DateTimeField(auto_now=True)
    is_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    class meta:
        verbose_name_plural = 'catagory'
        ordering = "-category"

    def __str__(self):
        return self.title   

