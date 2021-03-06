# Generated by Django 3.1.6 on 2021-03-20 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Name')),
                ('price', models.IntegerField(verbose_name='Price')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('created_at', models.DateField(verbose_name='Created at')),
                ('num_pages', models.IntegerField(verbose_name='Number of pages')),
                ('genre', models.CharField(blank=True, max_length=255, verbose_name='Genre')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Name')),
                ('price', models.IntegerField(verbose_name='Price')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('created_at', models.DateField(verbose_name='Created at')),
                ('type', models.IntegerField(choices=[(1, 'bullet'), (2, 'food'), (3, 'travel'), (4, 'sport')])),
                ('publisher', models.CharField(blank=True, max_length=255, verbose_name='Publisher')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
