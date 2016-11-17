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

from core.models import Bank, Order
from core.serializers import OrderSerializer
# Create your views here.

# TODO:

EXCHANGE_RATE = float(15)

# def main(request):
#     template = get_template('core/index.html')
#     _messages = []
#     ctx = {'messages': _messages}
#     return HttpResponse(template.render(ctx, request))


# def ajax_order(request):
#     _messages = []
#     # TODO: rate must be dynamic
#     # TODO: FLoat values below also must be dynamic
#     #       in case paypal raises its prices or something
#     EXCHANGE_RATE = float(15)
#     if request.POST:
#         amount = request.POST.get("monto", None)
#         bank = request.POST.get("banco", None)
#         cbu = request.POST.get("cbu", None)
#         account = request.POST.get("ncuenta", None)
#         owner = request.POST.get("titular", None)
#         dni = request.POST.get("dni", None)
#         email = request.POST.get("email", None)
#         track_email = request.POST.get("emailalternativo", None)

#         bank_instance = Bank.objects.filter(code=bank)[0]

#         # TODO: This process can be moved to model
#         comission = float(amount) * float(0.054) + float(0.3)
#         amount_net = ((float(amount) - comission) * EXCHANGE_RATE) * 0.85

#         order = Order(
#             amount_gross=amount,
#             comission=comission,
#             amount_net=amount_net,
#             bank=bank_instance,
#             cbu_number=cbu,
#             account_number=account,
#             account_owner=owner,
#             account_owner_dni=dni,
#             paypal_email=email,
#             tracking_email=track_email,
#         )

#         order.save()
#         # uniq_ref = payment.unique_reference

#     else:
#         _messages.append("Invalid Method")
#         raise Http404("Invalid Method")

#     ctx = {'status': 'OK'}

#     return JsonResponse(ctx, safe=False)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'orders': reverse('order-list', request=request, format=format),
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
        amount = self.request.data['amount_gross']
        comission = float(amount) * float(0.054) + float(0.3)
        amount_net = ((float(amount) - comission) * EXCHANGE_RATE) * 0.85
        serializer.save(
            bank=bank_instance,
            comission=comission,
            amount_net=amount_net)
