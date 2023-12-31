# Generated by Django 4.2.2 on 2023-09-19 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ColorPickerImageHolder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_title', models.CharField(max_length=255)),
                ('image_file', models.ImageField(upload_to='images/')),
                ('upload_datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
