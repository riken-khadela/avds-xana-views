# Generated by Django 3.2.3 on 2023-09-12 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twbot', '0003_auto_20230715_0926'),
    ]

    operations = [
        migrations.AddField(
            model_name='postdetails',
            name='saved_users',
            field=models.ManyToManyField(related_name='save_posts', to='twbot.User_details'),
        ),
    ]
