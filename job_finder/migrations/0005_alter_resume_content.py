# Generated by Django 3.2.4 on 2021-07-01 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_finder', '0004_auto_20210629_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='content',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]
