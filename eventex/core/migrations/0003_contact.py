# Generated by Django 2.2.1 on 2019-07-28 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190725_2030'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(choices=[('E', 'Email'), ('P', 'Telefone')], max_length=1)),
                ('value', models.CharField(max_length=255)),
                ('speaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Speaker')),
            ],
        ),
    ]
