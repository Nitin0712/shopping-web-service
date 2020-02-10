# Generated by Django 2.2.7 on 2019-12-16 07:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('product_price', models.FloatField()),
                ('product_image', models.ImageField(upload_to='images/')),
                ('product_createddate', models.DateTimeField(auto_now_add=True)),
                ('product_updateddate', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='product_quantity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_qnt_keep', models.IntegerField()),
                ('pro_qnt_in', models.IntegerField()),
                ('pro_qnt_out', models.IntegerField()),
                ('pro_createddate', models.DateTimeField(auto_now_add=True)),
                ('pro_updateddate', models.DateTimeField(auto_now=True)),
                ('pro_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application1.product')),
            ],
            options={
                'db_table': 'product_quantity',
            },
        ),
        migrations.CreateModel(
            name='product_cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_quantity', models.IntegerField()),
                ('cart_createddate', models.DateTimeField(auto_now_add=True)),
                ('cart_updateddate', models.DateTimeField(auto_now=True)),
                ('cart_productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application1.product')),
                ('cart_usr_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'product_cart',
            },
        ),
    ]