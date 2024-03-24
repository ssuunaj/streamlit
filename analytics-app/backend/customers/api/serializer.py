from rest_framework import serializers
from ..models import Customers
from ..choices import GENDER_CHOICES


class GenderChoiceFieldSerializer(serializers.Field):

    def to_representation(self, obj):
        return dict(GENDER_CHOICES)[obj]

    def to_internal_value(self, data):
        return data

class CustomerSerializer(serializers.ModelSerializer):
    gender = GenderChoiceFieldSerializer()
    created = serializers.SerializerMethodField()
    class Meta:
        model = Customers
        fields = (
            'id',
            'name',
            'gender',
            'age',
            'favourite_number',
            'created'
        )

    def get_created(self, obj):
        return obj.created.strftime('%Y-%m-%d %H:%M:%S')
