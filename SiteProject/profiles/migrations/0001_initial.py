# Generated by Django 2.2 on 2019-04-28 12:07

from django.conf import settings
import django.core.validators
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
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Р’РІРµРґРёС‚Рµ РЅР°Р·РІР°РЅРёРµ РєР°С‚РµРіРѕСЂРёРё', max_length=20)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patronymic', models.CharField(help_text='Р’РІРµРґРёС‚Рµ РѕС‚С‡РµСЃС‚РІРѕ', max_length=200, null=True)),
                ('pasport_series', models.CharField(max_length=4, null=True, validators=[django.core.validators.RegexValidator(regex='\\d{4}')])),
                ('pasport_number', models.CharField(max_length=6, null=True, validators=[django.core.validators.RegexValidator(regex='\\d{6}')])),
                ('year_of_birth', profiles.customfields.IntegerRangeField(null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='profiles.Category')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
