# Generated by Django 5.1.1 on 2024-10-02 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notareport', '0003_posisi_jenis_posisi_alter_jenisnota_jenis_nota'),
    ]

    operations = [
        migrations.RenameField(
            model_name='natura',
            old_name='id_posisi',
            new_name='posisi',
        ),
        migrations.AddField(
            model_name='natura',
            name='nama',
            field=models.CharField(default='Isi nama', max_length=255),
        ),
    ]
