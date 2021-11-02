# Generated by Django 3.2 on 2021-10-31 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_graphs'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.AlterField(
            model_name='graphs',
            name='x1',
            field=models.IntegerField(help_text='x1'),
        ),
        migrations.AlterField(
            model_name='graphs',
            name='x2',
            field=models.IntegerField(help_text='x2'),
        ),
        migrations.AlterField(
            model_name='graphs',
            name='x3',
            field=models.IntegerField(help_text='x3'),
        ),
        migrations.AlterField(
            model_name='graphs',
            name='x4',
            field=models.IntegerField(help_text='x4'),
        ),
        migrations.AlterField(
            model_name='graphs',
            name='x5',
            field=models.IntegerField(help_text='x5'),
        ),
        migrations.AlterField(
            model_name='graphs',
            name='y1',
            field=models.IntegerField(help_text='y1'),
        ),
        migrations.AlterField(
            model_name='graphs',
            name='y2',
            field=models.IntegerField(help_text='y2'),
        ),
        migrations.AlterField(
            model_name='graphs',
            name='y3',
            field=models.IntegerField(help_text='y3'),
        ),
        migrations.AlterField(
            model_name='graphs',
            name='y4',
            field=models.IntegerField(help_text='y4'),
        ),
        migrations.AlterField(
            model_name='graphs',
            name='y5',
            field=models.IntegerField(help_text='y5'),
        ),
    ]