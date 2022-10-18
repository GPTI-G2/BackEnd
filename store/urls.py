from django.urls import path
from .views import (
    DummyView,
    ProductsView,
)

urlpatterns = [
    path("dummy/", DummyView.as_view()),
    path("products/", ProductsView.as_view()),
    # path("v1/products/category/<str:category>", CategoryView.as_view()),
    # path("v1/products/<int:product_id>", ProductView.as_view()),

]
