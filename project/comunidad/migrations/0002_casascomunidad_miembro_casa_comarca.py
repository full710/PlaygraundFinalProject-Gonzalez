# Generated by Django 4.2.6 on 2023-10-10 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comunidad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CasasComunidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_casa', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='miembro',
            name='casa_comarca',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='comunidad.casascomunidad'),
        ),
    ]
