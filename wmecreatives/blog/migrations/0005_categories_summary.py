# Generated by Django 4.2.3 on 2023-07-24 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_categories_author_categories_date_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='summary',
            field=models.TextField(blank=True, help_text='31 letters max will give a better out look', null=True),
        ),
    ]
