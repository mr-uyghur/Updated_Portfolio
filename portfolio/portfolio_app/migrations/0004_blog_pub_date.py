# Generated by Django 2.2.4 on 2021-02-22 02:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0003_auto_20210221_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
