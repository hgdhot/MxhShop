# from rest_framework.views import APIView, status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import pagination
from rest_framework import viewsets
from rest_framework import filters

from django_filters.rest_framework import DjangoFilterBackend

from .serializers import GoodsSerializer, CategorySerializer
from .models import Goods, GoodsCategory
from .filters import GoodFilter


# Create your views here.
class GoodsPagination(pagination.PageNumberPagination):
    # 默认单页记录数
    page_size = 10
    # 客户端可以通过此参数指定的值设置查询第几页
    page_query_param = 'p'
    # 客户端可以通过此参数指定的值设置单页显示记录数
    page_size_query_param = 'page_size'
    # 控制客户端能够设定的单页最大记录数
    max_page_size = 100


# class GoodsListView(APIView):
# class GoodsListView(mixins.ListModelMixin, generics.GenericAPIView):
# class GoodsListView(generics.ListAPIView):
class GoodsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    商品列表页，实现商品的分页、搜索、过滤、排序
    """
    """
    def get(self, request, format=None):
        goods = Goods.objects.all()[:10]
        goods_serializer = GoodsSerializer(goods, many=True)
        return Response(goods_serializer.data)

    def post(self, request, format=None):
        # 此处的request对象是drf框架封装的
        # 会把django的request对象中的GET/POST等请求参数都放到data属性中
        serializer = GoodsSerializer(data=request.data)
        # 序列化器可以用来做校验
        if serializer.is_valid():
            # 序列化器可以用来将请求数据保存到数据库中（类似于django的forms）
            serializer.save()
            # 在rest_framework.views中的status模块中定义了很多标准响应码
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    """
    serializer_class = GoodsSerializer
    # 查询所有商品，按商品售价倒序（从高到低）排列
    queryset = Goods.objects.all().order_by('-shop_price')
    pagination_class = GoodsPagination
    # 过滤所用的配置
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # filter_fields = ('name', 'shop_price')
    filterset_class = GoodFilter
    search_fields = ('^name', '^goods_brief', '^goods_desc')
    ordering_fields = ('shop_price', 'market_price')

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)

    # 最基础的过滤的方式，定义了此方法就不用定义queryset属性了
    # def get_queryset(self):
    #     # 只有在第一次使用此查询集中的数据时才会真正发生数据库查询
    #     queryset = Goods.objects.all()
    #     price_min = self.request.query_params.get('price_min', 0)
    #     if price_min:
    #         queryset = queryset.filter(shop_price__gt=int(price_min))
    #     return queryset


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        商品分类列表数据
    retrieve:
        获取某一商品分类的信息，访问方式是标准的REST方式，如/goods/categorys/categoryid
    """
    serializer_class = CategorySerializer
    queryset = GoodsCategory.objects.filter(category_type=1)
