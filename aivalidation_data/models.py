from django.db import models
from django.utils import timezone

# Create your models here.

class Patient(models.Model):
    """ 病人信息

    """
    name = models.CharField(
        max_length=10,
        db_column='name',
        null=True,
        blank=True
    )
    birthday = models.DateField(
        db_column='birthday',
        null=True,
        blank=True
    )
    create_time = models.DateTimeField(
        db_column='create_time',
        default=timezone.now,
        null=True,
        blank=True
    )
    # modified_by = models.IntegerField(
    #     db_column='modifiedBy',
    #     null=True,
    #     blank=True
    # )
    # modified_time = models.DateTimeField(
    #     db_column='modified_time',
    #     auto_now=True,
    #     null=True,
    #     blank=True
    # )

class Item(models.Model):
    """ 检测项
    """
    item_code_lis = models.CharField(
        'lis_code',
        max_length=10,
        db_column='item_code',
        null=True,
        blank=True
    )
    item_code_middleware = models.CharField(
        'infinity_code',
        max_length=10,
        db_column='item_code_lis',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ['-id']


class ItemRange(models.Model):
    """ 检测项范围

    """
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    max_range = models.FloatField()
    min_range = models.FloatField()


class TestItem(models.Model):
    item_code = models.CharField


class Order(models.Model):
    """ 检验申请单，来自于lis

    """
    order_id = models.CharField('申请单id', max_length=30, db_column='order_id')
    command_identifier = models.IntegerField('消息类型，创建: NW，撤销: CA，更改: XO', db_column='command_identifier')
    patient = models.ForeignKey(Patient, verbose_name='病人', on_delete=models.CASCADE)
    diagnosis = models.CharField('诊断', max_length=200, db_column='diagnosis')
    encounter_type = models.CharField('就诊类型', max_length=10, db_column='encounter_type')
    department = models.CharField('就诊科室', max_length=200, db_column='department')
    test_items = models.ForeignKey(Item, verbose_name='检测项')


class InfinityData(models.Model):
    """ 检验结果单，来自于infinity

    """
    order_id = models.CharField('申请单id', max_length=30, db_column='order_id')








