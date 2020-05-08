from django.urls import path
from .import views

urlpatterns = [
    path('product_info/<product_id>/', views.product_info,
         name='product_info'),
    path('add_product/', views.add_product, name='add_product'),
    path('product_admin/', views.product_admin, name='product_admin'),
]
