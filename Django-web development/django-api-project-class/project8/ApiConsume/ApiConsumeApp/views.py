from django.shortcuts import render, redirect
import requests

# Create your views here.

apiForProduct = 'http://127.0.0.1:8000'

def home_view(request):

    return render(request, 'home.html')


def Product_view(request):

    response = requests.get(apiForProduct).json()
    # res = response.json()

    # PRODUCT = Product.objects.all()

    return render(request, 'product.html', context={'response':response})



def detailed_view(request, id):

    response = requests.get(f'{apiForProduct}/{id}').json()
    # res = response.json()

    return render(request, 'product.html', context={'response':response})


def add_product_view(request):

    if request.method == 'POST':
     name  = request.POST.get('product_name')
     price = request.POST.get('price')
     quantity= request.POST.get('quantity')
   

     data1 = {
        'name': name,
        'unit_price': price,
        'quantity': quantity
     }

     response = requests.post(apiForProduct, json=data1)
        # res = response.json()

     if response.status_code == 201:
        return redirect('product')

    return render(request, 'addproduct.html')


def update_product_view(request, id):

    product = requests.get(f'{apiForProduct}/{id}').json()
    

    if request.method == 'POST':
     name  = request.POST.get('product_name')
     price = request.POST.get('price')
     quantity= request.POST.get('quantity')
   

     data1 = {
        'name': name,
        'unit_price': price,
        'quantity': quantity
     }

     response = requests.put(f'{apiForProduct}/{id}/', json=data1)
        # res = response.json()

     if response.status_code == 200:
        return redirect('product')

    return render(request, 'update.html' , context={'product':product})



def delete_view(request, id):

    response = requests.delete(f'{apiForProduct}/{id}')
    # res = response.json()

    
