from __future__ import unicode_literals
from datetime import date

from django.db import models

class Projekt(models.Model):
	Titel = models.CharField(max_length=64, unique=True)
	Startdatum = models.DateField()
	Enddatum = models.DateField()
	Einnahmen = models.IntegerField()
	
	def __str__(self):
		return "{:} ({:} Euro)".format(self.Titel, self.Einnahmen)
	
	def ProjektEinnahmen(self, startZeit, zeitraum):
		currZeit = startZeit
		einnahmen = list()
		for _ in range(zeitraum):
			nextZeit = date(currZeit.year if currZeit.month < 12 else currZeit.year + 1, currZeit.month + 1 if currZeit.month < 12 else 1, 1)
			if currZeit <= self.Enddatum < nextZeit:
				einnahmen.append(self.Einnahmen)
			else:
				einnahmen.append(0)
			currZeit = nextZeit
		
		return einnahmen

class Angestellter(models.Model):
	Name = models.CharField(max_length=64, unique=True)
	Gehalt = models.IntegerField()
	Einstellungsdatum = models.DateField()
	Entlassungsdatum = models.DateField(null=True, blank=True)
	
	def __str__(self):
		return self.Name
	
	def Gehaelter(self, startZeit, zeitraum=24):
		currDate = startZeit
		gehaelter = list()
		for _ in range(zeitraum):
			if self.Einstellungsdatum > currDate:
				gehaelter.append(0)
			else:
				if self.Entlassungsdatum != None and self.Entlassungsdatum < currDate:
					gehaelter.append(0)
				else:
					gehaelter.append(self.Gehalt)
			
			currDate = date(currDate.year if currDate.month < 12 else currDate.year + 1, currDate.month + 1 if currDate.month < 12 else 1, 1)
			
		return gehaelter
