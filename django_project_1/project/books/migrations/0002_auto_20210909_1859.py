# Generated by Django 3.2.6 on 2021-09-09 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='authors',
            options={'ordering': ['-birthday'], 'verbose_name': 'Authors', 'verbose_name_plural': 'Authors'},
        ),
        migrations.AlterModelOptions(
            name='publishings',
            options={'verbose_name': 'Publishings', 'verbose_name_plural': 'Publishings'},
        ),
    ]
