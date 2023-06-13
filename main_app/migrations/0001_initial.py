# Generated by Django 4.2.2 on 2023-06-12 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('legend', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('firstSeen', models.CharField(max_length=100)),
            ],
        ),
    ]