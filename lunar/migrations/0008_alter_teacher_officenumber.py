# Generated by Django 3.2.8 on 2022-07-03 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lunar', '0007_alter_teacher_officenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='officenumber',
            field=models.TextField(blank=True, null=True),
        ),
    ]