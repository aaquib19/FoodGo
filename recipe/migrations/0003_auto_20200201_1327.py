# Generated by Django 3.0.2 on 2020-02-01 13:27

from django.db import migrations, models
import recipe.models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_recipe_imge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='imge',
        ),
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=recipe.models.upload_image_path),
        ),
    ]
