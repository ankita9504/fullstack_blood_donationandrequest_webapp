# Generated by Django 3.2 on 2024-04-28 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0006_bloodrequest_request_by_hospital'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=100)),
            ],
        ),
    ]
