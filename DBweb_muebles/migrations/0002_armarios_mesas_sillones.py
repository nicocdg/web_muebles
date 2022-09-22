# Generated by Django 4.1.1 on 2022-09-19 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DBweb_muebles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Armarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=40)),
                ('material', models.CharField(max_length=40)),
                ('puertas', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Mesas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=40)),
                ('material', models.CharField(max_length=40)),
                ('capacidadPersonas', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sillones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=40)),
                ('material', models.CharField(max_length=40)),
                ('cuerpos', models.IntegerField()),
            ],
        ),
    ]