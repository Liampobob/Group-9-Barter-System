# Generated by Django 3.1.7 on 2021-04-10 16:43

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('business_name', models.CharField(max_length=128, null=True)),
                ('working_days', models.CharField(max_length=128, null=True)),
                ('work_tags', models.CharField(max_length=256, null=True)),
                ('description', models.CharField(max_length=256, null=True)),
                ('contact', models.CharField(max_length=128, null=True)),
                ('start_time', models.IntegerField(null=True)),
                ('end_time', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BusinessReviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('business_id', models.IntegerField()),
                ('review_text', models.CharField(max_length=256)),
                ('stars', models.PositiveIntegerField()),
                ('time', models.TimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('category', models.CharField(choices=[('J', 'Job'), ('C', 'Class'), ('B', 'toBuy'), ('S', 'toSell'), ('O', 'CBO')], max_length=1)),
                ('description', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('facebook_id', models.CharField(max_length=32, null=True)),
                ('name', models.CharField(max_length=80, null=True)),
                ('phone_number', models.CharField(max_length=20, null=True)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('isBusiness', models.BooleanField(default=False)),
                ('bio', models.TextField(null=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
