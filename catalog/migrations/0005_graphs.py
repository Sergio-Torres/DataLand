# Generated by Django 3.2 on 2021-10-15 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_delete_prueba'),
    ]

    operations = [
        migrations.CreateModel(
            name='Graphs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=1000)),
                ('x1', models.IntegerField(verbose_name=())),
                ('x2', models.IntegerField(verbose_name=())),
                ('x3', models.IntegerField(verbose_name=())),
                ('x4', models.IntegerField(verbose_name=())),
                ('x5', models.IntegerField(verbose_name=())),
                ('y1', models.IntegerField(verbose_name=())),
                ('y2', models.IntegerField(verbose_name=())),
                ('y3', models.IntegerField(verbose_name=())),
                ('y4', models.IntegerField(verbose_name=())),
                ('y5', models.IntegerField(verbose_name=())),
            ],
        ),
    ]