from django.urls import path
from .views import (
    DummyView,
    ProductsView,
    ProductView,
)

urlpatterns = [
    path("dummy/", DummyView.as_view()),
    path("products/", ProductsView.as_view()),
    path("products/<int:product_id>", ProductView.as_view()),

]
