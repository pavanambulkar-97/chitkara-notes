from django.contrib import admin
from .models import Product, Review


# Optional: Customize how Product appears in admin
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'quantity',
                    'category', 'created_at', 'updated_at')
    list_filter = ('category',)




# Optional: Customize how Review appears in admin
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'rating', 'created_at')
    list_filter = ('rating',)
# Registering both models with their custom admin classes
admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)