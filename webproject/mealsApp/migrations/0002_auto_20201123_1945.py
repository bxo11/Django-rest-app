# Generated by Django 3.1.3 on 2020-11-23 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mealsApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='admins',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='meals',
        ),
    ]
