# Generated by Django 4.2.3 on 2024-01-28 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks_service', '0004_stock_price_stock_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('ticker', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
