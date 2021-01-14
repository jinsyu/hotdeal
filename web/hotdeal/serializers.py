
from rest_framework import serializers
from .models import Deal


class DealSerializers(serializers.ModelSerializer):
    class Meta:
        model = Deal
        fields = ('__all__')
