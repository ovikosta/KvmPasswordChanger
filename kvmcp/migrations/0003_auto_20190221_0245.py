# Generated by Django 2.1.5 on 2019-02-20 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kvmcp', '0002_kvminfo_end_access'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kvminfo',
            name='end_access',
            field=models.DateTimeField(null=True),
        ),
    ]