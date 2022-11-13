from rest_framework.response import Response
from django.http import Http404, JsonResponse
from rest_framework.views import APIView

from store.models import Product

from .serializers import DummySerializer, ProductsResponseSerializer
from .services import build_obj_list, build_obj,validate_and_save_data


class DummyView(APIView):
    def get(self, request, *args, **kwargs):
        obj = {
            "message": "Dummy success",
        }
        serializer = DummySerializer(data=obj)
        if serializer.is_valid():
            print("Valido el Serialiers")
            return Response(obj)
        return Response({})


class ProductsView(APIView):

    def get(self, request, *args, **kwargs):
        products = Product.objects.all().order_by("id")
        products_list = build_obj_list(products)
        serializer = ProductsResponseSerializer(products_list, many=True)
        return Response({"products": serializer.data})

class ProductView(APIView):
    def get_product(self, product_id):
        try:
            return Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            raise Http404 from None

    def get(self, request, product_id, *args, **kwargs):
        product = self.get_product(product_id)
        product_obj = build_obj(product)
        serializer = ProductsResponseSerializer(product_obj)
        return Response(serializer.data)

class StoresView(APIView):

    def get(self, request, *args, **kwargs):
        return Response({"Information": "This is the stores view"})

    def post(self, request, *args, **kwargs):
        response = validate_and_save_data(request)
        return response
class ListsView(APIView):
    def get_products(self, product_id):
        try:
            return Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return None

    def get(self, request, *args, **kwargs):
        products_type= request.GET.get('products', None)
        
        if products_type:
            products_type = products_type.split(',')
            liquidos_list = []
            lider_list = []
            jumbo_list = []
            mix_list = []
            for p_type in products_type:
                try:
                    p1 = Product.objects.all().filter(store_id=1, type=p_type).order_by("price").first()
                    p1 = build_obj(p1)
                    liquidos_list.append(p1)
                except Product.DoesNotExist:
                    pass
                try:
                    p2 = Product.objects.all().filter(store_id=2, type=p_type).order_by("price").first()
                    p2 = build_obj(p2)
                    lider_list.append(p2)
                except Product.DoesNotExist:
                    pass
                try:
                    p3 = Product.objects.all().filter(store_id=3, type=p_type).order_by("price").first()
                    p3 = build_obj(p3)
                    jumbo_list.append(p3)
                except Product.DoesNotExist:
                    pass
                
            for i in range(len(liquidos_list)):
                lista = [liquidos_list[i], lider_list[i], jumbo_list[i]]
                sorted_list = sorted(lista, key=lambda x: x['price'])
                mix_list.append(sorted_list[0])

            liquidos_serializer = ProductsResponseSerializer(liquidos_list, many=True)
            lider_serializer = ProductsResponseSerializer(lider_list, many=True)
            jumbo_serializer = ProductsResponseSerializer(jumbo_list, many=True)
            mix_serializer = ProductsResponseSerializer(mix_list, many=True)
            return Response({"Information": "This is the optimized list view", "Liquidos": liquidos_serializer.data, "Lider": lider_serializer.data, "Jumbo": jumbo_serializer.data,"Mix": mix_serializer.data})
        return Response({"Information": "Please select what products you want to compare"})
class ListView(APIView):

    def get(self, request, *args, **kwargs):

        coronas = Product.objects.filter(type="c-corona").order_by("price")
        coronas_list = build_obj_list(coronas)
        corona_serialize = ProductsResponseSerializer(coronas_list, many=True)

        alto = Product.objects.filter(type="p-alto").order_by("price")
        alto_list = build_obj_list(alto)
        alto_serialize = ProductsResponseSerializer(alto_list, many=True)

        jack = Product.objects.filter(type="w-jack").order_by("price")
        jack_list = build_obj_list(jack)
        jack_serialize = ProductsResponseSerializer(jack_list, many=True)

        royal = Product.objects.filter(type="c-royal").order_by("price")
        royal_list = build_obj_list(royal)
        royal_serialize = ProductsResponseSerializer(royal_list, many=True)

        mistral = Product.objects.filter(type="p-mistral").order_by("price")
        mistral_list = build_obj_list(mistral)
        mistral_serialize = ProductsResponseSerializer(mistral_list, many=True)

        return Response({"Information": "This is the cheapest list view", "Corona": corona_serialize.data[0], "Alto del Carmen": alto_serialize.data[0], "Jack Daniels": jack_serialize.data[0], "Royal": royal_serialize.data[0], "Mistral": mistral_serialize.data[0]})
        
