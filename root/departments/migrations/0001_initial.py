# Generated by Django 4.2.3 on 2023-07-17 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15, verbose_name="Ім'я")),
                ('about', models.TextField(max_length=256, verbose_name='Тема')),
                ('email', models.EmailField(max_length=30, verbose_name='Email')),
                ('message', models.TextField(max_length=1024, verbose_name='Повідомлення')),
            ],
        ),
    ]
