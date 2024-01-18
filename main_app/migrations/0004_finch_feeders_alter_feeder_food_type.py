# Generated by Django 5.0.1 on 2024-01-18 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_feeder_alter_feeding_options_alter_finch_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='finch',
            name='feeders',
            field=models.ManyToManyField(to='main_app.feeder'),
        ),
        migrations.AlterField(
            model_name='feeder',
            name='food_type',
            field=models.CharField(choices=[('G', 'Grasses'), ('I', 'Insects'), ('L', 'Liquid'), ('S', 'Seeds')], default='S', max_length=1),
        ),
    ]