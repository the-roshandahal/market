# Generated by Django 3.2 on 2023-06-06 09:00

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('themes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('email', models.CharField(max_length=1000)),
                ('subject', models.CharField(max_length=1000)),
                ('contact', models.CharField(max_length=1000)),
                ('message', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PrivacyAndTerms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_set', models.CharField(max_length=100)),
                ('privacy_policy', models.TextField()),
                ('terms_and_condition', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SitemapEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('priority', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_set', models.CharField(max_length=100)),
                ('home_meta_title', models.CharField(max_length=255)),
                ('home_meta_description', models.TextField()),
                ('home_meta_keywords', models.TextField()),
                ('about_meta_title', models.CharField(max_length=255)),
                ('about_meta_description', models.TextField()),
                ('about_meta_keywords', models.TextField()),
                ('contact_meta_title', models.CharField(max_length=255)),
                ('contact_meta_description', models.TextField()),
                ('contact_meta_keywords', models.TextField()),
                ('blogs_meta_title', models.CharField(max_length=255)),
                ('blogs_meta_description', models.TextField()),
                ('blogs_meta_keywords', models.TextField()),
                ('themes_meta_title', models.CharField(max_length=255)),
                ('themes_meta_description', models.TextField()),
                ('themes_meta_keywords', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_token', models.CharField(max_length=105, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseSummary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=100, unique=True)),
                ('discount', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10000000), django.core.validators.MinValueValidator(10)])),
                ('total_amount', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10000000), django.core.validators.MinValueValidator(10)])),
                ('payment_method', models.CharField(blank=True, choices=[('khalti', 'khalti'), ('other', 'other')], default='khalti', max_length=100, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PurchasedTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=100)),
                ('download_count', models.IntegerField()),
                ('purchase_summary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='features.purchasesummary')),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='themes.template')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Downloads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('download_count', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='themes.template')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='themes.template')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]