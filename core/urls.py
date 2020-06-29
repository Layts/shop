from django.urls import path
from .views import item_list, box, manage_items, item_new


app_name = 'core'
urlpatterns = [
    path('', item_list, name='item-list'),
    path('box', box, name='item-list'),
    path('manage/', manage_items, name='manage'),
    path('item/new/', item_new, name='item_new'),
]
