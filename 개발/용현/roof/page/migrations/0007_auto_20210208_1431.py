# Generated by Django 3.1.5 on 2021-02-08 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0006_auto_20210208_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='category_id',
            field=models.ManyToManyField(to='page.Category'),
        ),
    ]
