# Generated by Django 2.2.5 on 2019-11-25 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='age',
            field=models.IntegerField(default=18),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='weight',
            field=models.IntegerField(default=19),
            preserve_default=False,
        ),
    ]