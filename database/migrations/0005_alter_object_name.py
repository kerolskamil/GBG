# Generated by Django 3.2.8 on 2022-03-30 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_auto_20220330_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='object',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]