from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('products/category/<int:category_id>/', views.products_by_category, name='products_by_category'),
    path('bags/', views.bag_page, name='bagPage'),
    path('shags/', views.shag_page, name='shagPage'),
    path('about/', views.aboutPage, name='aboutPage'),
    path('contact/', views.contactPage, name='contactPage'),
    path('offer/', views.offer, name='offerPage'),
    path('why/', views.why, name='whyPage'),
    
    # Product detail page
    path('productDetail/<int:pk>/', views.productDetail, name='productDetail'),
    
]

# Serving media files during development
