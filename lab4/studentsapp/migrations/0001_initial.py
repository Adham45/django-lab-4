# Generated by Django 4.0.2 on 2022-02-03 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('usr_id', models.AutoField(primary_key=True, serialize=False)),
                ('usr_name', models.CharField(default='', max_length=30)),
                ('usr_email', models.EmailField(default='', max_length=100)),
                ('usr_password', models.CharField(max_length=35)),
                ('usr_is_logged', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('track_id', models.AutoField(primary_key=True, serialize=False)),
                ('track_name', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('std_id', models.AutoField(primary_key=True, serialize=False)),
                ('std_fname', models.CharField(default='', max_length=20)),
                ('std_lname', models.CharField(default='', max_length=20)),
                ('track_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='studentsapp.track')),
            ],
        ),
    ]