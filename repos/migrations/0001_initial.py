# Generated by Django 2.2.7 on 2019-11-17 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Repo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('html_url', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('private', models.BooleanField()),
                ('created_at', models.DateTimeField()),
                ('watchers', models.IntegerField()),
                ('body', models.TextField()),
            ],
            options={
                'unique_together': {('name', 'html_url')},
            },
        ),
    ]
