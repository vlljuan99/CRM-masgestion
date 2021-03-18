from django.db import models
from django.utils import timezone
# Aquí creamos las BBDD como si fueran básicamente clases

class Clientes(models.Model):

    REFERENCIADO = 'Cliente referenciado'
    CLIENTE_TIENDA = 'Cliente de tienda'
    CLIENTE_CARTERA = 'Cliente de cartera'
    ORIGEN = [
        (REFERENCIADO, 'Cliente referenciado'),
        (CLIENTE_TIENDA, 'Cliente de tienda'),
        (CLIENTE_CARTERA, 'Cliente de cartera'),
    ]

    EMPRESA = 'Empresa'
    PARTICULAR = 'Particular'
    AUTONOMO = 'Autónomo'
    SEGMENTO = [
        (EMPRESA, 'Empresa'),
        (PARTICULAR, 'Particular'),
        (AUTONOMO, 'Autónomo'),
    ]

    LLAMADO = 'Llamado'
    OFERTADO = 'Ofertado'
    AGENDADO = 'Agendado'
    NOCONTESTA = 'No contesta'
    NOINTERESA = 'No interesa'
    VENDIDO = 'Vendido'
    NOEXISTE = 'No existe'
    ESTADO = [
        (LLAMADO, 'Llamado'),
        (OFERTADO, 'Ofertado'),
        (AGENDADO, 'Agendado'),
        (NOCONTESTA, 'No contesta'),
        (NOINTERESA, 'No interesa'),
        (VENDIDO, 'Vendido'),
        (NOEXISTE, 'No existe')
    ]

    YOIGO = 'Yoigo'
    JAZZTEL = 'Jazztel'
    DIGI = 'Digi'
    MOVISTAR = 'Movistar'
    ORANGE = 'Orange'
    MASMOVIL = 'MasMovil'
    VODAFONE = 'Vodafone'
    PEPEPHONE = 'Pepephone'
    LOWI = 'Lowi'
    LEBARA = 'Lebara'
    LLAMAYA = 'Llamaya'
    OTROS = 'Otros'

    OPERADOR = [
    (YOIGO, 'Yoigo'),
    (JAZZTEL, 'Jazztel'),
    (DIGI, 'Digi'),
    (MOVISTAR, 'Movistar'),
    (ORANGE, 'Orange'),
    (MASMOVIL, 'MasMovil'),
    (VODAFONE, 'Vodafone'),
    (PEPEPHONE, 'Pepephone'),
    (LOWI, 'Lowi'),
    (LEBARA, 'Lebara'),
    (LLAMAYA, 'Llamaya'),
    (OTROS, 'Otros')
    ]

    #delete system

    id = models.AutoField(primary_key=True, default=None)

    nombre = models.CharField(
        max_length=200,
        default=None,
        null=True
    )
    
    DNI = models.CharField(
        max_length=15,
        default=None,
        null=True
    )

    telefono = models.CharField(
        max_length=25,
        default=None,
        null=True
    )

    email = models.EmailField(
        max_length = 100,
        default=None,
        null=True
    )

    comercial = models.ForeignKey(
        'Comerciales',
        on_delete=models.CASCADE,
        default=None
    )

    # comercial = models.CharField(
    #     max_length=15,
    #     default=None,
    #     null=True
    # )

    CP = models.CharField(
        max_length=10,
        default=None,
        null=True
    )

    provincia = models.CharField(
        max_length=50,
        default=None,
        null=True
    )

    poblacion = models.CharField(
        max_length=50,
        default=None,
        null=True
    )

    direccion = models.CharField(
        max_length=200,
        default=None,
        null=True
    )

    numero = models.CharField(
        max_length=15,
        default=None,
        null=True
    )

    portal = models.CharField(
        max_length=15,
        default=None,
        null=True
    )

    escalera = models.CharField(
        max_length=15,
        default=None,
        null=True
    )

    planta = models.CharField(
        max_length=15,
        default=None,
        null=True
    )

    puerta = models.CharField(
        max_length=15,
        default=None,
        null=True
    )

    fecha_contacto = models.DateField(
        default=timezone.now,
        null=True
    )

    fecha_venta = models.DateField(
        default=timezone.now,
        null=True
    )
    
    fecha_agendado = models.DateField(
        default=timezone.now,
        null=True
    )

    origen = models.CharField(
        max_length=50,
        choices=ORIGEN,
        default=REFERENCIADO,
        null=True
    )
    segmento = models.CharField(
        max_length=50,
        choices=SEGMENTO,
        default=PARTICULAR,
        null=True
    )

    estado = models.CharField(
        max_length=50,
        choices=ESTADO,
        default=AGENDADO,
        null=True
    )

    operador = models.CharField(
        max_length=50,
        choices=OPERADOR,
        default=MASMOVIL,
        null=True
    )

    FMC_portaFIJO = models.PositiveSmallIntegerField(
        null=True,
        default=0
    )

    FMC_FijoNuevo = models.PositiveSmallIntegerField(
        null=True,
        default=0
    )

    PospagoMO = models.PositiveSmallIntegerField(
        null=True,
        default=0
    )

    PospagoMB_DUOMB = models.PositiveSmallIntegerField(
        null=True,
        default=0
    )

    CROSS_FijoPortado = models.PositiveSmallIntegerField(
        null=True,
        default=0
    )

    CROSS_FijoNuevo = models.PositiveSmallIntegerField(
        null=True,
        default=0
    )

    RENUEVO = models.PositiveSmallIntegerField(
        null=True,
        default=0
    )

    RENUEVOSUBIDA = models.PositiveSmallIntegerField(
        null=True,
        default=0
    )

    TV = models.PositiveSmallIntegerField(
        null=True,
        default=0
    )

    SEGURO = models.PositiveSmallIntegerField(
        null=True,
        default=0
    )

    ACCESORIOS = models.PositiveSmallIntegerField(
        null=True,
        default=0
    )

    TERMLIBRE = models.PositiveSmallIntegerField(
        null=True,
        default=0
    )

    CAMBIOTECNOLOGIA = models.PositiveSmallIntegerField(
        null=True,
        default=0
    )

    PREPAGO = models.PositiveSmallIntegerField(
        null=True,
        default=0
    )

    SEGURO_FAM = models.PositiveSmallIntegerField(
        null=True,
        default=0
    )

    PEPENERGY = models.PositiveSmallIntegerField(
        null=True,
        default=0
    )

    ENERGYGO = models.PositiveSmallIntegerField(
        null=True,
        default=0
    )

    SMARTHOME = models.PositiveSmallIntegerField(
        null=True,
        default=0
    )

    MOADICIONAL = models.PositiveSmallIntegerField(
        null=True,
        default=0
    )

    comentarios = models.TextField(
        default=None,
        null=True
    )


