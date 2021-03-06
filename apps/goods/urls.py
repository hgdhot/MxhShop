from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views_base import GoodsListView

from .views import GoodsViewSet, CategoryViewSet

# goods_list = GoodsListViewSet.as_view({
#     'get': 'list',
#     'post': 'create',
# })

# 通过Router来注册视图集，就不用向上面那样来显式地
# 将不同请求方式（GET、POST）所对应的操作（Action）进行绑定
router = DefaultRouter()
# 配置goods的url
router.register(r'goods', GoodsViewSet, base_name="goods")
router.register(r'categorys', CategoryViewSet, base_name="categorys")


# urlpatterns = [
#     # path('', GoodsListView.as_view(), name='goods-list'),
#     path('', goods_list, name='goods-list'),
# ]

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
