from rest_framework import serializers

from goods.models import Goods, GoodsCategory


class CategorySerializer3(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = '__all__'


class CategorySerializer2(serializers.ModelSerializer):
    sub_cat = CategorySerializer3(many=True)

    class Meta:
        model = GoodsCategory
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    sub_cat = CategorySerializer2(many=True)

    class Meta:
        model = GoodsCategory
        fields = '__all__'
        depth = 3


# class GoodsSerializer(serializers.Serializer):
class GoodsSerializer(serializers.ModelSerializer):

    # name = serializers.CharField(required=True, max_length=100)
    # click_num = serializers.IntegerField(default=0)
    # goods_front_image = serializers.ImageField()

    def create(self, validated_data):
        """
        用校验后的数据validated_data创建一个新的对应模型类对象
        """
        return Goods.objects.create(**validated_data)

    # 定义序列化器时，这样一个字段一个字段的定义很麻烦，可以使用模型序列化器
    class Meta:
        model = Goods
        # 通过fields属性指明模型类的哪些字段需要序列化
        # 通过__all__指明所有字段，默认外键字段的值是外键值
        # 可以手动覆盖，使其显示外键对象的完整属性
        fields = '__all__'
        # 使用depth属性可以方便的实现序列化器的嵌套
        depth = 1
    # 自定义外键字段的序列化器，使其显示外键关联对象的完整属性
    # category = CategorySerializer()

