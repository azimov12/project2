# Generated by Django 4.2.4 on 2023-09-15 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='keyboard',
            name='k_brand_name',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AddField(
            model_name='noutbooks',
            name='noutbook_name',
            field=models.CharField(default='', max_length=25),
        ),
    ]
