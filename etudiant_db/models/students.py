from django.db import models

class Etudiant(models.Model):
    nom = models.CharField(max_length=100, blank=False, null=False)
    prenom = models.CharField(max_length=50, blank=True, null=True)
    date_naissance = models.DateField(blank=False, null=False)
    lieu_naissance = models.CharField(max_length=50, blank=False, null=False)
    cin = models.CharField(max_length=14,blank=True, null=True)
    contact = models.CharField(max_length=10 ,blank=False, null=False)
    email = models.CharField(max_length=100, blank=True, null=True)
    adresse = models.CharField(max_length=50, blank=False, null=False)
    sexe = models.IntegerField(default=1, blank=False, null=False)
    bacc_serie = models.CharField(max_length=50, blank=False, null=False)
    bacc_annee = models.CharField(max_length=50, blank=False, null=False)
    bacc_motion = models.CharField(max_length=50, blank=False, null=False)
    lycee = models.CharField(max_length=50, blank=False, null=False)
    pere = models.CharField(max_length=50, blank=False, null=False)
    mere = models.CharField(max_length=50, blank=False, null=False)
    tutaire = models.CharField(max_length=50, blank=True, null=True)
    adress_parent = models.CharField(max_length=100, blank=False, null=False)
    date_ajoute = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_modification = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.nom + ' ' + str(self.prenom) + ' ' + str(self.bacc_serie) + ' ' + str(self.bacc_annee) + ' ' + str(self.bacc_motion)+ ' ' + str(self.lycee) + ' ' + str(self.date_ajoute) + ' ' + str(self.date_modification)