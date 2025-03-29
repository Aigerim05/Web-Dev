import json
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .serializers import ProductSerializer, ProductSerializer2

from .models import *

@csrf_exempt
def products_list(request):
    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)

    elif request.method == "POST":
        data = json.loads(request.body)
        serializer = ProductSerializer2(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=201)


@csrf_exempt
def get_product(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist as e:
        return JsonResponse({"error" : str(e)}, status=404)
   
    if request.method == "GET":
        return JsonResponse(product.to_json(), status=200)
    elif request.method == "PUT":
        new_data = json.loads(request.body)
        serializer = ProductSerializer2(instance=product, data=new_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=201)
    elif request.method == "DELETE":
        product.delete()
        return JsonResponse({"message": "Product deleted"})
        


    
def categories_list(request):
     categories = Category.objects.all()
     categories_json = [category.to_json() for category in categories]
     return JsonResponse(categories_json, safe=False)

def get_category(request, id):
    try:
        category = Category.objects.get(id=id)
        return JsonResponse(category.to_json(), safe=False)
    except Category.DoesNotExist:
        return JsonResponse({'error': 'Category not found'}, status=404)

def get_products_by_category(request, id):
    try:
        category = Category.objects.get(id=id)
        products = Product.objects.all().filter(category=category)
        products_json = [p.to_json() for p in products]
        return JsonResponse(products_json, safe=False)
    except Category.DoesNotExist:
        return JsonResponse({'error': 'Category not found'}, status=404)