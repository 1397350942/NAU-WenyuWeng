# Generated by Django 4.0.4 on 2022-05-14 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0011_auto_20220312_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='number',
            field=models.CharField(default='G20220514170445', max_length=18, unique=True, verbose_name='工单编号'),
        ),
        migrations.AlterField(
            model_name='status',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
