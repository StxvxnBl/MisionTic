# Generated by Django 4.1.1 on 2022-10-08 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0004_cliente_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.CharField(max_length=50, verbose_name='Email'),
        ),
    ]