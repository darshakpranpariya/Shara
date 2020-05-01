# Generated by Django 3.0.4 on 2020-05-01 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DeepUserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reputation', models.PositiveIntegerField()),
                ('totalupvote', models.PositiveIntegerField()),
                ('totaldownvote', models.PositiveIntegerField()),
                ('totaltips', models.PositiveIntegerField()),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sharaapp.AllUsers')),
            ],
        ),
    ]
