# Generated by Django 5.2 on 2025-04-28 16:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Origem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='receita',
            name='origem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.origem'),
        ),
    ]
