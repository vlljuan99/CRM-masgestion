from django import forms
from .models import Clientes, Comerciales
from django.utils import timezone



class ClienteForm(forms.ModelForm):
    nombre = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Nombre completo'}), label='Nombre del cliente', required=False) #nombre y apellidos del cliente
    DNI = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'DNI'}), label='DNI', required=False)
    telefono = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Teléfono'}), label='Móvil o Fijo', required=False)
    CP = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Código postal'}), label='Código postal', required=False) #codigo postal
    email = forms.EmailField(widget= forms.TextInput(attrs={'placeholder':'ejemplo@ejemplo.es'}), label='Correo electrónico', required=False)
    provincia = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Provincia'}), label='Provincia', required=False) #nombre y apellidos del cliente
    poblacion = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Población'}), label='Población', required=False)
    direccion = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Dirección completa'}), label='Dirección', required=False)

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

    operador = forms.ChoiceField(label='Operador', choices=OPERADOR, required=False)

    numero = forms.CharField(required=False)
    portal = forms.CharField(required=False)
    escalera = forms.CharField(required=False)
    planta = forms.CharField(required=False)
    puerta = forms.CharField(required=False)
    FMC_portaFIJO = forms.IntegerField(required=False)
    FMC_FijoNuevo = forms.IntegerField(required=False)
    PospagoMO = forms.IntegerField(required=False)
    PospagoMB_DUOMB = forms.IntegerField(required=False)
    CROSS_FijoPortado = forms.IntegerField(required=False)
    CROSS_FijoNuevo = forms.IntegerField(required=False)
    RENUEVO = forms.IntegerField(required=False)
    RENUEVOSUBIDA = forms.IntegerField(required=False)
    TV = forms.IntegerField(required=False)
    SEGURO = forms.IntegerField(required=False)
    ACCESORIOS = forms.IntegerField(required=False)
    TERMLIBRE = forms.IntegerField(required=False)
    CAMBIOTECNOLOGIA = forms.IntegerField(required=False)
    PREPAGO = forms.IntegerField(required=False)
    SEGURO_FAM = forms.IntegerField(required=False)
    PEPENERGY = forms.IntegerField(required=False)
    ENERGYGO = forms.IntegerField(required=False)
    SMARTHOME = forms.IntegerField(required=False)
    MOADICIONAL = forms.IntegerField(required=False)

    # fecha_contacto = forms.DateField(widget=DateTimePicker(options={"format": "YYYY-MM-DD", "pickTime": False}))
    fecha_contacto = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),label='fecha contacto', required=False)
    fecha_venta = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),label='fecha venta', required=False)
    fecha_agendado = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),label='fecha agendado', required=False)

    REFERENCIADO = 'Cliente referenciado'
    CLIENTE_TIENDA = 'Cliente de tienda'
    CLIENTE_CARTERA = 'Cliente de cartera'
    ORIGEN = [
        (REFERENCIADO, 'Cliente referenciado'),
        (CLIENTE_TIENDA, 'Cliente de tienda'),
        (CLIENTE_CARTERA, 'Cliente de cartera'),
    ]
    origen = forms.ChoiceField(label='Origen', choices=ORIGEN, required=False)

    EMPRESA = 'Empresa'
    PARTICULAR = 'Particular'
    AUTONOMO = 'Autónomo'
    SEGMENTO = [
        (EMPRESA, 'Empresa'),
        (PARTICULAR, 'Particular'),
        (AUTONOMO, 'Autónomo'),
    ]
    segmento = forms.ChoiceField(choices=SEGMENTO, required=False)

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

    estado = forms.ChoiceField(choices=ESTADO, required=False)

    comentarios = forms.CharField(widget=forms.Textarea, required=False)

    comercial = forms.ModelChoiceField(queryset=Comerciales.objects.all(), required=False)



    class Meta:
        model = Clientes
        fields = ['nombre', 'DNI', 'telefono', 'CP', 'provincia', 'email', 'operador', 'comercial',
                  'poblacion', 'direccion', 'numero', 'portal', 'escalera',
                  'planta', 'puerta', 'fecha_contacto', 'fecha_agendado',
                  'fecha_venta', 'origen', 'segmento', 'estado', 'FMC_portaFIJO', 'FMC_FijoNuevo', 'PospagoMO', 'PospagoMB_DUOMB', 'CROSS_FijoPortado',
                  'CROSS_FijoNuevo', 'RENUEVO', 'RENUEVOSUBIDA', 'TV', 'SEGURO', 'ACCESORIOS', 'TERMLIBRE', 'CAMBIOTECNOLOGIA',
                  'PREPAGO', 'SEGURO_FAM', 'PEPENERGY', 'ENERGYGO', 'SMARTHOME', 'MOADICIONAL', 'comentarios']



class BuscaCliente(forms.ModelForm):

    FMC_portaFIJO = 'FMC_portaFIJO'
    FMC_FijoNuevo = 'FMC_FijoNuevo'
    PospagoMO = 'PospagoMO'
    PospagoMB_DUOMB = 'PospagoMB_DUOMB'
    CROSS_FijoPortado = 'CROSS_FijoPortado'
    CROSS_FijoNuevo = 'CROSS_FijoNuevo'
    RENUEVO = 'RENUEVO'
    RENUEVOSUBIDA = 'RENUEVOSUBIDA'
    TV = 'TV'
    SEGURO = 'SEGURO'
    ACCESORIOS = 'ACCESORIOS'


    CONTRATACIONES = [
        (FMC_portaFIJO, 'FMC_portaFijo'),
        (FMC_FijoNuevo, 'FMC_FijoNuevo'),
        (PospagoMO, 'PospagoMO'),
        (PospagoMB_DUOMB, 'PospagoMB_DUOMB'),
        (CROSS_FijoPortado, 'CROSS_FijoPortado'),
        (CROSS_FijoNuevo, 'CROSS_FijoNuevo'),
        (RENUEVO, 'RENUEVO'),
        (RENUEVOSUBIDA, 'RENUEVOSUBIDA'),
        (TV, 'TV'),
        (SEGURO, 'SEGURO'),
        (ACCESORIOS, 'ACCESORIOS')
    ]

    contrataciones = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=CONTRATACIONES, required=False, label='contrataciones')

    class Meta:
        model = Clientes
        fields = ['nombre', 'DNI', 'telefono', 'CP', 'email', 'provincia', 'contrataciones',
                  'poblacion', 'direccion', 'numero', 'portal', 'escalera',
                  'planta', 'puerta', 'fecha_contacto', 'fecha_agendado',
                  'fecha_venta', 'origen', 'segmento', 'estado', 'FMC_portaFIJO', 'FMC_FijoNuevo', 'PospagoMO', 'PospagoMB_DUOMB', 'CROSS_FijoPortado',
                  'CROSS_FijoNuevo', 'RENUEVO', 'RENUEVOSUBIDA', 'TV', 'SEGURO', 'ACCESORIOS', 'TERMLIBRE', 'CAMBIOTECNOLOGIA',
                  'PREPAGO', 'SEGURO_FAM', 'PEPENERGY', 'ENERGYGO', 'SMARTHOME', 'MOADICIONAL']
