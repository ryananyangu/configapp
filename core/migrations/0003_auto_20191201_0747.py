# Generated by Django 2.2.7 on 2019-12-01 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20191116_0650'),
    ]

    operations = [
        migrations.AddField(
            model_name='requests',
            name='successExpectedValue',
            field=models.CharField(default=1, max_length=160),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requests',
            name='successResponseKey',
            field=models.CharField(default=1, max_length=160),
            preserve_default=False,
        ),
    ]
