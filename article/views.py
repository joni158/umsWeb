from django.shortcuts import render
from .models import Berita, Agenda

# Create your views here.

def home(request):

	item_active = Berita.objects.all()[:3]
	item = Berita.objects.all()[3:6]
	agenda = Agenda.objects.all()[:4]

	context = {
		'item_active':item_active,
		'item':item,
		'agenda':agenda
	}

	templates = "home_v.html"

	return render(request, templates, context)

def berita(request, id_berita=1):

	berita = Berita.objects.get(id_berita=id_berita)
	other_post = Berita.objects.all()[:4]
	agenda = Agenda.objects.all()[:3]

	context = {
		'berita':berita,
		'other_post':other_post,
		'agenda':agenda,
	}

	templates = "single_news.html"

	return render(request, templates, context)