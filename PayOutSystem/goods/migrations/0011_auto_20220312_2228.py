# Generated by Django 2.2.12 on 2022-03-12 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0010_auto_20220309_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='goods_count',
            field=models.CharField(default='未知', max_length=20, verbose_name='下单数量'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='number',
            field=models.CharField(default='G20220312222848', max_length=18, unique=True, verbose_name='工单编号'),
        ),
    ]
