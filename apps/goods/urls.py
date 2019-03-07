from django.urls import path, include
# from .views_base import GoodsListView
from .views import GoodsListView

urlpatterns = [
    path('', GoodsListView.as_view(), name='goods-list')
]
