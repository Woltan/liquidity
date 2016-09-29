from datetime import date, datetime
from django.http import HttpResponseRedirect
from django.views import View
from django.shortcuts import render

from .models import Angestellter, Projekt
from .forms import AngestellterForm, ProjektForm

class IndexView(View):
	def get(self, request):
		projekte = Projekt.objects.all()
		angestellte = Angestellter.objects.all()
		einnahmen = [p.ProjektEinnahmen(date(datetime.today().year, datetime.today().month, 1), 24) for p in projekte]
		gehaelter = [a.Gehaelter(date(datetime.today().year, datetime.today().month, 1), 24) for a in angestellte]
		return render(request, "liquid/index.html", {"projekte": projekte, "angestellte": angestellte, "einnahmen": einnahmen, "gehaelter": gehaelter})

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
			return HttpResponseRedirect("/")
		
		return render(request, "liquid/projekt_form.html", {"form": form})

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
			return HttpResponseRedirect("/")
		
		return render(request, "liquid/angestellter_form.html", {"form": form})
