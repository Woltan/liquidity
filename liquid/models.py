from __future__ import unicode_literals

from django.db import models

class Projekt(models.Model):
	Titel = models.CharField(max_length=64, unique=True)
	Startdatum = models.DateField()
	Enddatum = models.DateField()
	Einnahmen = models.IntegerField()
	
	def __str__(self):
		return "{:} ({:} Euro)".format(self.Titel, self.Einnahmen)
	
	@classmethod
	def ProjektEinnahmen(cls, startZeit, endZeit):
		k = sum([p.Einnahmen if startZeit <= p.Enddatum < endZeit else 0 for p in cls.objects.all()])
		print startZeit, endZeit, k
		return k 

class Angestellter(models.Model):
	Name = models.CharField(max_length=64, unique=True)
	Gehalt = models.IntegerField()
	Einstellungsdatum = models.DateField()
	Entlassungsdatum = models.DateField(null=True, blank=True)
	
	def __str__(self):
		return self.Name
	
	@classmethod
	def Gehaelter(cls, startZeit, endZeit):
		gehaelter = 0
		for a in cls.objects.all():
			if a.Einstellungsdatum > startZeit:
				continue
			
			if a.Entlassungsdatum != None and a.Entlassungsdatum < endZeit:
				continue
			gehaelter += a.Gehalt
		
		return gehaelter
