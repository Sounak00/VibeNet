# Generated by Django 5.2.2 on 2025-06-05 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0002_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='post_images/'),
        ),
    ]
