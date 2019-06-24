# Generated by Django 2.1.7 on 2019-05-08 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookingForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email_address', models.CharField(max_length=30)),
                ('contact_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Preferences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_1', models.CharField(max_length=30)),
                ('entry_2', models.CharField(max_length=30)),
                ('entry_3', models.CharField(max_length=30)),
                ('entry_4', models.TextField(max_length=50)),
                ('entry_5', models.TextField(max_length=50)),
                ('incubator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saunterer.BookingForm')),
            ],
        ),
    ]
