from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from core.models import Bank, Order
from core.forms import DateSearchForm, OrderForm
# Create your views here.


def main(request):
    template = get_template('core/index.html')
    _messages = []
    ctx = {'messages': _messages}
    return HttpResponse(template.render(ctx, request))


def ajax_order(request):
    _messages = []
    # TODO: rate must be dynamic
    # TODO: FLoat values below also must be dynamic
    #       in case paypal raises its prices or something
    EXCHANGE_RATE = float(15)
    if request.POST:
        amount = request.POST.get("monto", None)
        bank = request.POST.get("banco", None)
        cbu = request.POST.get("cbu", None)
        account = request.POST.get("ncuenta", None)
        owner = request.POST.get("titular", None)
        dni = request.POST.get("dni", None)
        email = request.POST.get("email", None)
        track_email = request.POST.get("emailalternativo", None)

        bank_instance = Bank.objects.filter(code=bank)[0]

        # TODO: This process can be moved to model
        comission = float(amount) * float(0.054) + float(0.3)
        print(type(comission), type(amount))
        amount_net = ((float(amount) - comission) * EXCHANGE_RATE) * 0.85

        order = Order(
            amount_gross=amount,
            comission=comission,
            amount_net=amount_net,
            bank=bank_instance,
            cbu_number=cbu,
            account_number=account,
            account_owner=owner,
            account_owner_dni=dni,
            paypal_email=email,
            tracking_email=track_email,
        )

        order.save()
        # uniq_ref = payment.unique_reference

    else:
        _messages.append("Invalid Method")

    ctx = {'status': 'OK'}

    return JsonResponse(ctx, safe=False)
