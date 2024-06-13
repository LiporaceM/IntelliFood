# Generated by Django 5.0.6 on 2024-06-13 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image_url', models.URLField()),
                ('prep_time', models.IntegerField()),
                ('ingredients', models.TextField()),
                ('instructions', models.TextField()),
            ],
        ),
    ]
