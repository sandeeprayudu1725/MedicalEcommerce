# Generated by Django 4.0.6 on 2022-07-18 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('product_slug', models.SlugField(max_length=255)),
                ('product_description', models.TextField(blank=True)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('product_image', models.ImageField(blank=True, upload_to='images/')),
                ('product_stock', models.IntegerField(default=0)),
                ('product_available', models.BooleanField(default=True)),
                ('product_created_date', models.DateTimeField(auto_now_add=True)),
                ('product_updated_date', models.DateTimeField(auto_now=True)),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
        ),
    ]