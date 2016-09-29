from django import forms
from .models import Angestellter, Projekt

class ProjektForm(forms.ModelForm):
	class Meta:
		model = Projekt
		fields = "__all__"
		widgets = {
				"Startdatum": forms.SelectDateWidget(years=range(2015, 2020)),
				"Enddatum": forms.SelectDateWidget(years=range(2015, 2020)),
				}
	def clean(self):
		cleaned_data = super(ProjektForm, self).clean()
		
		if cleaned_data["Enddatum"] <= cleaned_data["Startdatum"]:
			raise forms.ValidationError("Startdatum muss vor dem Enddatum sein.")
		
		return cleaned_data
	
class AngestellterForm(forms.ModelForm):
	class Meta:
		model = Angestellter
		fields = "__all__"
		widgets = {
				"Einstellungsdatum": forms.SelectDateWidget(years=range(2015, 2020)),
				"Entlassungsdatum": forms.SelectDateWidget(years=range(2015, 2020)),
				}
