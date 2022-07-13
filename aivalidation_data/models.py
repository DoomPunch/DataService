from django.db import models
from django.utils import timezone

# Create your models here.


class Order(models.Model):
    pass


class InfinityData(models.Model):
    pass


class Item(models.Model):
    item_code_lis = models.CharField(max_length=10, db_column='ItemCodeLis', null=True, blank=True)
    item_code_middleware = models.CharField(max_length=10, db_column='ItemCodeLis', null=True, blank=True)


class ItemRange(models.Model):
    item = models.ForeignKey(Item, on_delete=True)


class Patient(models.Model):
    name = models.CharField(max_length=10, db_column='Name', null=True, blank=True)
    birthday = models.DateField(db_column='Birthday', null=True, blank=True)
    create_time = models.DateTimeField(db_column='CreateTime', default=timezone.now, null=True, blank=True)
    modified_by = models.IntegerField(db_column='ModifiedBy', null=True, blank=True)
    modified_time = models.DateTimeField(db_column='ModifiedTime', auto_now=True, null=True, blank=True)
