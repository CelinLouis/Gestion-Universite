# Generated by Django 3.2.12 on 2022-04-24 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etudiant_db', '0006_filiere'),
    ]

    operations = [
        migrations.CreateModel(
            name='Niveau',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=10)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
