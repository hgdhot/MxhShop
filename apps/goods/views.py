# from rest_framework.views import APIView, status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import pagination
from rest_framework import viewsets

from .serializers import GoodsSerializer
from .models import Goods


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
class GoodsViewSet(viewsets.ModelViewSet):
    """
    商品列表页
    """
    """
    def get(self, request, format=None):
        goods = Goods.objects.all()[:10]
        goods_serializer = GoodsSerializer(goods, many=True)
        return Response(goods_serializer.data)

    def post(self, request, format=None):
        # 此处的request对象时drf框架封装的
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
    queryset = Goods.objects.all()
    pagination_class = GoodsPagination

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)
