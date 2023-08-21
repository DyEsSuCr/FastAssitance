# Generated by Django 4.2.4 on 2023-08-21 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='State')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de modificacion')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de eliminacion')),
                ('name', models.CharField(max_length=60, verbose_name='Nombre')),
                ('address', models.CharField(max_length=60, unique=True, verbose_name='Direcciom')),
                ('phone_number', models.CharField(max_length=16, unique=True, verbose_name='Telefono')),
            ],
            options={
                'verbose_name': 'Negocio',
                'verbose_name_plural': 'Negocios',
                'ordering': ['-name'],
            },
        ),
    ]