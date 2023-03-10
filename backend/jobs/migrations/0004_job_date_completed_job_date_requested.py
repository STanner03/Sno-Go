# Generated by Django 4.1.5 on 2023-02-28 20:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_remove_job_area_type_job_services_job_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='date_completed',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='date_requested',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
