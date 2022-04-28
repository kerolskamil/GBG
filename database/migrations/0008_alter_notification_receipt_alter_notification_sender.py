# Generated by Django 4.0.4 on 2022-04-27 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0007_alter_friendship_receiver_alter_friendship_sender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='receipt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='receipt', to='database.user'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='sender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='senderr', to='database.user'),
        ),
    ]
