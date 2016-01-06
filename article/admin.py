from django.contrib import admin
from .models import Berita, Agenda

# Register your models here.

class BeritaAdmin(admin.ModelAdmin):
	list_display = ['judul', 'isi', 'gambar_utama', 'url', 'kategori', 'status']

	class Meta:
		model = Berita
		
admin.site.register(Berita, BeritaAdmin)

class AgendaAdmin(admin.ModelAdmin):
	list_display = ['judul', 'tempat', 'tanggal', 'mulai', 'selesai']

	class Meta:
		model = Agenda
		
admin.site.register(Agenda, AgendaAdmin)