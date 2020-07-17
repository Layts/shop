from django.urls import path
from .views import (item_list, manage_items,
                    item_new, view_items, add_to_cart,
                    remove_from_cart, OrderSummaryView,
                    ItemDetailView)


app_name = 'core'
urlpatterns = [
    path('', item_list, name='item-list'),
    path('manage/', manage_items, name='manage'),
    path('item/new/', item_new, name='item_new'),
    path('products', view_items, name='view_items'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('box/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='item'),
]
