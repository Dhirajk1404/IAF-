# Generated by Django 3.2.4 on 2021-07-22 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0012_airforcesyllabus_navysyllabus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airforceexam',
            name='eligibility_age',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='armyexam',
            name='eligibility_age',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='navyexam',
            name='eligibility_age',
            field=models.CharField(max_length=500),
        ),
    ]