# Generated by Django 2.2 on 2019-04-27 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0002_article_typeof'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
            ],
        ),
    ]
