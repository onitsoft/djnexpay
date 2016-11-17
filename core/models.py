from django.db import models
from django.conf import settings
from django.utils.crypto import get_random_string

#from core.settings import UNIQUE_REFERENCE_LENGTH, REFERENCE_LOOKUP_ATTEMPTS

# Create your models here.

from safedelete import safedelete_mixin_factory, SOFT_DELETE, \
    DELETED_VISIBLE_BY_PK, safedelete_manager_factory, DELETED_INVISIBLE

SoftDeleteMixin = safedelete_mixin_factory(policy=SOFT_DELETE,
                                           visibility=DELETED_VISIBLE_BY_PK)


class UniqueFieldMixin(models.Model):

    class Meta:
        abstract = True

    @staticmethod
    def gen_unique_value(val_gen, set_len_gen, start_len):
        failed_count = 0
        max_len = start_len
        while True:
            if failed_count >= settings.REFERENCE_LOOKUP_ATTEMPTS:
                failed_count = 0
                max_len += 1

            val = val_gen(max_len)
            cnt_unq = set_len_gen(val)
            if cnt_unq == 0:
                return val
            else:
                failed_count += 1


class SoftDeletableModel(SoftDeleteMixin):
    disabled = models.BooleanField(default=False)
    active_objects = safedelete_manager_factory(
        models.Manager, models.QuerySet, DELETED_INVISIBLE)()

    class Meta:
        abstract = True


class TimeStampedModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BankManager(models.Manager):

    def get_by_natural_key(self, code):
        return self.get(code=code)


class Bank(TimeStampedModel, SoftDeletableModel):
    objects = BankManager()
    code = models.CharField(max_length=4)
    name = models.CharField(max_length=15)

    def natural_key(self):
        return self.code

    def __str__(self):
        return self.name


class OrderManager(models.Manager):

    def get_by_natural_key(self, order_number):
        return self.get(order_number=order_number)


class Order(TimeStampedModel, SoftDeletableModel, UniqueFieldMixin):
    objects = OrderManager()
    order_number = models.CharField(
        max_length=settings.UNIQUE_REFERENCE_LENGTH, unique=True)
    amount_gross = models.DecimalField(max_digits=12, decimal_places=2)
    comission = models.DecimalField(max_digits=12, decimal_places=2)
    amount_net = models.DecimalField(max_digits=12, decimal_places=2)
    bank = models.ForeignKey(Bank)
    cbu_number = models.CharField(max_length=22)
    account_number = models.CharField(max_length=15)
    account_owner = models.CharField(max_length=20)
    account_owner_dni = models.CharField(max_length=12)
    paypal_email = models.CharField(max_length=50)
    tracking_email = models.CharField(max_length=50)
    is_paid = models.BooleanField(default=False)
    is_released = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    is_failed = models.BooleanField(default=False)

    def natural_key(self):
        return self.order_number

    def save(self, *args, **kwargs):

        self.order_number = \
            self.gen_unique_value(
                lambda x: get_random_string(x),
                lambda x: Order.objects.filter(order_number=x).count(),
                settings.UNIQUE_REFERENCE_LENGTH
            )

        super(Order, self).save(*args, **kwargs)
