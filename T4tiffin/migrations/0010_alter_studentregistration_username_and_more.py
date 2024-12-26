# Generated by Django 5.1.3 on 2024-12-26 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('T4tiffin', '0009_alter_studentregistration_school_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentregistration',
            name='username',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterUniqueTogether(
            name='studentregistration',
            unique_together={('username', 'school_id')},
        ),
    ]