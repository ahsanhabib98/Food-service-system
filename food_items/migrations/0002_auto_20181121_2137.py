# Generated by Django 2.0.5 on 2018-11-21 15:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food_items', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fooditems',
            name='edited_at',
        ),
        migrations.AddField(
            model_name='fooditems',
            name='draft',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='fooditems',
            name='minimum_quantity',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='fooditems',
            name='status',
            field=models.CharField(choices=[('Sold', 'SOLD'), ('Available', 'AVAILABLE')], default=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='fooditems',
            name='provider',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
