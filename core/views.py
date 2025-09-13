
from django.shortcuts import render
from django.http import JsonResponse
from .models import Hero, Category, Product


def home(request):
    hero = Hero.objects.filter(is_active=True).first()
    categories = Category.objects.all()
    bag_products = Product.objects.filter(is_bag=True)
    shag_products = Product.objects.filter(is_shag=True)
    return render(request, 'home.html', {
        'hero': hero,
        'categories': categories,
        'bag_products': bag_products,
        'shag_products': shag_products,
    })


def products_by_category(request, category_id):
    section_type = request.GET.get('type')
    if category_id == 0:
        if section_type == 'bag':
            products = Product.objects.filter(is_bag=True)
        elif section_type == 'shag':
            products = Product.objects.filter(is_shag=True)
        else:
            products = Product.objects.none()
    else:
        products = Product.objects.filter(category_id=category_id)
        if section_type == 'bag':
            products = products.filter(is_bag=True)
        elif section_type == 'shag':
            products = products.filter(is_shag=True)
    data = [
        {
            'id': p.id,
            'name': p.name,
            'description': p.description,
            'image': p.image.url if p.image else '',
            'price': str(p.price),
            'old_price': str(p.old_price) if p.old_price else '',
            'discount_percent': p.discount_percent if p.discount_percent else '',
            'is_bag': p.is_bag,
            'is_shag': p.is_shag,
        }
        for p in products
    ]
    return JsonResponse({'products': data})
