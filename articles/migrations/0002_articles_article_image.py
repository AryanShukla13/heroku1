# Generated by Django 4.0.5 on 2022-07-24 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='article_image',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='articles/'),
        ),
    ]
