# Generated by Django 5.1.1 on 2024-10-03 07:18
# Generated by Django 4.2.16 on 2024-10-03 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JenisNota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenis_nota', models.CharField(choices=[('BBM', 'BBM'), ('Non-BBM', 'Non-BBM')], default='default_value', max_length=255)),
                ('nama_nota', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'JenisNota',
                'verbose_name_plural': 'JenisNota',
            },
        ),
        migrations.CreateModel(
            name='Naker',
            fields=[
                ('nik', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=255)),
                ('witel', models.CharField(choices=[('Malang', 'Malang'), ('Kediri', 'Kediri'), ('Madiun', 'Madiun')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Naker',
                'verbose_name_plural': 'Naker',
            },
        ),
        migrations.CreateModel(
            name='Posisi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenis_posisi', models.CharField(choices=[('Manager', 'Manager'), ('AssMAN', 'AssMAN'), ('Supervisor', 'Supervisor'), ('Team Leader', 'Team Leader'), ('Staff', 'Staff'), ('Helpdesk', 'Helpdesk'), ('Teknisi', 'Teknisi')], default='Pilih Posisi', max_length=225)),
                ('nama_posisi', models.CharField(max_length=225, unique=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Posisi',
                'verbose_name_plural': 'Posisi',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_project', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Project',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_role', models.CharField(max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Role',
                'verbose_name_plural': 'Role',
            },
        ),
        migrations.CreateModel(
            name='Sto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nama_sto', models.CharField(max_length=255)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'STO',
                'verbose_name_plural': 'STO',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_unit', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Unit',
                'verbose_name_plural': 'Unit',
            },
        ),
        migrations.CreateModel(
            name='TransaksiNonBBM',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tgl_nota', models.DateField(blank=True, null=True)),
                ('nominal', models.IntegerField()),
                ('foto_nota', models.ImageField(upload_to='notas/')),
                ('foto_evidence', models.ImageField(upload_to='evidences/')),
                ('uraian_kegiatan', models.TextField()),
                ('status', models.CharField(choices=[('rejected', 'Rejected'), ('processed', 'Processed'), ('verified', 'Verified'), ('paid', 'Paid')], default='Proccessed', max_length=10)),
                ('status_changed_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('jenis_nota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notareport.jenisnota')),
                ('nik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notareport.naker')),
                ('sto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notareport.sto')),
            ],
            options={
                'verbose_name': 'TransaksiNonBBM',
                'verbose_name_plural': 'TransaksiNonBBM',
            },
        ),
        migrations.CreateModel(
            name='TransaksiBBM',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tgl_nota', models.DateField()),
                ('jenis_KBM', models.CharField(choices=[('R2', 'R2'), ('R4', 'R4')], max_length=2)),
                ('no_polisi', models.CharField(max_length=20)),
                ('km', models.CharField(max_length=20)),
                ('nominal', models.IntegerField()),
                ('foto_nota', models.ImageField(upload_to='notas/')),
                ('foto_odo', models.ImageField(upload_to='odos/')),
                ('uraian_kegiatan', models.TextField()),
                ('status', models.CharField(choices=[('rejected', 'Rejected'), ('processed', 'Processed'), ('verified', 'Verified'), ('paid', 'Paid')], default='Proccessed', max_length=10)),
                ('status_changed_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id_jenis_nota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notareport.jenisnota')),
                ('id_sto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notareport.sto')),
                ('nik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notareport.naker')),
            ],
            options={
                'verbose_name': 'TransaksiBBM',
                'verbose_name_plural': 'TransaksiBBM',
            },
        ),
        migrations.CreateModel(
            name='Natura',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nama', models.CharField(default='Isi nama', max_length=255)),
                ('witel', models.CharField(choices=[('Malang', 'Malang'), ('Kediri', 'Kediri'), ('Madiun', 'Madiun')], max_length=10)),
                ('km_referensi', models.DecimalField(decimal_places=2, max_digits=10)),
                ('km_liter', models.DecimalField(decimal_places=2, max_digits=10)),
                ('harga_bensin', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('nik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notareport.naker')),
                ('posisi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notareport.posisi', to_field='nama_posisi')),
            ],
            options={
                'verbose_name': 'Natura',
                'verbose_name_plural': 'Natura',
            },
        ),
        migrations.AddField(
            model_name='naker',
            name='posisi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notareport.posisi'),
        ),
        migrations.AddField(
            model_name='naker',
            name='role',
            field=models.ForeignKey(default='default_value', on_delete=django.db.models.deletion.CASCADE, to='notareport.role', to_field='nama_role'),
        ),
        migrations.AddField(
            model_name='naker',
            name='sto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notareport.sto'),
        ),
        migrations.AddField(
            model_name='naker',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notareport.unit'),
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, unique=True)),
                ('nik', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='notareport.naker')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Kendaraan',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tgl_pendataan', models.DateTimeField(auto_now_add=True)),
                ('witel', models.CharField(choices=[('Malang', 'Malang'), ('Kediri', 'Kediri'), ('Madiun', 'Madiun')], max_length=10)),
                ('jenis_KBM', models.CharField(choices=[('R2', 'R2'), ('R4', 'R4')], max_length=2)),
                ('merk_type_KBM', models.CharField(choices=[('Honda Beat', 'Honda Beat'), ('Mitsubishi Expander', 'Mitsubishi Expander')], max_length=100)),
                ('no_polisi', models.CharField(max_length=20)),
                ('odometer', models.CharField(max_length=20)),
                ('foto_speedometer', models.ImageField(upload_to='speedometers/')),
                ('foto_tampak_depan', models.ImageField(upload_to='kendaraan/depan/')),
                ('foto_tampak_samping', models.ImageField(upload_to='kendaraan/samping/')),
                ('tgl_tempo_STNK_5thn', models.DateField()),
                ('tgl_service_terakhir', models.DateField()),
                ('kondisi_kendaraan', models.CharField(blank=True, max_length=100, null=True)),
                ('foto_kondisi_kendaraan', models.ImageField(blank=True, null=True, upload_to='kendaraan/kondisi/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('nik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kendaraan_nik', to='notareport.naker')),
                ('nik_pengguna_kbm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kendaraan_pengguna', to='notareport.naker')),
            ],
            options={
                'verbose_name': 'Kendaraan',
                'verbose_name_plural': 'Kendaraan',
            },
        ),
        migrations.CreateModel(
            name='Natura',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('witel', models.CharField(choices=[('Malang', 'Malang'), ('Kediri', 'Kediri'), ('Madiun', 'Madiun')], max_length=10)),
                ('km_referensi', models.CharField(max_length=20)),
                ('km_liter', models.CharField(max_length=20)),
                ('harga_bensin', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('nik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notareport.naker')),
                ('id_posisi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notareport.posisi')),
            ],
            options={
                'verbose_name': 'Natura',
                'verbose_name_plural': 'Natura',
            },
        ),
        migrations.AddField(
            model_name='naker',
            name='posisi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notareport.posisi'),
        ),
        migrations.AddField(
            model_name='naker',
            name='role',
            field=models.ForeignKey(default='default_value', on_delete=django.db.models.deletion.CASCADE, to='notareport.role'),
        ),
        migrations.AddField(
            model_name='naker',
            name='sto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notareport.sto'),
        ),
        migrations.CreateModel(
            name='TransaksiBBM',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tgl_nota', models.DateField()),
                ('jenis_KBM', models.CharField(choices=[('R2', 'R2'), ('R4', 'R4')], max_length=2)),
                ('no_polisi', models.CharField(max_length=20)),
                ('km', models.CharField(max_length=20)),
                ('nominal', models.IntegerField()),
                ('foto_nota', models.ImageField(upload_to='notas/')),
                ('foto_odo', models.ImageField(upload_to='odos/')),
                ('uraian_kegiatan', models.TextField()),
                ('status', models.CharField(choices=[('rejected', 'Rejected'), ('processed', 'Processed'), ('verified', 'Verified'), ('paid', 'Paid')], default='Proccessed', max_length=10)),
                ('status_changed_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id_jenis_nota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notareport.jenisnota')),
                ('id_sto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notareport.sto')),
                ('nik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notareport.naker')),
            ],
            options={
                'verbose_name': 'TransaksiBBM',
                'verbose_name_plural': 'TransaksiBBM',
            },
        ),
        migrations.CreateModel(
            name='TransaksiNonBBM',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tgl_nota', models.DateField(blank=True, null=True)),
                ('nominal', models.IntegerField()),
                ('foto_nota', models.ImageField(upload_to='notas/')),
                ('foto_evidence', models.ImageField(upload_to='evidences/')),
                ('uraian_kegiatan', models.TextField()),
                ('status', models.CharField(choices=[('rejected', 'Rejected'), ('processed', 'Processed'), ('verified', 'Verified'), ('paid', 'Paid')], default='Proccessed', max_length=10)),
                ('status_changed_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('jenis_nota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notareport.jenisnota')),
                ('nik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notareport.naker')),
                ('sto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notareport.sto')),
            ],
            options={
                'verbose_name': 'TransaksiNonBBM',
                'verbose_name_plural': 'TransaksiNonBBM',
            },
        ),
        migrations.AddField(
            model_name='naker',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notareport.unit'),
        ),
    ]
