# Generated by Django 2.2.14 on 2021-05-13 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20210513_0229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bobaproduct',
            name='image',
            field=models.ImageField(default="{% static 'images/filler.jpg' %}", null=True, upload_to='boba'),
        ),
    ]
