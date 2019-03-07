from .serializers import GoodsSerializer
from rest_framework.views import APIView, status
from rest_framework.response import Response

from .models import Goods


# Create your views here.
class GoodsListView(APIView):

    """
    List all goods
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