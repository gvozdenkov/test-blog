# Generated by Django 4.0.1 on 2022-01-26 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_author_tag_post_author_post_tag'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name_plural': 'Posts'},
        ),
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.CharField(max_length=40),
        ),
    ]
