# Generated by Django 4.0.5 on 2022-07-05 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cards',
            name='cards_image',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='cards/'),
        ),
    ]
