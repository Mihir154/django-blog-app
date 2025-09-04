from django.urls import path
from .views import *

urlpatterns = [
    path('<int:category_id>', category_posts, name='category_posts')
]
