# Generated by Django 2.2.5 on 2020-07-28 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mtr', '0004_auto_20200728_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mtr',
            name='motorista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='motoristas.Motoristas'),
        ),
    ]
