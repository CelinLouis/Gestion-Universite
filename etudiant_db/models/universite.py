from django.db import models

class Universite(models.Model):
    nom = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.nom + '  ' + str(self.description) + '  ' + str(self.date_created)