# Generated by Django 2.2.1 on 2019-05-26 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_type',
            field=models.CharField(choices=[(1, 'Fakturowania'), (2, 'Dostawy'), (3, 'Siedziba')], max_length=40),
        ),
    ]