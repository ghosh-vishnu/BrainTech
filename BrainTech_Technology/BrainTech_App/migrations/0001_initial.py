# Generated by Django 4.2.11 on 2024-09-20 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_number', models.CharField(max_length=50, unique=True)),
                ('offer_letter', models.FileField(upload_to='offer_letters/')),
            ],
        ),
    ]
