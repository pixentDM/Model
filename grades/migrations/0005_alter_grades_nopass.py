# Generated by Django 4.2.10 on 2024-03-12 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0004_alter_grades_grade_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grades',
            name='nopass',
            field=models.CharField(null=True, verbose_name='불합격'),
        ),
    ]
