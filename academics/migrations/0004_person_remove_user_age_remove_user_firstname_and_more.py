# Generated by Django 5.0.2 on 2024-03-15 21:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0003_alter_user_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('ident_number', models.CharField(blank=True, max_length=12)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
        migrations.RemoveField(
            model_name='user',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='user',
            name='ident_number',
        ),
        migrations.RemoveField(
            model_name='user',
            name='lastname',
        ),
        migrations.AddField(
            model_name='user',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 15, 16, 42, 11, 684383)),
        ),
        migrations.AddField(
            model_name='user',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 15, 16, 42, 11, 684383)),
        ),
    ]