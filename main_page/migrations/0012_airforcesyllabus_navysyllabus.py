# Generated by Django 3.1.4 on 2021-07-18 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0011_armysyllabus'),
    ]

    operations = [
        migrations.CreateModel(
            name='AirforceSyllabus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('subjects', models.CharField(max_length=1000)),
                ('syllabus', models.CharField(max_length=100000)),
            ],
        ),
        migrations.CreateModel(
            name='NavySyllabus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('subjects', models.CharField(max_length=1000)),
                ('syllabus', models.CharField(max_length=100000)),
            ],
        ),
    ]