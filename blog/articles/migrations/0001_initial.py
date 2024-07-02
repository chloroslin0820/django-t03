# Generated by Django 4.2.13 on 2024-07-02 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=150)),
                ('contenu', models.TextField()),
                ('slug', models.SlugField(max_length=100)),
                ('date_publication', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(default='default.jpg', upload_to='')),
            ],
        ),
    ]
