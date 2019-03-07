from django.views.generic.base import View
from .models import Goods


class GoodsListView(View):

    def get(self, request):
        """
        通过django的view实现商品列表页
        :param request:
        :return:
        """
        json_list = []
        goods = Goods.objects.all()[:10]
        # for good in goods:
        #     json_dict = {}
        #     json_dict["name"] = good.name
        #     json_dict["category"] = good.category.name
        #     json_dict["market_price"] = good.market_price
        #     json_dict["add_time"] = good.add_time
        #     json_list.append(json_dict)

        # 如果模型的字段很多，使用上述方法手动转换就很麻烦
        # 可使用model_to_dict把模型转化成字段
        # from django.forms.models import model_to_dict
        # for good in goods:
        #     json_dict = model_to_dict(good)
        #     json_list.append(json_dict)

        # 使用django的serializers能够解决上述方法无法将imagefieldfile等类型字段无法序列化问题
        from django.core import serializers
        json_data = serializers.serialize('json', goods)
        import json
        json_data = json.loads(json_data)

        from django.http import HttpResponse, JsonResponse
        # return HttpResponse(json.dumps(json_list), content_type='application/json')
        return JsonResponse(json_data, safe=False)
