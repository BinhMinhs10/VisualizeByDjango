# Generated by Django 2.2 on 2019-04-12 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('benefits', models.TextField()),
                ('destination', models.CharField(max_length=200)),
                ('image_urls', models.CharField(max_length=400)),
                ('link', models.CharField(max_length=400)),
                ('name', models.CharField(max_length=200)),
                ('room_type', models.CharField(max_length=200)),
                ('images', models.CharField(max_length=200)),
                ('price', models.IntegerField(default=0)),
                ('star', models.FloatField()),
            ],
        ),
    ]