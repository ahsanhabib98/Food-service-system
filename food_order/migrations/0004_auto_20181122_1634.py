# Generated by Django 2.0.5 on 2018-11-22 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food_order', '0003_auto_20181122_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='food_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_items.FoodItems'),
        ),
    ]
