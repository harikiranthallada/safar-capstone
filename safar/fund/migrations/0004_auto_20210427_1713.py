# Generated by Django 3.1.7 on 2021-04-27 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fund', '0003_auto_20210422_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='admin_msg',
            field=models.CharField(blank=True, default='none', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.CharField(blank=True, choices=[('PENDING', 'PENDING'), ('ACCEPTED', 'ACCEPTED'), ('CANCELLED', 'CANCELLED'), ('COMPLETED', 'COMPLETED')], default='PENDING', max_length=50),
        ),
    ]
