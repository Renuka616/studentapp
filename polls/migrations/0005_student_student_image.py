# Generated by Django 4.2.4 on 2023-10-02 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_alter_student_first_name_alter_student_last_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]