# Generated by Django 2.2.1 on 2019-05-31 06:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('name', models.CharField(max_length=60, verbose_name='Name')),
                ('description', models.CharField(blank=True, max_length=158, verbose_name='Description')),
                ('slug', models.CharField(blank=True, db_index=True, max_length=64, unique=True, verbose_name='Slug')),
                ('language', models.CharField(choices=[('en-us', 'English'), ('id', 'Indonesian')], default='en-us', max_length=6, verbose_name='Language')),
                ('created_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='childs', to='post.Category', verbose_name='Parent Category')),
            ],
            options={
                'db_table': 'djwb_category',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('title', models.CharField(blank=True, max_length=120, null=True, verbose_name='Title')),
                ('description', models.CharField(blank=True, max_length=158, null=True, verbose_name='Description')),
                ('slug', models.CharField(blank=True, db_index=True, max_length=128, null=True, unique=True, verbose_name='Slug')),
                ('body', models.TextField(blank=True, null=True, verbose_name='Body')),
                ('body_preview', models.TextField(blank=True, null=True, verbose_name='Body Preview')),
                ('read', models.IntegerField(default=0, verbose_name='Read')),
                ('state', models.IntegerField(default=0, verbose_name='State')),
                ('publish_date', models.DateTimeField(blank=True, null=True, verbose_name='Publish Date')),
                ('language', models.CharField(choices=[('en-us', 'English'), ('id', 'Indonesian')], default='en-us', max_length=6, verbose_name='Language')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='post.Category', verbose_name='Category')),
                ('created_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
            ],
            options={
                'db_table': 'djwb_post',
                'ordering': ['-publish_date'],
            },
        ),
    ]