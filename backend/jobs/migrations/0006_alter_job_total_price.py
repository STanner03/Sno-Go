# Generated by Django 4.1.5 on 2023-03-01 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_job_paid_alter_job_cash_only_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='total_price',
            field=models.FloatField(null=True),
        ),
    ]
