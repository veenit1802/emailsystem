# Generated by Django 2.2.2 on 2019-06-23 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_mail', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=150)),
                ('body', models.CharField(max_length=400)),
            ],
        ),
    ]
