# Generated by Django 3.0.8 on 2020-08-25 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200825_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newcampaign',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
