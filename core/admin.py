from django.contrib import admin

# Hero Section

from .models import Hero, Category, Product


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'subtitle')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_bag', 'is_shag', 'created_at')
    list_filter = ('category', 'is_bag', 'is_shag')
    search_fields = ('name', 'description')