# Generated by Django 2.2 on 2019-04-28 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20190428_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='Введите название категории', max_length=20),
        ),
    ]
