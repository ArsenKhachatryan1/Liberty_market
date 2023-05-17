# Generated by Django 4.2.1 on 2023-05-06 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home_page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo_img', models.ImageField(upload_to='images', verbose_name='Logo image')),
                ('home', models.CharField(max_length=30, verbose_name='Home')),
                ('author', models.CharField(max_length=30, verbose_name='Author')),
                ('create', models.CharField(max_length=30, verbose_name='Create')),
                ('details', models.CharField(max_length=30, verbose_name='Details')),
                ('explore', models.CharField(max_length=30, verbose_name='Explore')),
            ],
        ),
    ]
