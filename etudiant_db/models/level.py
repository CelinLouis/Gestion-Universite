from django.db import models


class Niveau(models.Model):
    titre = models.CharField(max_length=10, blank=False, null=False)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.titre + '  ' + str(self.date_created)