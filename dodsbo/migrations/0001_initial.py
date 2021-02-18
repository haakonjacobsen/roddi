# Generated by Django 3.1.6 on 2021-02-18 17:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Estate',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('estateID', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('itemID', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('value', models.IntegerField()),
                ('status', models.CharField(max_length=100)),
                ('estateID', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='dodsbo.estate')),
                ('owner_username', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Wish',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('wish', models.CharField(max_length=100)),
                ('itemID', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='dodsbo.item')),
                ('username', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Participate',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('estateID', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='dodsbo.estate')),
                ('username', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('initial_time', models.DateTimeField(
                    default=django.utils.timezone.now)),
                ('text', models.TextField()),
                ('updated_time', models.DateTimeField(
                    default=django.utils.timezone.now)),
                ('itemID', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='dodsbo.item')),
                ('user', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
