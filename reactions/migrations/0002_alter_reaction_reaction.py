# Generated by Django 3.2.23 on 2024-02-16 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reaction',
            name='reaction',
            field=models.CharField(choices=[('CROWN', 'Your Highness!'), ('GOOD', 'Good Girl/Boy!'), ('LOVE', 'I love you!')], max_length=50),
        ),
    ]
