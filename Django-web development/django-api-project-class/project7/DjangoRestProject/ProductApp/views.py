from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404

# Create your views here.
@api_view(['GET', 'POST'])
def product_list_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


    elif request.method == 'POST':
        
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)  # To get the validated data
        serializer.save()  # saves the validated data into the DB
        print(serializer.data)  # gives the clean data in the form of JSON
    
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# API with parameter
@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_view(request, id):

    product = get_object_or_404(Product, pk=id)


    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)


    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
