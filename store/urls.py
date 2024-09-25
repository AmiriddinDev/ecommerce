from django.urls import path

from store.views import store_list_view, product_detail_view

app_name = 'store'
urlpatterns = [
    path('', store_list_view, name='stor_list'),
    path('<slug:slug>/', product_detail_view, name='products_detail'),
]