# Generated by Django 2.2.6 on 2019-11-07 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
