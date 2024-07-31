from django.db.models import Prefetch
from rest_framework.generics import ListAPIView
from v1.models import FoodListSerializer, FoodCategory, Food


class FoodCategoryListView(ListAPIView):
    serializer_class = FoodListSerializer

    def get_queryset(self):
        published_food = Food.objects.filter(is_publish=True)
        return FoodCategory.objects.prefetch_related(Prefetch('food', queryset=published_food)).filter(
            food__is_publish=True).distinct()