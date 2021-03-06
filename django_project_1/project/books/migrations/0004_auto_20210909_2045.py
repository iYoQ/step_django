# Generated by Django 3.2.6 on 2021-09-09 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20210909_2037'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['nickname'], 'verbose_name': 'Review', 'verbose_name_plural': 'Review'},
        ),
        migrations.AddField(
            model_name='review',
            name='book_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='books.books', verbose_name='book'),
        ),
    ]
