# Generated by Django 4.2.6 on 2023-10-18 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('Nombre', models.TextField(max_length=100)),
                ('Existencias', models.IntegerField()),
                ('Descripcion', models.TextField(max_length=150)),
                ('Precio', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
    ]