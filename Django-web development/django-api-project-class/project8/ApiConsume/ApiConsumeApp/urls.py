from django.urls import path
from . import views

urlpatterns=[
    path('', views.home_view, name='home'),
    path('product/', views.Product_view, name="product"),
    path('addproduct/', views.add_product_view, name='addproduct'),
    path('updateproduct/<int:id>/', views.update_product_view, name='update')
]