# Generated by Django 3.2.12 on 2022-04-21 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(blank=True, max_length=50, null=True)),
                ('date_naissance', models.DateField()),
                ('lieu_naissance', models.CharField(max_length=50)),
                ('cin', models.IntegerField(blank=True, null=True)),
                ('contact', models.IntegerField()),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('adresse', models.CharField(max_length=50)),
                ('sexe', models.IntegerField(default=1)),
                ('bacc_serie', models.CharField(max_length=50)),
                ('bacc_annee', models.CharField(max_length=50)),
                ('bacc_motion', models.CharField(max_length=50)),
                ('lycee', models.CharField(max_length=50)),
                ('pere', models.CharField(max_length=50)),
                ('mere', models.CharField(max_length=50)),
                ('tutaire', models.CharField(blank=True, max_length=50, null=True)),
                ('adress_parent', models.CharField(max_length=100)),
                ('date_ajoute', models.DateTimeField(auto_now_add=True)),
                ('date_modification', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
