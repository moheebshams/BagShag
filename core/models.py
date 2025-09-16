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
    is_bag = models.BooleanField(default=False, help_text="Is this category for Bags?")
    is_shag = models.BooleanField(default=False, help_text="Is this category for Shags?")

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
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Special offer
from django.utils import timezone
from datetime import timedelta

class Offer(models.Model):
    title = models.CharField(max_length=100)
    sale = models.CharField(max_length=100, default="No sale")
    discount = models.CharField(max_length=100, default="0%")
    description = models.TextField()
    days = models.IntegerField(default=0)
    hours = models.IntegerField(default=0)
    minutes = models.IntegerField(default=0)
    seconds = models.IntegerField(default=0)
    image = models.ImageField(upload_to='offers/', blank=True, null=True)
    start_time = models.DateTimeField(default=timezone.now)

    @property
    def end_time(self):
        return self.start_time + timedelta(
            days=self.days, hours=self.hours,
            minutes=self.minutes, seconds=self.seconds
        )

    def __str__(self):
        return self.title



# Why Choose Us Section
class WhyChooseUs(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_class = models.CharField(
        max_length=100,
        help_text="Font Awesome class, e.g., 'fas fa-shipping-fast'"
    )

    def __str__(self):
        return self.title
    
# Banner Model
class Banner(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='banners/')

    def __str__(self):
        return self.title