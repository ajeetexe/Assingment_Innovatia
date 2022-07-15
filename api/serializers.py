from rest_framework import serializers
from .models import RechargeHistroy


class RechargeSerializers(serializers.ModelSerializer):
    class Meta:
        model = RechargeHistroy
        fields = '__all__'