from django.conf.urls import url

from .views import IndexView, projekte

urlpatterns = [
	url(r'index/$', IndexView.as_view()),
	url(r'projekte/$', projekte),
]