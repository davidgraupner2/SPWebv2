# Generated by Django 3.1.1 on 2020-09-04 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenant',
            name='subdomain_prefix',
            field=models.CharField(default='Test', max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
