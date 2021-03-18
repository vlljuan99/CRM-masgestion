#!/usr/bin/env python

"""
    Script to import data from .csv file to Model Database DJango
    To execute this script run: 
                                1) manage.py shell
                                2) exec(open('importador.py').read())
"""

import csv
from CRM.models import Clientes, Comerciales

CSV_PATH = './REPORTE.csv'      # Csv file path  

def fechaDecode(fecha):
    try:
        if not fecha: return None
        monthDecode = {
            'ene': '01',
            'feb': '02',
            'mar': '03',
            'abr': '04',
            'may': '05',
            'jun': '06',
            'jul': '07',
            'ago': '08',
            'sep': '09',
            'oct': '10',
            'nov': '11',
            'dic': '12',
            'Jan': '01',
            'Feb': '02',
            'Mar': '03',
            'Apr': '04',
            'May': '05',
            'Jun': '06',
            'Jul': '07',
            'Ago': '08',
            'Aug': '08',
            'Sept': '09',
            'Oct': '10',
            'Nov': '11',
            'Dic': '12',
            'Dec': '12'
        }
        fields = fecha.split('-')
        if len(fields[2]) > 2:
            yr = fields[2][-2:]
        else:
            yr = fields[2]
        year = '20' + yr
        month = monthDecode[fields[1]]
        day = fields[0]
        if len(day) < 2: day = '0' + day

        return year + '-' + month + '-' + day
    except:
        return 0

with open(CSV_PATH, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    i=0
    for row in spamreader:
        # try:
        if i>=2:
            if(fechaDecode(row[2])!=0 and fechaDecode(row[14])!=0 and fechaDecode(row[15])!=0):
                fecha_contacto = fechaDecode(row[2])
                fecha_agendado = fechaDecode(row[14])
                fecha_venta = fechaDecode(row[15])
                # vec=[]
                
                # for j in range(16,34):
                #     if row[j]!='':
                #         vec.append(row[j])
                #     else:
                #         vec.append(0)

                if(Comerciales.objects.filter(nombre=row[3]).count()<=0):
                    comercial=Comerciales.objects.create(nombre=row[3])
                else:
                    comercial=Comerciales.objects.get(nombre=row[3])

                
                Clientes.objects.create(nombre=row[0],origen=row[1],comercial=comercial,fecha_contacto=fecha_contacto,DNI=row[4],segmento=row[5],direccion=row[6],CP=row[7],poblacion=row[8],telefono=row[10],operador=row[11],estado=row[12], fecha_agendado=fecha_agendado, fecha_venta=fecha_venta, FMC_portaFIJO=row[16],FMC_FijoNuevo=row[17],PospagoMO=row[18],PospagoMB_DUOMB=row[19],CROSS_FijoPortado=row[20],CROSS_FijoNuevo=row[21],RENUEVO=row[22],RENUEVOSUBIDA=row[23],TV=row[24],SEGURO=row[25],ACCESORIOS=row[26],TERMLIBRE=row[27],CAMBIOTECNOLOGIA=row[28],PREPAGO=row[29],SEGURO_FAM=row[30],PEPENERGY=row[31],ENERGYGO=row[32],SMARTHOME=row[33],MOADICIONAL=row[34],comentarios=row[35])
                print(i)
                i=i+1
        else:
            i=i+1         
        # except:
        #     print(str(i))
