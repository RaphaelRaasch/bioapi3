# Generated by Django 2.2.5 on 2020-07-28 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('motoristas', '0003_auto_20200602_2119'),
        ('mtrv2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mtrv2',
            name='motorista',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='motoristas.Motoristas'),
            preserve_default=False,
        ),
    ]