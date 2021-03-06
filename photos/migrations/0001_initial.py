# Generated by Django 2.2 on 2019-04-24 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shot_date', models.DateTimeField(verbose_name='when the shot was taken')),
                ('camera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.Camera')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoIdentification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('left', models.IntegerField(default=None)),
                ('right', models.IntegerField(default=None)),
                ('top', models.IntegerField(default=None)),
                ('bottom', models.IntegerField(default=None)),
                ('verified', models.BooleanField(default=False)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.Person')),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.Photo')),
            ],
        ),
    ]
