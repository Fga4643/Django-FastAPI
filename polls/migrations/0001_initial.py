# Generated by Django 4.0 on 2024-06-09 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=256)),
                ('client_info', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'clients',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ClientInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'clients_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Endpoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endpoint_name', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'endpoints',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EndpointStates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=256)),
                ('state_reason', models.CharField(max_length=256)),
                ('state_start', models.CharField(max_length=256)),
                ('state_end', models.CharField(max_length=256)),
                ('state_id', models.CharField(max_length=256)),
                ('group_id', models.CharField(max_length=256)),
                ('reason_group', models.CharField(max_length=256)),
                ('info', models.JSONField(default=dict)),
            ],
            options={
                'db_table': 'endpoint_states',
                'managed': False,
            },
        ),
    ]
