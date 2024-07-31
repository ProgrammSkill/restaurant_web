from django.urls import include, path
from .views import FoodCategoryListView

urlpatterns = [
    path('foods/', FoodCategoryListView.as_view(), name='foods'),
]