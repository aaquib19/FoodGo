# Generated by Django 3.0.2 on 2020-02-01 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='imge',
            field=models.FileField(blank=True, null=True, upload_to='products/'),
        ),
    ]
