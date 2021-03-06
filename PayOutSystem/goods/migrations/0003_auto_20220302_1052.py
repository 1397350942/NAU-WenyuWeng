# Generated by Django 2.2.12 on 2022-03-02 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20220301_0001'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='endtime',
            field=models.DateTimeField(auto_now=True, verbose_name='最后修改时间'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='createtime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='number',
            field=models.CharField(default='G20220302105209', max_length=15, unique=True, verbose_name='工单编号'),
        ),
    ]
