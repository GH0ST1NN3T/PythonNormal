# Generated by Django 4.2.7 on 2024-03-27 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tobias', '0007_rename_preco_produto_preco_do_produto_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='produto',
            name='nome_do_produto',
        ),
        migrations.AddField(
            model_name='produto',
            name='Nome_do_produto',
            field=models.CharField(blank=True, db_column='nomeProduto', max_length=30),
        ),
    ]