from .models import Hero, Category, Product, Offer, WhyChooseUs
from django.shortcuts import render
from django.http import JsonResponse
from .models import Hero, Category, Product, Banner


def home(request):
    hero = Hero.objects.filter(is_active=True).first()
    bag_categories = Category.objects.filter(is_bag=True)
    shag_categories = Category.objects.filter(is_shag=True)
    bag_products = Product.objects.filter(category__is_bag=True)[:4]
    shag_products = Product.objects.filter(category__is_shag=True)[:4]
    offer = Offer.objects.first()
    why_choose_us = WhyChooseUs.objects.all()
    banners = Banner.objects.all()
    return render(request, 'home.html', {
        'hero': hero,
        'bag_categories': bag_categories,
        'shag_categories': shag_categories,
        'bag_products': bag_products,
        'shag_products': shag_products,
        'offer': offer,
        'why_choose_us': why_choose_us,
        'banners': banners,
    })

# Product detail view
def productDetail(request, pk):
    from django.shortcuts import get_object_or_404
    product = get_object_or_404(Product, pk=pk)
    # Fetch related products (same category, exclude current)
    related_products = Product.objects.filter(category=product.category).exclude(pk=product.pk)[:4]
    return render(request, 'productDetail.html', {
        'product': product,
        'related_products': related_products,
    })

def bag_page(request):
    bag_categories = Category.objects.filter(is_bag=True)
    bag_products = Product.objects.filter(category__is_bag=True)
    return render(request, 'bagPage.html', {
        'categories': bag_categories,
        'bag_products': bag_products,
    })

def shag_page(request):
    shag_categories = Category.objects.filter(is_shag=True)
    shag_products = Product.objects.filter(category__is_shag=True)
    return render(request, 'shagPage.html', {
        'categories': shag_categories,
        'shag_products': shag_products,
    })


def products_by_category(request, category_id):
    section_type = request.GET.get('type')
    if category_id == 0:

        if section_type == 'bag':
            products = Product.objects.filter(category__is_bag=True)
        elif section_type == 'shag':
            products = Product.objects.filter(category__is_shag=True)
        else:
            products = Product.objects.none()
    else:
        products = Product.objects.filter(category_id=category_id)
        if section_type == 'bag':
            products = products.filter(category__is_bag=True)
        elif section_type == 'shag':
            products = products.filter(category__is_shag=True)
    data = [
        {
            'id': p.id,
            'name': p.name,
            'description': p.description,
            'image': p.image.url if p.image else '',
            'price': str(p.price),
            'old_price': str(p.old_price) if p.old_price else '',
            'discount_percent': p.discount_percent if p.discount_percent else '',
            'badge': p.badge if p.badge else '',
        }
        for p in products
    ]
    return JsonResponse({'products': data})


def aboutPage(request):
    return render(request, 'aboutPage.html')

def contactPage(request):
    return render(request, 'contactPage.html')

def offer(request):
    offer = Offer.objects.first()
    return render(request, 'offer.html', {'offer': offer})

def why(request):
    why_items = WhyChooseUs.objects.all()
    return render(request, 'why.html', {'why_items': why_items})