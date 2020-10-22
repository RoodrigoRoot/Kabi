# Generated by Django 3.1.2 on 2020-10-22 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('phone', models.CharField(max_length=10, verbose_name='Teléfono')),
                ('direction', models.CharField(max_length=200, verbose_name='Dirección')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.RenameField(
            model_name='accounts',
            old_name='created_ay',
            new_name='created_at',
        ),
        migrations.AlterField(
            model_name='accounts',
            name='direction',
            field=models.CharField(max_length=200, verbose_name='Dirección'),
        ),
    ]
