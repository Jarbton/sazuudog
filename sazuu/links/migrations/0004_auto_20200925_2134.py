# Generated by Django 3.1.1 on 2020-09-25 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0003_link_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='icon',
            field=models.CharField(choices=[('129430', '128536'), ('128248', '128248'), ('127925', '127925'), ('128250', '128250'), ('128036', '128036')], default='129430', help_text='Emoji logo for this service.', max_length=30),
        ),
    ]
