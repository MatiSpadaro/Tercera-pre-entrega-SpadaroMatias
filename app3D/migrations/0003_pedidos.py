# Generated by Django 4.2.5 on 2023-09-12 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app3D', '0002_productos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo3D', models.CharField(max_length=40)),
                ('filamento', models.CharField(max_length=40)),
            ],
        ),
    ]
