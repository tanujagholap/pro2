# Generated by Django 5.0.3 on 2024-03-15 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Create',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=20)),
                ('s_name', models.CharField(max_length=20)),
                ('roll', models.IntegerField()),
                ('marks', models.IntegerField()),
            ],
        ),
    ]
