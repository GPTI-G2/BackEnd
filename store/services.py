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


