# Generated by Django 2.2.12 on 2022-02-28 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='未查看', max_length=5, unique=True, verbose_name='工单状态')),
            ],
            options={
                'verbose_name': '工单状态',
                'verbose_name_plural': '工单状态',
                'db_table': 'goods_status',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createtime', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('number', models.CharField(default='G20220228233932', max_length=15, unique=True, verbose_name='工单编号')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('content', models.TextField(verbose_name='工单内容')),
                ('goods_type', models.CharField(default='物流问题', max_length=10, verbose_name='问题类型')),
                ('other', models.TextField(default='无', verbose_name='备注')),
                ('clent_name', models.CharField(default='无', max_length=20, verbose_name='收货人')),
                ('goods_name', models.CharField(default='无', max_length=100, verbose_name='物品名')),
                ('goods_count', models.IntegerField(default=-1, verbose_name='下单数量')),
                ('wuliu_number', models.CharField(default='无', max_length=50, verbose_name='物流单号')),
                ('buy_date', models.DateField(default='2000-1-1', verbose_name='下单日期')),
                ('comment', models.TextField(default='暂无处理意见..', verbose_name='处理意见')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否激活')),
                ('c_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='c_user', to='user.User')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='goods.Status')),
                ('t_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='t_user', to='user.User')),
            ],
            options={
                'verbose_name': '工单',
                'verbose_name_plural': '工单',
                'db_table': 'goods',
            },
        ),
    ]