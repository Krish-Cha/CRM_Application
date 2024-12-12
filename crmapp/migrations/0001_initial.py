# Generated by Django 4.2.4 on 2024-05-01 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('contactno', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=100)),
                ('subject', models.CharField(max_length=500)),
                ('message', models.CharField(max_length=5000)),
                ('posteddate', models.CharField(max_length=30)),
            ],
        ),
    ]
