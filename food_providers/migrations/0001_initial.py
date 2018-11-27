# Generated by Django 2.0.5 on 2018-11-18 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('food_area', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CooKInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cook_name', models.CharField(max_length=100)),
                ('cook_image', models.ImageField(upload_to='images')),
                ('contact_no', models.PositiveIntegerField()),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_area.Area')),
            ],
        ),
    ]
