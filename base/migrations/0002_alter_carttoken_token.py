# Generated by Django 4.1.2 on 2022-10-21 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carttoken',
            name='token',
            field=models.CharField(default='Mj8xwHekwj6I7EbApeqJF2GNJsiMRDDj5c1s5g1Ob0Xy5RucXh', max_length=50),
        ),
    ]
