
from rest_framework import serializers
from .models import Product

class ReviewSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    review_text = serializers.CharField()
    rating = serializers.DecimalField(max_digits=3, decimal_places=1)
    created_at = serializers.DateTimeField()

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'unit_price',
                  'quantity', 'price_with_tax', 'reviews']
    unit_price = serializers.IntegerField(
        source='price')  # Renaming price to unit_price
    
    price_with_tax = serializers.SerializerMethodField(
        method_name='calculate_tax')
    
    reviews = ReviewSerializer(source='review_set',many=True, read_only=True)

    def calculate_tax(self, product):
        return product.price * 1.2




   