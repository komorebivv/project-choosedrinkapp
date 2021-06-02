# Generated by Django 3.2.3 on 2021-05-28 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchdrink', '0004_alter_drink_descriptionpreparing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drink',
            name='descriptionPreparing',
            field=models.TextField(verbose_name='Opis przygotowania'),
        ),
        migrations.AlterField(
            model_name='drink',
            name='nameDrink',
            field=models.CharField(max_length=50, verbose_name='Nazwa drinku'),
        ),
        migrations.AlterField(
            model_name='drink',
            name='photo',
            field=models.ImageField(default='some photo', upload_to='uploads/', verbose_name='Zdjęcie drinka'),
        ),
        migrations.AlterField(
            model_name='drink',
            name='taste',
            field=models.CharField(choices=[('S', 'słodki'), ('B', 'gorzki'), ('R', 'kwaśny')], default='S', max_length=2, verbose_name='Smak drinka'),
        ),
        migrations.AlterField(
            model_name='drink',
            name='temperature',
            field=models.CharField(choices=[('W', 'ciepły'), ('C', 'zimny')], default='C', max_length=2, verbose_name='Temperatura'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='alcohol',
            field=models.CharField(max_length=15, verbose_name='Alkohol'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='fruit',
            field=models.CharField(max_length=15, verbose_name='Owoce'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='otheradd',
            field=models.CharField(max_length=15, verbose_name='Inne dodatki'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='otherdrink',
            field=models.CharField(max_length=15, verbose_name='Inne napoje'),
        ),
    ]
