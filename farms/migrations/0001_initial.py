# Generated by Django 3.2 on 2021-04-21 19:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Farms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farm_name', models.CharField(blank=True, max_length=200)),
                ('recorded_by', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Telephone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phonenumber', models.CharField(max_length=200)),
                ('farms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farms.farms')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_name', models.CharField(blank=True, max_length=200)),
                ('street_no', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('country', models.CharField(choices=[('Nig', 'Nigeria'), ('AF', 'Afghanistan'), ('AL', 'Albania'), ('DZ', 'Algeria'), ('AX', 'Aland'), ('AS', 'American'), ('AI', 'Anguilla'), ('AD', 'Andorra'), ('AO', 'Angola'), ('AN', ' Antilles - Netherlands')], default='Nig', max_length=200)),
                ('farms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farms.farms')),
            ],
        ),
    ]
