# Generated by Django 5.2 on 2025-05-13 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_foarm'),
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
