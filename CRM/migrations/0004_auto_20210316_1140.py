# Generated by Django 3.1.7 on 2021-03-16 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0003_auto_20210315_2032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comerciales',
            name='SUMA_ACCESORIOS',
        ),
        migrations.RemoveField(
            model_name='comerciales',
            name='SUMA_CAMBIOTECNOLOGIA',
        ),
        migrations.RemoveField(
            model_name='comerciales',
            name='SUMA_CROSS_FijoNuevo',
        ),
        migrations.RemoveField(
            model_name='comerciales',
            name='SUMA_CROSS_FijoPortado',
        ),
        migrations.RemoveField(
            model_name='comerciales',
            name='SUMA_ENERGYGO',
        ),
        migrations.RemoveField(
            model_name='comerciales',
            name='SUMA_FMC_FijoNuevo',
        ),
        migrations.RemoveField(
            model_name='comerciales',
            name='SUMA_FMC_portaFIJO',
        ),
        migrations.RemoveField(
            model_name='comerciales',
            name='SUMA_MOADICIONAL',
        ),
        migrations.RemoveField(
            model_name='comerciales',
            name='SUMA_PEPENERGY',
        ),
        migrations.RemoveField(
            model_name='comerciales',
            name='SUMA_PREPAGO',
        ),
        migrations.RemoveField(
            model_name='comerciales',
            name='SUMA_PospagoMB_DUOMB',
        ),
        migrations.RemoveField(
            model_name='comerciales',
            name='SUMA_PospagoMO',
        ),
        migrations.RemoveField(
            model_name='comerciales',
            name='SUMA_RENUEVO',
        ),
        migrations.RemoveField(
            model_name='comerciales',
            name='SUMA_RENUEVOSUBIDA',
        ),
        migrations.RemoveField(
            model_name='comerciales',
            name='SUMA_SEGURO',
        ),
        migrations.RemoveField(
            model_name='comerciales',
            name='SUMA_SEGURO_FAM',
        ),
        migrations.RemoveField(
            model_name='comerciales',
            name='SUMA_SMARTHOME',
        ),
        migrations.RemoveField(
            model_name='comerciales',
            name='SUMA_TERMLIBRE',
        ),
        migrations.RemoveField(
            model_name='comerciales',
            name='SUMA_TV',
        ),
        migrations.RemoveField(
            model_name='comerciales',
            name='cl_agendado',
        ),
        migrations.RemoveField(
            model_name='comerciales',
            name='cl_llamado',
        ),
        migrations.RemoveField(
            model_name='comerciales',
            name='cl_nocontesta',
        ),
        migrations.RemoveField(
            model_name='comerciales',
            name='cl_noexiste',
        ),
        migrations.RemoveField(
            model_name='comerciales',
            name='cl_nointeresa',
        ),
        migrations.RemoveField(
            model_name='comerciales',
            name='cl_ofertado',
        ),
        migrations.RemoveField(
            model_name='comerciales',
            name='cl_vendido',
        ),
    ]