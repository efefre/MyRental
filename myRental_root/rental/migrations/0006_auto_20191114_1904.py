# Generated by Django 2.2.6 on 2019-11-14 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0005_auto_20191110_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanbook',
            name='date',
            field=models.DateField(verbose_name='Data wypożyczenia'),
        ),
        migrations.AlterField(
            model_name='loanbook',
            name='friend_email',
            field=models.EmailField(max_length=254, verbose_name='Adres e-mail'),
        ),
        migrations.AlterField(
            model_name='loanbook',
            name='friend_name',
            field=models.CharField(max_length=50, verbose_name='Imię'),
        ),
        migrations.AlterField(
            model_name='loanbook',
            name='friend_surname',
            field=models.CharField(max_length=50, verbose_name='Nazwisko'),
        ),
    ]
