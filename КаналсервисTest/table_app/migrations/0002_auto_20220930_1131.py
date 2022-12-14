# Generated by Django 3.2.8 on 2022-09-30 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resulttable',
            old_name='delivery_time',
            new_name='delivery_date',
        ),
        migrations.AlterField(
            model_name='resulttable',
            name='price_dollars',
            field=models.FloatField(verbose_name='стоимость,$'),
        ),
        migrations.AlterField(
            model_name='resulttable',
            name='price_rubs',
            field=models.FloatField(verbose_name='стоимость в руб.'),
        ),
    ]
