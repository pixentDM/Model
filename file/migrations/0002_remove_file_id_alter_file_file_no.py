# Generated by Django 4.2.10 on 2024-03-06 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='id',
        ),
        migrations.AlterField(
            model_name='file',
            name='file_no',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='파일고유번호'),
        ),
    ]
