# Generated by Django 4.1.13 on 2024-11-18 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mesa', models.CharField(max_length=1000, verbose_name='Mesa')),
                ('platillos', models.CharField(max_length=1000, verbose_name='Platillos')),
                ('fecha_pedido', models.DateTimeField(auto_now_add=True, verbose_name='Fecha pedido')),
            ],
            options={
                'verbose_name': 'Órden',
                'verbose_name_plural': 'Órdenes',
            },
        ),
    ]
