# Generated by Django 2.2.4 on 2021-03-01 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0004_blog_pub_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='summary',
            new_name='title',
        ),
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.TextField(default=True, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='image_2',
            field=models.ImageField(default=True, upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='image_3',
            field=models.ImageField(default=True, upload_to='images/'),
            preserve_default=False,
        ),
    ]
