# Generated by Django 2.1.1 on 2018-10-26 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zappyapp', '0009_auto_20181026_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='image',
            field=models.ImageField(default='Customers/default.jpg', upload_to='Customers'),
        ),
    ]