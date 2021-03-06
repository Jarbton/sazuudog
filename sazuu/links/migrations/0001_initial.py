# Generated by Django 3.1.1 on 2020-09-25 18:35

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('service', models.CharField(help_text='Title of service e.g Facebook.', max_length=250)),
                ('url', models.URLField(help_text='Url to account page on service.', max_length=500)),
                ('display', models.BooleanField(default=False, help_text='Indicate if link should be displayed.')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