class Comerciales(models.Model):
    id = models.AutoField(primary_key=True)

    nombre = models.CharField(
        max_length=200,
        unique=True,
        default=None
    )

    # cl_agendado = models.PositiveSmallIntegerField(null=True)

    # cl_llamado = models.PositiveSmallIntegerField(null=True)

    # cl_nocontesta = models.PositiveSmallIntegerField(null=True)

    # cl_noexiste = models.PositiveSmallIntegerField(null=True)

    # cl_nointeresa = models.PositiveSmallIntegerField(null=True)

    # cl_ofertado = models.PositiveSmallIntegerField(null=True)

    # cl_vendido = models.PositiveSmallIntegerField(null=True)

    # SUMA_FMC_portaFIJO = models.PositiveSmallIntegerField(null=True)

    # SUMA_FMC_FijoNuevo = models.PositiveSmallIntegerField(null=True)

    # SUMA_PospagoMO = models.PositiveSmallIntegerField(null=True)

    # SUMA_PospagoMB_DUOMB = models.PositiveSmallIntegerField(null=True)

    # SUMA_CROSS_FijoPortado = models.PositiveSmallIntegerField(null=True)

    # SUMA_CROSS_FijoNuevo = models.PositiveSmallIntegerField(null=True)

    # SUMA_RENUEVO = models.PositiveSmallIntegerField(null=True)

    # SUMA_RENUEVOSUBIDA = models.PositiveSmallIntegerField(null=True)

    # SUMA_TV = models.PositiveSmallIntegerField(null=True)

    # SUMA_SEGURO = models.PositiveSmallIntegerField(null=True)

    # SUMA_ACCESORIOS = models.PositiveSmallIntegerField(null=True)

    # SUMA_TERMLIBRE = models.PositiveSmallIntegerField(null=True)

    # SUMA_CAMBIOTECNOLOGIA = models.PositiveSmallIntegerField(null=True)

    # SUMA_PREPAGO = models.PositiveSmallIntegerField(null=True)

    # SUMA_SEGURO_FAM = models.PositiveSmallIntegerField(null=True)

    # SUMA_PEPENERGY = models.PositiveSmallIntegerField(null=True)

    # SUMA_ENERGYGO = models.PositiveSmallIntegerField(null=True)

    # SUMA_SMARTHOME = models.PositiveSmallIntegerField(null=True)

    # SUMA_MOADICIONAL = models.PositiveSmallIntegerField(null=True)


    
