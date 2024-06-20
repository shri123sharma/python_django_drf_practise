# Generated by Django 5.0.3 on 2024-05-17 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iapp3_drf', '0007_musictrack'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
            ],
        ),
    ]