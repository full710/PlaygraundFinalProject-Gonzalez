# Generated by Django 4.2.6 on 2023-10-10 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0004_alter_publicaciones_cantidad_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publicaciones',
            options={'verbose_name': 'Publicación', 'verbose_name_plural': 'Publicaciones'},
        ),
    ]
