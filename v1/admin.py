from django.contrib import admin
from v1.models import FoodCategory, Food


@admin.register(FoodCategory)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['name_ru', 'name_en', 'name_ch', 'order_id']


@admin.register(Food)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['category', 'is_vegan', 'is_special', 'code', 'internal_code', 'name_ru', 'description_ru',
                    'description_en', 'description_ch', 'cost', 'is_publish', 'additional_list']

    def additional_list(self, obj):
        return ", ".join([str(additional_item) for additional_item in obj.additional.all()])

    additional_list.short_description = 'Дополнительные товары'