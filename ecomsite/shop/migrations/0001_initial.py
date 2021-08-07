# Generated by Django 3.2.5 on 2021-07-28 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('discont_price', models.FloatField()),
                ('desciption', models.TextField()),
                ('image', models.CharField(max_length=300)),
            ],
        ),
    ]
