# Generated by Django 2.0.3 on 2018-10-31 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180724_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryinfo',
            name='other_task',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='deliveryinfo',
            name='task_detail',
            field=models.TextField(default=None, max_length=6000, null=True),
        ),
    ]