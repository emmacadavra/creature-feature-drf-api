# Generated by Django 3.2.23 on 2024-02-10 23:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('followers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='follower',
            options={'ordering': ['-created_on']},
        ),
        migrations.RenameField(
            model_name='follower',
            old_name='created_at',
            new_name='created_on',
        ),
    ]
