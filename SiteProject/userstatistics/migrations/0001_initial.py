# Generated by Django 2.2 on 2019-05-10 13:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import profiles.customfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', profiles.customfields.IntegerRangeField()),
                ('appraiser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['year'],
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название задачи', max_length=20)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', profiles.customfields.IntegerRangeField()),
                ('quality', models.CharField(choices=[('+', 'Завысил'), ('-', 'Занизил'), ('=', 'Не пошла на третью проверку')], max_length=1)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userstatistics.Job')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userstatistics.Task')),
            ],
            options={
                'ordering': ['score'],
            },
        ),
    ]
