# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 19:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Characters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('cclass', models.CharField(choices=[('FI', 'Fighter'), ('RO', 'Rogue'), ('WI', 'Wizard')], default='FI', max_length=2)),
                ('strength', models.PositiveSmallIntegerField(default=1)),
                ('dexterity', models.PositiveSmallIntegerField(default=1)),
                ('intelligence', models.PositiveSmallIntegerField(default=1)),
                ('health', models.PositiveSmallIntegerField(default=1)),
                ('current_health', models.SmallIntegerField(default=1)),
                ('gold', models.PositiveSmallIntegerField(default=0)),
                ('level', models.PositiveSmallIntegerField(default=1)),
                ('killed_by', models.CharField(default='', max_length=255)),
                ('slug', models.SlugField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owned_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Users')),
            ],
        ),
        migrations.CreateModel(
            name='Combats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Exits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exitdirection', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
                ('strbonus', models.PositiveSmallIntegerField()),
                ('dexbonus', models.PositiveSmallIntegerField()),
                ('intbonus', models.PositiveSmallIntegerField()),
                ('hthbonus', models.PositiveSmallIntegerField()),
                ('consumable', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owned_by', models.ManyToManyField(related_name='owner', to='game.Characters')),
            ],
        ),
        migrations.CreateModel(
            name='Monsters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
                ('mclass', models.CharField(choices=[('BR', 'Brute'), ('AS', 'Assassin'), ('MA', 'Mage'), ('EL', 'Elite')], default='BR', max_length=2)),
                ('strength', models.PositiveSmallIntegerField(default=1)),
                ('dexterity', models.PositiveSmallIntegerField(default=1)),
                ('intelligence', models.PositiveSmallIntegerField(default=1)),
                ('health', models.PositiveSmallIntegerField(default=1)),
                ('image', models.CharField(max_length=10)),
                ('slug', models.SlugField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('killed_by', models.ManyToManyField(related_name='killed', to='game.Characters')),
            ],
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('peek_description', models.TextField()),
                ('terrain_type', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('currently_in', models.ManyToManyField(related_name='populating', to='game.Characters')),
                ('explored_by', models.ManyToManyField(related_name='explored', to='game.Characters')),
                ('monster', models.ManyToManyField(related_name='denizen', to='game.Monsters')),
            ],
        ),
        migrations.CreateModel(
            name='Traps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
                ('tclass', models.CharField(choices=[('PZ', 'Puzzle'), ('PS', 'Poison'), ('RF', 'Reflex'), ('CL', 'Collapse')], default='PS', max_length=2)),
                ('strength', models.PositiveSmallIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Treasures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
                ('gold', models.PositiveSmallIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Items')),
            ],
        ),
        migrations.AddField(
            model_name='rooms',
            name='trap',
            field=models.ManyToManyField(related_name='dangers', to='game.Traps'),
        ),
        migrations.AddField(
            model_name='rooms',
            name='treasure',
            field=models.ManyToManyField(related_name='reward', to='game.Treasures'),
        ),
        migrations.AddField(
            model_name='exits',
            name='comes_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entrances', to='game.Rooms'),
        ),
        migrations.AddField(
            model_name='exits',
            name='leads_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exits', to='game.Rooms'),
        ),
    ]
