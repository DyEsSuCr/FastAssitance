# Generated by Django 4.1.2 on 2022-12-06 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='business',
            field=models.ForeignKey(blank=True, default='EMPLOYEE', null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.business'),
        ),
    ]
