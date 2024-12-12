# Generated by Django 4.2.4 on 2024-05-22 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('contactno', models.CharField(max_length=10)),
                ('emailaddress', models.CharField(max_length=50)),
                ('buydate', models.CharField(max_length=30)),
            ],
        ),
    ]
