# Generated by Django 5.0 on 2023-12-09 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='price',
            fields=[
                ('article', models.IntegerField(max_length=10, primary_key=True, serialize=False)),
                ('product', models.CharField(max_length=100)),
                ('inprice', models.IntegerField(max_length=10)),
                ('price', models.IntegerField(max_length=10)),
                ('unit', models.CharField(max_length=20)),
                ('instock', models.IntegerField(max_length=10)),
                ('desc', models.CharField(max_length=100)),
            ],
        ),
    ]
