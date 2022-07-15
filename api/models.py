from uuid import uuid5
from django.db import models
import uuid
# Create your models here.

class RechargeHistroy(models.Model):
    mobile_number = models.CharField(max_length=12)
    price = models.IntegerField()
    operator_name = models.CharField(max_length=255)
    recharge_on = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=255,default=str(uuid.uuid5(uuid.NAMESPACE_DNS,'python.org')))

    def __str__(self):
        return self.mobile_number