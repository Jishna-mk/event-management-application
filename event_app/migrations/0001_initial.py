# Generated by Django 4.0.6 on 2022-10-26 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookedList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_name', models.CharField(max_length=200)),
                ('Event_name', models.CharField(max_length=200)),
                ('Sponser_name', models.CharField(max_length=200)),
                ('Start_date', models.CharField(max_length=10)),
                ('End_date', models.CharField(max_length=10)),
            ],
        ),
    ]
