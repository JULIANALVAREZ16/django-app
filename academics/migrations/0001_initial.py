# Generated by Django 5.0.2 on 2024-04-05 18:52

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('abrev', models.CharField(max_length=10)),
                ('descrip', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 4, 5, 13, 51, 59, 498852))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2024, 4, 5, 13, 51, 59, 498852))),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Identification_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('abrev', models.CharField(max_length=10)),
                ('descrip', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 4, 5, 13, 51, 59, 498852))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2024, 4, 5, 13, 51, 59, 498852))),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=250)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 4, 5, 13, 51, 59, 436344))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2024, 4, 5, 13, 51, 59, 436344))),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Deparments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('abrev', models.CharField(max_length=10)),
                ('descrip', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 4, 5, 13, 51, 59, 498852))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2024, 4, 5, 13, 51, 59, 498852))),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('id_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.countries')),
            ],
        ),
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('abrev', models.CharField(max_length=10)),
                ('descrip', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 4, 5, 13, 51, 59, 498852))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2024, 4, 5, 13, 51, 59, 498852))),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('id_dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.deparments')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('ident_number', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=150)),
                ('mobile', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 4, 5, 13, 51, 59, 498852))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2024, 4, 5, 13, 51, 59, 498852))),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('id_exp_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.cities')),
                ('id_ident_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.identification_type')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.user')),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 4, 5, 13, 51, 59, 498852))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2024, 4, 5, 13, 51, 59, 498852))),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('id_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.person')),
            ],
        ),
    ]
