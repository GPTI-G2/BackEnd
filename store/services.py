from rest_framework import status
from rest_framework.response import Response
from store.models import Store, Product
from .serializers import ProductPostSerializer

def build_obj_list(queryset):
    obj_list = []
    for product in queryset:
        product_obj = {
            "id": product.id,
            "name": product.name,
            "store": product.store_id.name,
            "sku": product.sku,
            "brand": product.brand,
            "size": product.size,
            "image_url": product.image_url,
            "price": product.price,
            "type": product.type,
        }
        obj_list.append(product_obj)
    return obj_list


def build_obj(product):
    product_obj = {
            "id": product.id,
            "name": product.name,
            "store": product.store_id.name,
            "sku": product.sku,
            "brand": product.brand,
            "size": product.size,
            "image_url": product.image_url,
            "price": product.price,
            "type": product.type,
        }
    return product_obj

def validate_and_save_data(request):
    try:
        store_name = request.data["store"].title()
        products_list = request.data["products_list"]
    except Exception:
        return Response({"message": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        store = Store.objects.get(name=store_name)
    except Exception:
        return Response({"message": "Invalid store"}, status=status.HTTP_400_BAD_REQUEST)

    error_list_products = []
    for product in products_list:
        serializer = ProductPostSerializer(data=product)
        if serializer.is_valid():
            try:
                product_obj = Product.objects.get(sku=product["sku"])
                product_obj.price = product["price"]
                product_obj.save()
            except Product.DoesNotExist:
                product_obj = Product.objects.create(
                    name=serializer.data["name"],
                    store_id=store,
                    sku=serializer.data["sku"],
                    brand=serializer.data["brand"],
                    size=serializer.data["size"],
                    image_url=serializer.data["image_url"],
                    price=serializer.data["price"],
                    type=serializer.data["type"],
                )
                product_obj.save()
        else:
            print(serializer.errors)
            error_list_products.append(product)

    response = {"message": "Information Received", "error_products": error_list_products}
    return Response(response)

