# Generated by Django 3.1.2 on 2020-11-14 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Storage', '0006_auto_20201114_1410'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='auther',
            new_name='author',
        ),
    ]
