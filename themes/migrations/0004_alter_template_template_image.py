# Generated by Django 3.2 on 2023-06-07 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('themes', '0003_auto_20230606_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='template_image',
            field=models.ImageField(upload_to='template_images/'),
        ),
    ]