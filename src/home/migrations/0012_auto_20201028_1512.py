# Generated by Django 3.1.2 on 2020-10-28 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_hero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
