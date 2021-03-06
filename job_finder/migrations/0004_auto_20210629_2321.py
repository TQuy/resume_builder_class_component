# Generated by Django 3.2.4 on 2021-06-29 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_finder', '0003_alter_resume_content'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='resume',
            name='unique_resume_name',
        ),
        migrations.AddConstraint(
            model_name='resume',
            constraint=models.UniqueConstraint(fields=('name', 'user'), name='unique_resume_name'),
        ),
    ]
