# Generated by Django 4.1.5 on 2023-02-28 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_job_date_completed_job_date_requested'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='paid',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='cash_only',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='photo_required',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='recurring',
            field=models.BooleanField(null=True),
        ),
    ]