# Generated by Django 4.1.5 on 2023-02-23 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_favourite'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name_plural': 'categories'},
        ),
    ]
