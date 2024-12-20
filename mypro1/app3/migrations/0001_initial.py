# Generated by Django 5.1.2 on 2024-12-05 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=200)),
                ('email_id', models.EmailField(max_length=254, unique=True)),
                ('mobile_no', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
