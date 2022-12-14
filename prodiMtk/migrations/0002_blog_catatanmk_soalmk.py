# Generated by Django 4.1.2 on 2022-10-18 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prodiMtk', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=200)),
                ('isi', models.CharField(max_length=200)),
                ('panulis', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='CatatanMk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_mk', models.CharField(max_length=200)),
                ('nama_mk', models.CharField(max_length=200)),
                ('catatan_mk', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='SoalMk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_mk', models.CharField(max_length=200)),
                ('nama_mk', models.CharField(max_length=200)),
                ('soal_mk', models.CharField(max_length=500)),
            ],
        ),
    ]
