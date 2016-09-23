from datetime import date
from django.http import HttpResponseRedirect
from django.views import View
from django.shortcuts import render

from .models import Angestellter, Projekt
from .forms import AngestellterForm, ProjektForm

class IndexView(View):
	def get(self, request):
		currDatum = date(date.today().year, date.today().month, 1)
		kontoverlauf = [0]
		for _ in range(24):
			nextDatum = date(currDatum.year if currDatum.month < 12 else currDatum.year + 1,
							 currDatum.month + 1 if currDatum.month < 12 else 1, 1)
			
			kontoverlauf.append(kontoverlauf[-1] - Angestellter.Gehaelter(currDatum, nextDatum) + Projekt.ProjektEinnahmen(currDatum, nextDatum))
			currDatum = nextDatum
			
		return render(request, "liquid/index.html", {"kontoverlauf": kontoverlauf})

class ProjekteView(View):
	def get(self, request):
		return render(request, "liquid/projekte.html", {"projekte": Projekt.objects.all()})

class ProjektView(View):
	def get(self, request, p_id=""):
		if p_id == "":
			form = ProjektForm()
			projekt = None
		else:
			projekt = Projekt.objects.get(pk=int(p_id))
			form = ProjektForm(instance=projekt)
		return render(request, "liquid/projekt_form.html", {"form": form, "projekt": projekt})
	
	def post(self, request, p_id=None):
		form = ProjektForm(request.POST, instance=Projekt.objects.get(pk=int(p_id)) if p_id != "" else None)
		
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/projekte")
		
		return render(request, "liquid/projekt_form.html", {"form": form})

class AngestellteView(View):
	def get(self, request):
		return render(request, "liquid/angestellte.html", {"angestellte": Angestellter.objects.all()})

class AngestellterView(View):
	def get(self, request, a_id=""):
		if a_id == "":
			form = AngestellterForm()
			angestellter = None
		else:
			angestellter = Angestellter.objects.get(pk=int(a_id))
			form = AngestellterForm(instance=angestellter)
		return render(request, "liquid/angestellter_form.html", {"form": form, "angestellter": angestellter})
	
	def post(self, request, a_id=None):
		form = AngestellterForm(request.POST, instance=Angestellter.objects.get(pk=int(a_id)) if a_id != "" else None)
		
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/angestellte")
		
		return render(request, "liquid/angestellter_form.html", {"form": form})
