# Generated by Django 2.0.6 on 2020-04-02 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('sex', models.BooleanField()),
                ('group', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 't_student',
            },
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Grade_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='class',
            name='grade_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.Grade'),
        ),
    ]
