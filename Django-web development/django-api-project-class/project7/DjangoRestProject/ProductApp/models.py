from django.db import models
class Product(models.Model):
    CATEGORY_CHOICES = [
        ("Electronics", "Electronics"),
        ("Stationary", "Stationary"),
         ("HomeAppliance", "HomeAppliance")
    ]
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    quantity = models.IntegerField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


class Review(models.Model):
    review_text = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


    def __str__(self):
        return f"Review for {self.product.name}"
