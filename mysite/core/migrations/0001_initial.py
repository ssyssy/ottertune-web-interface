# Generated by Django 2.0.2 on 2018-07-12 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=40)),
                ('shared_buffers', models.IntegerField(choices=[('1', '3'), ('2', '9'), ('3', '27')])),
                ('effective_io_concurrency', models.IntegerField(choices=[('1', '1'), ('2', '2')])),
            ],
        ),
    ]
