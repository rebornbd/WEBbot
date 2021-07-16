# Generated by Django 3.2.5 on 2021-07-09 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(blank=True, max_length=200, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': ' site',
                'verbose_name_plural': ' sites',
            },
        ),
        migrations.CreateModel(
            name='RelatedSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(blank=True, max_length=200, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relatedsites', to='crawler.site')),
            ],
            options={
                'verbose_name': ' related-site',
                'verbose_name_plural': ' related-sites',
            },
        ),
    ]