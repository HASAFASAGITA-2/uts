# Generated by Django 4.1.2 on 2022-10-18 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prodiMtk', '0002_blog_catatanmk_soalmk'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='panulis',
            new_name='penulis',
        ),
    ]