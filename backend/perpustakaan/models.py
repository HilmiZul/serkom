from django.db import models

# model untuk merepresentasikan tabel Buku
class Buku(models.Model):
  kelompok_choices = (
    ('Produktif', 'Produktif'),
    ('Normatif', 'Normatif'),
    ('Adaptif', 'Adaptif'),
  )
  judul = models.CharField(max_length=50)
  penulis = models.CharField(max_length=40)
  penerbit = models.CharField(max_length=30)
  kelompok = models.CharField(max_length=9, choices=kelompok_choices)
  isbn = models.CharField(max_length=20)
  jumlah = models.IntegerField()
  cover = models.ImageField(upload_to='cover')
  tanggal = models.DateTimeField(auto_now_add=True)
  lokasi = models.CharField(max_length=30, null=True)
  
  def __str__(self):
    return self.judul