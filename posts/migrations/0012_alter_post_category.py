# Generated by Django 3.2.23 on 2024-03-12 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_post_excerpt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Facinorous Fluffballs', 'Facinorous Fluffballs'), ('Reptillian Villains', 'Reptillian Villains'), ('Feathered Fiends', 'Feathered Fiends')], default='Facinorous Fluffballs', max_length=40),
        ),
    ]