# class CategoryView(APIView, PageNumberPagination):
#     page_size = 40

#     def get_category(self, category):
#         try:
#             return Category.objects.get(name=category)
#         except Category.DoesNotExist:
#             raise Http404 from None

#     def get(self, request, category, *args, **kwargs):
#         category_obj = self.get_category(category.title())
#         products = Product.objects.filter(category_id=category_obj).order_by("id")
#         results = self.paginate_queryset(products, request, view=self)
#         products_list = build_obj_list(results)
#         serializer = ProductResponseSerializer(products_list, many=True)
#         return self.get_paginated_response(serializer.data)


# class ProductView(APIView):
#     def get_product(self, product_id):
#         try:
#             return Product.objects.get(pk=product_id)
#         except Product.DoesNotExist:
#             raise Http404 from None

#     def get(self, request, product_id, *args, **kwargs):
#         product = self.get_product(product_id)
#         related_products = Product.objects.filter(category_id=product.category_id).exclude(id=product.id)
#         recommended_products = sorted(related_products, key=lambda p: p.price())[:5]
#         product_obj = build_obj(product)
#         product_obj["recommended_products"] = build_obj_list(recommended_products)
#         serializer = ProductResponseSerializer(product_obj)
#         return Response(serializer.data)


# class UpdateProductsView(APIView):
#     def post(self, request, *args, **kwargs):
#         response = validate_and_save_data(request)
#         return response


# class FilterProductsView(APIView, PageNumberPagination):
#     page_size = 40

#     def get_by_keyword(self, keyword, *args, **kwargs):
#         products = Product.objects.all()
#         try:
#             return products.filter(name__icontains=keyword)
#         except Product.DoesNotExist:
#             raise Http404 from None

#     def get_by_category(self, category, *args, **kwargs):
#         products = Product.objects.all()
#         try:
#             return products.filter(category_id__name=category)
#         except Product.DoesNotExist:
#             raise Http404 from None

#     def get(self, request, *args, **kwargs):
#         keyword = request.query_params.get("keyword")
#         filtered_products = self.get_by_keyword(keyword)
#         products_by_category = self.get_by_category(keyword)
#         set_keyword = set(filtered_products)
#         set_category = set(products_by_category)
#         set_final = set_keyword.union(set_category)
#         if len(set_final) > 0:

#             results = self.paginate_queryset(list(set_final), request, view=self)
#             products_list = build_obj_list(results)
#             serializer = ProductResponseSerializer(products_list, many=True)
#             return self.get_paginated_response(serializer.data)
#         raise Http404 from None


# class NonPaginateProductsView(APIView):
#     def get(self, request, *args, **kwargs):
#         products = Product.objects.all().order_by("id")
#         products_list = build_obj_list(products)
#         serializer = ProductResponseSerializer(products_list, many=True)
#         return Response(serializer.data)


# class NonPaginateFilterProductsView(APIView):
#     def get_by_keyword(self, keyword, *args, **kwargs):
#         products = Product.objects.all()
#         try:
#             return products.filter(name__icontains=keyword)
#         except Product.DoesNotExist:
#             raise Http404 from None

#     def get_by_category(self, category, *args, **kwargs):
#         products = Product.objects.all()
#         try:
#             return products.filter(category_id__name=category)
#         except Product.DoesNotExist:
#             raise Http404 from None

#     def get(self, request, *args, **kwargs):
#         keyword = request.query_params.get("keyword")
#         filtered_products = self.get_by_keyword(keyword)
#         products_by_category = self.get_by_category(keyword)
#         set_keyword = set(filtered_products)
#         set_category = set(products_by_category)
#         set_final = set_keyword.union(set_category)
#         if len(set_final) > 0:
#             products_list = build_obj_list(list(set_final))
#             serializer = ProductResponseSerializer(products_list, many=True)
#             return Response(serializer.data)
#         raise Http404 from None
