# Generated by Django 2.2.6 on 2019-11-09 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0001_initial'),
        ('rental', '0003_delete_books'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoanBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('friend_name', models.CharField(max_length=50)),
                ('friend_surname', models.CharField(max_length=50)),
                ('friend_email', models.EmailField(max_length=254)),
                ('book', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='books.Books')),
            ],
        ),
    ]
