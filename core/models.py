
from django.db import models

# Hero Section
class Hero(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='hero_images/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# Product Model
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    old_price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    discount_percent = models.PositiveIntegerField(blank=True, null=True, help_text="Discount percent (e.g. 20 for 20% off)")
    badge = models.CharField(max_length=30, blank=True, null=True, help_text="Badge text (e.g. 'New', 'Hot', etc.)")
    is_bag = models.BooleanField(default=False)
    is_shag = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name