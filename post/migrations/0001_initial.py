# Generated by Django 5.1.2 on 2024-11-03 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('category', models.CharField(choices=[('CLIENT', 'Client'), ('MANAGER', 'Manager'), ('COMMON', 'Common')], default='COMMON', max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('link', models.URLField(blank=True, null=True)),
            ],
        ),
    ]