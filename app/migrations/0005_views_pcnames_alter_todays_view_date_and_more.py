# Generated by Django 5.0.6 on 2024-06-10 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_todays_view_date_alter_todays_view_views_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='views',
            name='PcNames',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='todays_view',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='views',
            name='date',
            field=models.DateField(),
        ),
    ]
