# Generated by Django 4.2.4 on 2023-10-23 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_num', models.CharField(max_length=20)),
                ('reg_date', models.DateField()),
                ('engine_num', models.CharField(max_length=50)),
                ('chassis_num', models.CharField(max_length=50)),
                ('rc', models.FileField(upload_to='vehicle/%Y/%m/%d/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.customer')),
            ],
        ),
    ]
