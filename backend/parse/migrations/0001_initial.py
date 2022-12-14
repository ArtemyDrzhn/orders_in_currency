# Generated by Django 4.0.7 on 2022-09-12 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ordering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(verbose_name='№')),
                ('order_number', models.PositiveBigIntegerField(verbose_name='заказ №')),
                ('cost_dollars', models.PositiveIntegerField(verbose_name='стоимость,$')),
                ('delivery_date', models.DateField(verbose_name='срок поставки')),
                ('cost_rubles', models.FloatField(verbose_name='стоимость,₽')),
            ],
        ),
    ]
