# Generated by Django 3.1.2 on 2020-10-25 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Storage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a new tag', max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='upload',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.AddField(
            model_name='upload',
            name='tags',
            field=models.ManyToManyField(help_text='Select the tags', to='Storage.Tag'),
        ),
    ]
