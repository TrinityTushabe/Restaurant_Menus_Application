# Generated by Django 3.0.8 on 2023-10-28 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_menu_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=255),
        ),
    ]