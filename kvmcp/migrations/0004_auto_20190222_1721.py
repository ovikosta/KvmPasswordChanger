# Generated by Django 2.1.5 on 2019-02-22 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kvmcp', '0003_auto_20190221_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kvminfo',
            name='end_access',
            field=models.TimeField(null=True),
        ),
    ]