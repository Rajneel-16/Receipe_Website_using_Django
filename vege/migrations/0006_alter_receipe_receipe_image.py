# Generated by Django 5.0 on 2024-03-21 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0005_remove_student_department_remove_student_student_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipe',
            name='receipe_image',
            field=models.ImageField(upload_to='receipe'),
        ),
    ]
