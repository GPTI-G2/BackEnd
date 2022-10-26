from django.urls import path
from .views import (
    DummyView,
    ProductsView,
    ProductView,
    StoresView,
    ListsView
)

urlpatterns = [
    path("dummy/", DummyView.as_view()),
    path("products/", ProductsView.as_view()),
    path("products/<int:product_id>", ProductView.as_view()),
    path("stores/", StoresView.as_view()),
    path("lists/", ListsView.as_view()),

]
