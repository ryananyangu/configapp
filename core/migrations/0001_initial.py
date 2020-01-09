# Generated by Django 2.2.7 on 2019-11-10 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HttpHeaders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(db_index=True, max_length=32)),
                ('value', models.CharField(max_length=32)),
                ('date_created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'httpheaders',
                'verbose_name_plural': 'httpheaders',
                'db_table': 'httpheaders',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PayloadKeys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('KeyName', models.CharField(db_index=True, max_length=32)),
                ('Description', models.TextField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'payloadkeys',
                'verbose_name_plural': 'payloadkeys',
                'db_table': 'PayloadKeys',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requestDestinationClient', models.CharField(max_length=32)),
                ('uri', models.CharField(max_length=160)),
                ('requestTemplate', models.TextField()),
                ('isXml', models.BooleanField(default=False)),
                ('hasCertificate', models.BooleanField(default=False)),
                ('certificate', models.FileField(blank=True, null=True, upload_to='.')),
                ('isCustomSocket', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Requests',
                'verbose_name_plural': 'Requests',
                'db_table': 'Requests',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('KeyName', models.CharField(max_length=160)),
                ('isArray', models.BooleanField(default=False)),
                ('valueKeyName', models.CharField(blank=True, max_length=160)),
                ('date_created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Requests')),
            ],
            options={
                'verbose_name': 'reponse',
                'verbose_name_plural': 'reponses',
                'unique_together': {('request', 'KeyName')},
            },
        ),
        migrations.CreateModel(
            name='RequestExtraData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placeholder', models.CharField(db_index=True, max_length=32)),
                ('date_created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Response')),
            ],
            options={
                'verbose_name': 'RequestExtraData',
                'verbose_name_plural': 'RequestExtraDatas',
                'db_table': 'RequestExtraData',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='RequestHeaderMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('headers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.HttpHeaders')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Requests')),
            ],
            options={
                'verbose_name': 'RequestHeaderMapping',
                'verbose_name_plural': 'RequestHeaderMappings',
                'db_table': 'RequestHeaderMapping',
                'managed': True,
                'unique_together': {('request', 'headers')},
            },
        ),
        migrations.CreateModel(
            name='ProcessFlow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serviceID', models.CharField(max_length=32, unique=True)),
                ('serviceCode', models.CharField(db_index=True, max_length=32, unique=True)),
                ('priority', models.PositiveIntegerField(default=0)),
                ('processname', models.CharField(max_length=32)),
                ('processDesc', models.TextField()),
                ('isFinal', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Requests')),
            ],
            options={
                'verbose_name': 'processflow',
                'verbose_name_plural': 'processflows',
                'db_table': 'ProcessFlow',
                'managed': True,
                'unique_together': {('request', 'serviceID', 'serviceCode')},
            },
        ),
        migrations.CreateModel(
            name='PayloadKeyRequestMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placeholder', models.CharField(max_length=32)),
                ('date_created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('payloadkey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.PayloadKeys')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Requests')),
            ],
            options={
                'verbose_name': 'payloadkeyrequestmapping',
                'verbose_name_plural': 'payloadkeyrequestmappings',
                'db_table': 'PayloadKeyRequestMapping',
                'managed': True,
                'unique_together': {('request', 'payloadkey')},
            },
        ),
    ]
