# Generated by Django 2.2.14 on 2021-05-13 01:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_remove_bobaproduct_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bobaproduct',
            name='image',
        ),
    ]
