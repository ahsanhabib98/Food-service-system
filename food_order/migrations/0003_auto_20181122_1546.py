# Generated by Django 2.0.5 on 2018-11-22 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food_users_profile', '0001_initial'),
        ('food_order', '0002_auto_20181122_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='role',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='food_users_profile.Profile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='client_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_order.Client'),
        ),
    ]