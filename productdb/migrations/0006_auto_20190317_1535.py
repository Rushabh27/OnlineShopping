# Generated by Django 2.1.7 on 2019-03-17 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productdb', '0005_auto_20190314_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='url',
            field=models.CharField(max_length=100),
        ),
    ]
