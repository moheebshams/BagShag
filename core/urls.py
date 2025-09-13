from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('products/category/<int:category_id>/', views.products_by_category, name='products_by_category'),
]

# Serving media files during development
