# Generated by Django 4.0.6 on 2022-07-28 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_family', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='creation_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
