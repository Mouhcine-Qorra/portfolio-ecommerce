# Generated by Django 3.2.5 on 2021-09-27 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_auto_20210927_0242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingadress',
            name='phone',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
