# Generated by Django 2.0.5 on 2018-11-21 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food_area', '0001_initial'),
        ('food_delivery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_point_name', models.CharField(max_length=100)),
                ('delivery_point_image', models.ImageField(upload_to='images')),
                ('delivery_point_contact_no', models.PositiveIntegerField()),
                ('delivery_point_address', models.CharField(max_length=100)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_area.Area')),
            ],
        ),
        migrations.RemoveField(
            model_name='deliveryperson',
            name='area',
        ),
        migrations.DeleteModel(
            name='DeliveryPerson',
        ),
    ]