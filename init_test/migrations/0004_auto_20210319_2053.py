# Generated by Django 3.1.7 on 2021-03-19 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('init_test', '0003_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='option3',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='option4',
            field=models.CharField(max_length=200, null=True),
        ),
    ]