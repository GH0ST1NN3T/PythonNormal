# Generated by Django 4.2.7 on 2023-12-07 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tobias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='dataCadastro',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
