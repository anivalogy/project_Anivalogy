# Generated by Django 3.1.2 on 2020-10-24 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_navigation'),
    ]

    operations = [
        migrations.CreateModel(
            name='gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics')),
            ],
        ),
        migrations.DeleteModel(
            name='header',
        ),
        migrations.DeleteModel(
            name='navigation',
        ),
    ]