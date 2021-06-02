# Generated by Django 3.2.3 on 2021-05-30 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchdrink', '0007_auto_20210529_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='drink',
            name='ingredientsProportion',
            field=models.TextField(default='ingredients', verbose_name='Składniki'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='alcohol',
            field=models.CharField(max_length=20, verbose_name='Alkohol'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='fruit',
            field=models.CharField(blank=True, max_length=20, verbose_name='Owoce'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='otheradd',
            field=models.CharField(blank=True, max_length=20, verbose_name='Inne dodatki'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='otherdrink',
            field=models.CharField(blank=True, max_length=20, verbose_name='Inne napoje'),
        ),
    ]