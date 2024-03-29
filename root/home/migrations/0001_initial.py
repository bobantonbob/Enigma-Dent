# Generated by Django 4.2.3 on 2023-07-24 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('response', models.TextField(max_length=1024)),
                ('image', models.FileField(upload_to='images/response_user')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
