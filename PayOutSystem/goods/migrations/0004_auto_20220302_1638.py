# Generated by Django 2.2.12 on 2022-03-02 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_auto_20220302_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='number',
            field=models.CharField(default='G20220302163854', max_length=15, unique=True, verbose_name='工单编号'),
        ),
    ]
