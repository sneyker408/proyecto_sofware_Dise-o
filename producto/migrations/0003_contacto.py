# Generated by Django 4.2.6 on 2023-10-29 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0002_productos_delete_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('Nombre', models.TextField(max_length=100)),
                ('Correo', models.TextField(max_length=100)),
                ('Mensaje', models.TextField(max_length=500)),
            ],
        ),
    ]
