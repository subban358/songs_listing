# Generated by Django 3.0.1 on 2020-03-30 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='songs',
            name='cover',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
    ]
