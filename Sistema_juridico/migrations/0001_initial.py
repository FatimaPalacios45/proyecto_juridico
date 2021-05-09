# Generated by Django 2.1 on 2021-05-08 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audiencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalle', models.CharField(max_length=150)),
                ('fecha', models.DateField()),
                ('hora', models.DateTimeField()),
                ('descripcion', models.TextField(max_length=220)),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='Fecha de creacion')),
            ],
            options={
                'verbose_name': 'Audiencia',
                'verbose_name_plural': 'Audiencias',
            },
        ),
        migrations.CreateModel(
            name='Caso',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField(max_length=220)),
                ('estado', models.IntegerField(choices=[(0, 'En Proceso'), (1, 'Finalizado')], default=0)),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='Fecha de creacion')),
                ('audiencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sistema_juridico.Audiencia')),
            ],
            options={
                'verbose_name': 'Caso',
                'verbose_name_plural': 'Casos',
            },
        ),
        migrations.CreateModel(
            name='FormaDePago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=150)),
                ('plazo', models.IntegerField()),
                ('cuota', models.IntegerField()),
                ('monto', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='Fecha de creacion')),
            ],
            options={
                'verbose_name': 'Forma De Pago',
                'verbose_name_plural': 'Forma De Pagos',
            },
        ),
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('direccion', models.CharField(max_length=150)),
                ('descripcion', models.TextField(max_length=220)),
                ('correo', models.EmailField(max_length=150)),
                ('telefono', models.IntegerField()),
                ('tipo', models.CharField(max_length=150)),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='Fecha de creacion')),
            ],
            options={
                'verbose_name': 'Institucion',
                'verbose_name_plural': 'Instituciones',
            },
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('descripcion', models.TextField(max_length=220)),
                ('cargo', models.DecimalField(decimal_places=2, max_digits=5)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=6)),
                ('saldo_total', models.DecimalField(decimal_places=2, max_digits=6)),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='Fecha de creacion')),
                ('tipo_de_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sistema_juridico.FormaDePago')),
            ],
            options={
                'verbose_name': 'Pago',
                'verbose_name_plural': 'Pagos',
            },
        ),
        migrations.CreateModel(
            name='TipoDeAbogado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=220)),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='Fecha de creacion')),
            ],
            options={
                'verbose_name': 'Tipo de abogado',
                'verbose_name_plural': 'Tipos de abogados',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='TipoDeProceso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=220)),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='Fecha de creacion')),
            ],
            options={
                'verbose_name': 'Tipo de proceso',
                'verbose_name_plural': 'Tipos de procesos',
                'ordering': ['nombre'],
            },
        ),
        migrations.AddField(
            model_name='caso',
            name='pago',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sistema_juridico.Pago'),
        ),
        migrations.AddField(
            model_name='caso',
            name='tipo_de_proceso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sistema_juridico.TipoDeProceso'),
        ),
    ]