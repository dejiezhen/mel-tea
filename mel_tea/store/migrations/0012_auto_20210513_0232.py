# Generated by Django 2.2.14 on 2021-05-13 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_auto_20210513_0230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bobaproduct',
            name='image',
            field=models.ImageField(blank=True, default="{% static 'images/filler.jpg' %}", null=True, upload_to='boba'),
        ),
    ]
