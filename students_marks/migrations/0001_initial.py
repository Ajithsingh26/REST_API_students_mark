# Generated by Django 3.2.4 on 2021-07-13 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=20)),
                ('marks', models.FloatField()),
            ],
        ),
    ]
