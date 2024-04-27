# Generated by Django 5.0.2 on 2024-04-26 22:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0004_alter_cities_created_at_alter_cities_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cities',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 17, 24, 16, 535358)),
        ),
        migrations.AlterField(
            model_name='cities',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 17, 24, 16, 535358)),
        ),
        migrations.AlterField(
            model_name='countries',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 17, 24, 16, 535358)),
        ),
        migrations.AlterField(
            model_name='countries',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 17, 24, 16, 535358)),
        ),
        migrations.AlterField(
            model_name='deparments',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 17, 24, 16, 535358)),
        ),
        migrations.AlterField(
            model_name='deparments',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 17, 24, 16, 535358)),
        ),
        migrations.AlterField(
            model_name='identification_type',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 17, 24, 16, 535358)),
        ),
        migrations.AlterField(
            model_name='identification_type',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 17, 24, 16, 535358)),
        ),
        migrations.AlterField(
            model_name='person',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 17, 24, 16, 535358)),
        ),
        migrations.AlterField(
            model_name='person',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 17, 24, 16, 535358)),
        ),
        migrations.AlterField(
            model_name='students',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 17, 24, 16, 535358)),
        ),
        migrations.AlterField(
            model_name='students',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 17, 24, 16, 535358)),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 17, 24, 16, 535358)),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 17, 24, 16, 535358)),
        ),
    ]
