from django.contrib import admin

from .models import Angestellter, Projekt

admin.site.register([Angestellter, Projekt])