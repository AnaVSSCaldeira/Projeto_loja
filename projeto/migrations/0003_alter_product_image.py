# Generated by Django 3.2.13 on 2022-05-18 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projeto', '0002_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]