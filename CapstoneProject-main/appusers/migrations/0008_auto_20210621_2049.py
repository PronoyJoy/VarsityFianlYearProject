# Generated by Django 3.2.4 on 2021-06-21 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appusers', '0007_follow'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='follower',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='following',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]