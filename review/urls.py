from django.urls import path
from .import views

urlpatterns = [
    path('get_reviews/', views.get_reviews, name='get_reviews'),
    path('create_review/<product_id>', views.create_or_edit_review,
         name='create_review'),
    path('edit_review/<product_id>', views.create_or_edit_review,
         name='edit_review'),
    path('review_delete/<pk>', views.review_delete, name='review_delete')
]