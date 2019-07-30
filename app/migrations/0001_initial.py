# Generated by Django 2.2.3 on 2019-07-30 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.IntegerField()),
                ('title', models.TextField(max_length=40)),
                ('description', models.TextField(max_length=300)),
                ('coordinates', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Exits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direction', models.TextField()),
                ('direction_id', models.IntegerField(blank=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Rooms')),
            ],
        ),
    ]