from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from django.http import Http404

from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics

from core.models import Bank, Order, Parameter
from core.serializers import OrderSerializer, ParameterSerializer
# Create your views here.


EXCHANGE_RATE = float(15)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'orders': reverse('order-list', request=request, format=format),
        'parameters': reverse('parameters-list', request=request, format=format),
    })


class OrderViewSet(viewsets.ModelViewSet):
    """
    This endpoint presents orders.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    #permission_classes = (permissions.IsAuthenticated,IsOwner,)

    def perform_create(self, serializer):
        bank_instance = Bank.objects.filter(code=self.request.data['bank'])[0]
        parameters = Parameter.objects.all()[0]
        paypal_pct = float(parameters.paypal_pct)
        paypal_fee = float(parameters.paypal_fee)
        nexpay_pct = float(parameters.nexpay_pct)
        exchange_rate = float(parameters.exchange_rate)
        amount = self.request.data['amount_gross']
        comission = round(float(amount) * paypal_pct + paypal_fee, 2)
        amount_net = round(
            ((float(amount) - comission) * exchange_rate) * nexpay_pct)
        serializer.save(
            bank=bank_instance,
            comission=comission,
            amount_net=amount_net)


class ParameterViewSet(viewsets.ModelViewSet):
    """
    This endpoint presents parameters.
    """
    queryset = Parameter.objects.all()[:1]
    serializer_class = ParameterSerializer
