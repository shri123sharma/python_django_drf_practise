# Generated by Django 5.0.3 on 2024-05-07 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('i2app_signal', '0003_task_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('comp_name', models.CharField(max_length=255)),
                ('comp_location', models.CharField(max_length=255)),
                ('comp_type', models.CharField(choices=[('IT', 'Information technology'), (
                    'Sales', 'Sales'), ('Telecom', 'TC')], default='IT', max_length=8)),
            ],
        ),
    ]
