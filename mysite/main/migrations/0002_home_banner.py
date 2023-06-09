# Generated by Django 4.2.1 on 2023-05-06 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home_banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Name')),
                ('text1', models.CharField(max_length=256, verbose_name='text1')),
                ('text2', models.CharField(max_length=256, verbose_name='text2')),
                ('text3', models.CharField(max_length=256, verbose_name='text3')),
                ('text4', models.CharField(max_length=256, verbose_name='text4')),
                ('text5', models.CharField(max_length=256, verbose_name='text5')),
                ('text6', models.CharField(max_length=256, verbose_name='text6')),
                ('video_link', models.URLField(verbose_name='Video link')),
                ('img1', models.ImageField(upload_to='images', verbose_name='Image 1')),
                ('img2', models.ImageField(upload_to='images', verbose_name='Image 2')),
            ],
        ),
    ]
