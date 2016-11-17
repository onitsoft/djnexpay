from rest_framework import serializers
from core.models import Order


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    bank = serializers.ReadOnlyField(source='bank.name')
    order_number = serializers.SerializerMethodField()
    comission = serializers.SerializerMethodField()
    amount_net = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = (
            'order_number',
            'amount_gross',
            'comission',
            'amount_net',
            'bank',
            'cbu_number',
            'account_number',
            'account_owner',
            'account_owner_dni',
            'paypal_email',
            'tracking_email',
            'is_paid',
            'is_released',
            'is_completed',
            'is_failed')

    def get_order_number(self, obj):
        return obj.order_number

    def get_comission(self, obj):
        return obj.comission

    def get_amount_net(self, obj):
        return obj.amount_net
