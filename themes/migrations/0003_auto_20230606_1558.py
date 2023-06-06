# Generated by Django 3.2 on 2023-06-06 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('themes', '0002_auto_20230606_1549'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companysetup',
            old_name='logo',
            new_name='header_logo',
        ),
        migrations.AddField(
            model_name='companysetup',
            name='footer_logo',
            field=models.ImageField(blank=True, null=True, upload_to='company_images/'),
        ),
    ]
