# Generated by Django 2.2 on 2019-04-28 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20190428_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='conflict',
            field=models.CharField(choices=[('да', 'да'), ('нет', 'нет')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='third_check',
            field=models.CharField(choices=[('да', 'да'), ('нет', 'нет')], max_length=3, null=True),
        ),
    ]
