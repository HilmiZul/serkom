# Generated by Django 2.2.16 on 2020-10-07 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buku',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=50)),
                ('penulis', models.CharField(max_length=40)),
                ('penerbit', models.CharField(max_length=30)),
                ('kelompok', models.CharField(choices=[('Produktif', 'Produktif'), ('Normatif', 'Normatif'), ('Adaptif', 'Adaptif')], max_length=9)),
                ('isbn', models.CharField(max_length=20)),
                ('jumlah', models.IntegerField()),
                ('cover', models.ImageField(upload_to='cover')),
                ('tanggal', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
