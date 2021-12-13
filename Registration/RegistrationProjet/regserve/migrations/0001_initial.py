# Generated by Django 3.2.9 on 2021-11-30 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentId', models.PositiveIntegerField(blank=True)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('schoolyear', models.CharField(choices=[('FR', 'Freshman'), ('FR', 'Freshman'), ('FR', 'Freshman'), ('FR', 'Freshman'), ('FR', 'Freshman')], max_length=2)),
                ('email', models.EmailField(max_length=254)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(blank=True)),
            ],
        ),
    ]
