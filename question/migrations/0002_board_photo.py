# Generated by Django 2.2.1 on 2019-05-28 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]