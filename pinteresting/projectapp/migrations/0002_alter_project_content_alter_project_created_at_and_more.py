# Generated by Django 4.1.2 on 2022-10-14 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
