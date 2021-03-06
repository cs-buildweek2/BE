# Generated by Django 2.2.3 on 2019-07-30 22:10

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('room_id', models.IntegerField()),
                ('coordinates', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Exits',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('direction', models.TextField()),
                ('direction_id', models.IntegerField()),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Rooms')),
            ],
        ),
    ]
