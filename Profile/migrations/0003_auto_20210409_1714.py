# Generated by Django 3.1.3 on 2021-04-09 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0002_auto_20210409_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auxprofiledata',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='City'),
        ),
    ]
