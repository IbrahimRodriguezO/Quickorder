# Generated by Django 4.1.13 on 2024-10-20 03:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('name', models.CharField(max_length=60, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=40, verbose_name='Apellido paterno')),
                ('last_name_2', models.CharField(max_length=40, verbose_name='Apellido materno')),
                ('rol', models.CharField(choices=[('owner', 'Dueño'), ('waiter', 'Mesero'), ('chef', 'Cocinero')], max_length=20, verbose_name='Rol')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('password', models.CharField(max_length=100, verbose_name='Contraseña')),
                ('phone_number', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message="El número de teléfono debe tener el formato: '+999999999'. Hasta 10 dígitos permitidos.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Teléfono')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
                ('is_active', models.BooleanField(default=True, verbose_name='Estatus')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
