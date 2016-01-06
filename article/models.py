# Avoid importing `importlib` from this package

from django.db import models


KATEGORI = (
		('Berita Utama/ Standard', 'Berita Utama/ Standard'),
		('Slide News', 'Slide News'),
		('Karir/ Lowongan Kerja', 'Karir/ Lowongan Kerja')
	)

STATUS = (
		('P', 'Publish'),
		('U', 'Unpublish')
	)

class Berita(models.Model):
	id_berita = models.AutoField(primary_key=True)
	judul = models.CharField(max_length=100)
	isi = models.TextField()
	gambar_utama = models.FileField(upload_to='static/images/news/', blank=True)
	kategori = models.CharField(max_length=100, null=True, choices=KATEGORI, default='Berita Utama/ Standard')
	url = models.CharField(max_length=255, blank=True)
	status = models.CharField(max_length=20, null=True, choices=STATUS, default='P')

	tanggal_post = models.DateTimeField(auto_now_add=True, auto_now=False)
	tangal_update = models.DateTimeField(auto_now_add=False, auto_now=True)

	class Meta:
		db_table = "Berita"
		ordering = ("-tangal_update","judul")

	def __str__(self):
		return self.judul


class Agenda(models.Model):
	id_agenda = models.AutoField(primary_key=True)
	judul = models.CharField(max_length=100)
	tempat = models.CharField(max_length=100)
	tanggal = models.DateField(auto_now=False, auto_now_add=False, null=True)
	mulai = models.TimeField(auto_now=False, auto_now_add=False)
	selesai = models.TimeField(auto_now=False, auto_now_add=False)

	tanggal_post = models.DateTimeField(auto_now_add=True, auto_now=False)
	tangal_update = models.DateTimeField(auto_now_add=False, auto_now=True)

	class Meta:
		db_table = "Agenda"
		ordering = ("-tangal_update","judul")

	def __str__(self):
		return self.judul