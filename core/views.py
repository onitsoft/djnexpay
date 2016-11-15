from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseForbidden
from core.models import Bank
# Create your views here.


def main(request):
    template = get_template('core/index.html')
    banks = Bank.objects.all()
    _messages = []
    return HttpResponse(template.render({'messages': banks}, request))
