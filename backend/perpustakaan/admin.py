from django.contrib import admin
from .models import Buku

class BukuAdmin(admin.ModelAdmin):
  list_display = ['judul', 'penulis', 'kelompok', 'tanggal', 'jumlah']
  list_filter = ('kelompok',)
  search_fields = ['judul', 'penulis', 'penerbit']
  list_per_page = 10

admin.site.register(Buku, BukuAdmin)
