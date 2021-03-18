from django.shortcuts import render
from django.http import HttpResponse
from .models import Clientes, Comerciales
from .forms import ClienteForm, BuscaCliente
from django.db.models import Q
from django.core.paginator import Paginator
import csv

# Create your views here.

MESES = {
    'enero' : '-01-',
    'febrero' : '-02-',
    'marzo' : '-03-',
    'abril' : '-04-',
    'mayo' : '-05-',
    'junio' : '-06-',
    'julio' : '-07-',
    'agosto' : '-08-',
    'septiembre' : '-09-',
    'octubre' : '-10-',
    'noviembre' : '-11-',
    'diciembre' : '-12-'
}

def lista_clientes(request):
    busqueda = request.POST.get("search", "")
    if(request.method=='POST' and busqueda is not None):
        if busqueda.lower() in MESES.keys():
            mes = MESES[busqueda]
            clientes = Clientes.objects.filter(fecha_agendado__contains=mes) | Clientes.objects.filter(fecha_venta__contains=mes) | Clientes.objects.filter(fecha_contacto__contains=mes)
        else:
            clientes = Clientes.objects.filter(nombre__contains=busqueda) | Clientes.objects.filter(DNI__contains=busqueda) | Clientes.objects.filter(email__contains=busqueda) | Clientes.objects.filter(telefono__contains=busqueda) | Clientes.objects.filter(CP__contains=busqueda) | Clientes.objects.filter(provincia__contains=busqueda) | Clientes.objects.filter(poblacion__contains=busqueda) | Clientes.objects.filter(direccion__contains=busqueda) | Clientes.objects.filter(CP=busqueda) | Clientes.objects.filter(comercial__nombre__contains=busqueda)     
    else:
        clientes = Clientes.objects.get_queryset().order_by('nombre')
    
    paginator = Paginator(clientes, 25)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"page_obj":page_obj}
    return render(request, 'clientes.html', context)

def lista_comerciales(request):
    clientes = Clientes.objects.all()
    busqueda = request.POST.get("search", "")
    desde = request.POST.get("desde", "")
    hasta = request.POST.get("hasta", "")
    datos = {}

    consulta=consulta1=consulta2=Q()

    if(request.method=='POST' and busqueda != ""):
        if(desde != ""):
            consulta=Q(fecha_contacto__gte=desde)
        if(hasta != ""):
            consulta1=Q(fecha_contacto__lte=hasta)

        comerciales = Comerciales.objects.filter(nombre__contains=busqueda)

        for com in comerciales:
            comercial = dict(
                    ID = com.id,
                    NOMBRE = com.nombre,
                    AGENDADOS = Clientes.objects.filter(Q(comercial=com.id)&Q(estado='AGENDADO')&consulta&consulta1).count(),
                    LLAMADOS = Clientes.objects.filter(Q(comercial=com.id)&Q(estado='LLAMADO')&consulta&consulta1).count(),
                    OFERTADOS = Clientes.objects.filter(Q(comercial=com.id)&Q(estado='OFERTADO')&consulta&consulta1).count(),
                    NOCONTESTA = Clientes.objects.filter(Q(comercial=com.id)&Q(estado='NO CONTESTA')&consulta&consulta1).count(),
                    NOINTERESA = Clientes.objects.filter(Q(comercial=com.id)&Q(estado='NO INTERESADO')&consulta&consulta1).count(),
                    VENDIDO = Clientes.objects.filter(Q(comercial=com.id)&Q(estado='VENDIDO')&consulta&consulta1).count(),
                    NOEXISTE = Clientes.objects.filter(Q(comercial=com.id)&Q(estado='NO EXISTE')&consulta&consulta1).count(),
                    GENERAL = 0,
                    VENTAVALOR = Clientes.objects.filter( Q(comercial=com.id) & Q(estado='VENDIDO')&consulta&consulta1).count(),
                    VENTASTOTALES = Clientes.objects.filter( Q(comercial=com.id) & ((Q(FMC_portaFIJO__gt=0) | Q(FMC_FijoNuevo__gt=0) | Q(PospagoMO__gt=0) | Q(PospagoMB_DUOMB__gt=0) | Q(CROSS_FijoPortado__gt=0) | Q(CROSS_FijoNuevo__gt=0) | Q(RENUEVO__gt=0) | Q(RENUEVOSUBIDA__gt=0) | Q(TV__gt=0) | Q(SEGURO__gt=0) | Q(ACCESORIOS__gt=0) | Q(TERMLIBRE__gt=0) | Q(CAMBIOTECNOLOGIA__gt=0) | Q(PREPAGO__gt=0) | Q(SEGURO_FAM__gt=0) | Q(PEPENERGY__gt=0) | Q(ENERGYGO__gt=0) | Q(SMARTHOME__gt=0) | Q(MOADICIONAL__gt=0)) & consulta & consulta1 )).count(),
            )

            general = comercial['AGENDADOS'] + comercial['LLAMADOS'] + comercial['OFERTADOS'] + comercial['NOCONTESTA'] + comercial['NOINTERESA'] + comercial['VENDIDO'] + comercial['NOEXISTE']
            comercial['GENERAL'] = general

            datos[com.nombre] = comercial
    else:
        todos = Comerciales.objects.all()

        if(desde != ""):
            consulta=Q(fecha_contacto__gte=desde)
        if(hasta != ""):
            consulta1=Q(fecha_contacto__lte=hasta)

        for com in todos:
            comercial = dict(
                ID = com.id,
                NOMBRE = com.nombre,
                AGENDADOS = Clientes.objects.filter(Q(comercial=com.id)&Q(estado='AGENDADO')&consulta&consulta1).count(),
                LLAMADOS = Clientes.objects.filter(Q(comercial=com.id)&Q(estado='LLAMADO')&consulta&consulta1).count(),
                OFERTADOS = Clientes.objects.filter(Q(comercial=com.id)&Q(estado='OFERTADO')&consulta&consulta1).count(),
                NOCONTESTA = Clientes.objects.filter(Q(comercial=com.id)&Q(estado='NO CONTESTA')&consulta&consulta1).count(),
                NOINTERESA = Clientes.objects.filter(Q(comercial=com.id)&Q(estado='NO INTERESADO')&consulta&consulta1).count(),
                VENDIDO = Clientes.objects.filter(Q(comercial=com.id)&Q(estado='VENDIDO')&consulta&consulta1).count(),
                NOEXISTE = Clientes.objects.filter(Q(comercial=com.id)&Q(estado='NO EXISTE')&consulta&consulta1).count(),
                GENERAL = 0,
                VENTAVALOR = Clientes.objects.filter( Q(comercial=com.id) & Q(estado='VENDIDO')&consulta&consulta1).count(),
                VENTASTOTALES = Clientes.objects.filter( Q(comercial=com.id) & ((Q(FMC_portaFIJO__gt=0) | Q(FMC_FijoNuevo__gt=0) | Q(PospagoMO__gt=0) | Q(PospagoMB_DUOMB__gt=0) | Q(CROSS_FijoPortado__gt=0) | Q(CROSS_FijoNuevo__gt=0) | Q(RENUEVO__gt=0) | Q(RENUEVOSUBIDA__gt=0) | Q(TV__gt=0) | Q(SEGURO__gt=0) | Q(ACCESORIOS__gt=0) | Q(TERMLIBRE__gt=0) | Q(CAMBIOTECNOLOGIA__gt=0) | Q(PREPAGO__gt=0) | Q(SEGURO_FAM__gt=0) | Q(PEPENERGY__gt=0) | Q(ENERGYGO__gt=0) | Q(SMARTHOME__gt=0) | Q(MOADICIONAL__gt=0)) & consulta & consulta1 )).count(),
            )

            general = comercial['AGENDADOS'] + comercial['LLAMADOS'] + comercial['OFERTADOS'] + comercial['NOCONTESTA'] + comercial['NOINTERESA'] + comercial['VENDIDO'] + comercial['NOEXISTE']
            comercial['GENERAL'] = general

            datos[com.nombre] = comercial
    
    context = {"contadores": datos, "busqueda" : busqueda, "desde" : desde,"hasta" : hasta }
    return render(request, 'comerciales.html', context)

def detalle_comercial(request, pk):
    detalle = Comerciales.objects.get(id=pk)
    context = {
        "detalle" : detalle
    }
    return render(request, 'det_comercial.html', context)

def detalle_cliente(request, pk):
    detalle = Clientes.objects.get(id=pk)
    context = {
        "detalle": detalle
    }
    return render(request, 'detalle.html', context)


def nuevo_cliente(request):
    comerciales = Comerciales.objects.all()
    form = ClienteForm

    if(request.method=='POST'):
        form = ClienteForm(request.POST)

        if form.is_valid():
            new = form.save(commit=False)
            new.save()

            context = {"text" : "El Usuario se insertó correctamente, vuelva a la lista de clientes."}
            return render(request,'clientes.html', context)
        else:
            context = {"form" : form, "comerciales" : comerciales}
            return render(request,'form_cliente.html', context)

    else:
        context = {"form" : form, "comerciales" : comerciales}
        return render(request,'form_cliente.html', context)

# def busca_cliente(request):
#     form = BuscaCliente
#     if(request.method=='POST'):
#         form = BuscaCliente(request.POST)

#     context = {"form" : form}
#     return render(request,'form_busqueda.html', context)



def editar_cliente(request, pk):
    cliente = Clientes.objects.get(id=pk) #recuperamos la instancia del cliente
    form = ClienteForm(instance=cliente) #creamos el formulario con esos datos recuperados
    comerciales = Comerciales.objects.all()

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
            context = {"text" : "El Usuario se ha editado correctamente, vuelva a la lista de clientes."}
            return render(request,'clientes.html', context)
    
    context = {"form" : form, "comerciales" : comerciales, "text" : "El Usuario se ha editado correctamente, vuelva a la lista de clientes."}
    return render(request, 'editar.html', context) #esta es otra forma de pasar el contexto



def busca_cliente(request):
    form = BuscaCliente
    comerciales = Comerciales.objects.all()

    if(request.method=='POST'):
        DNI = request.POST.get("DNI", "")
        nombre = request.POST.get("nombre", "")
        comercial = request.POST.get("comercial", "")
        operador = request.POST.get("operador", "")
        telefono = request.POST.get("telefono", "")
        estado = request.POST.get("estado", "")
        general = request.POST.get("general", "")
        direccion = request.POST.get("direccion", "")
        poblacion = request.POST.get("poblacion", "")

        desde_fc = request.POST.get("desde_fc", "")
        hasta_fc = request.POST.get("hasta_fc", "")
        desde_fv = request.POST.get("desde_fv", "")
        hasta_fv = request.POST.get("hasta_fv", "")
        desde_fa = request.POST.get("desde_fa", "")
        hasta_fa = request.POST.get("hasta_fa", "")

        FMC_portaFijo = request.POST.get("FMC_portaFijo", "")
        FMC_FijoNuevo = request.POST.get("FMC_FijoNuevo", "")
        PospagoMO = request.POST.get("PospagoMO", "")
        PospagoMB_DUOMB = request.POST.get("PospagoMB_DUOMB", "")
        CROSS_FijoPortado = request.POST.get("CROSS_FijoPortado", "")
        CROSS_FijoNuevo = request.POST.get("CROSS_FijoNuevo", "")
        RENUEVO = request.POST.get("RENUEVO", "")
        RENUEVOSUBIDA = request.POST.get("RENUEVOSUBIDA", "")
        TV = request.POST.get("TV", "")
        SEGURO = request.POST.get("SEGURO", "")
        ACCESORIOS = request.POST.get("ACCESORIOS", "")
        TERMLIBRE = request.POST.get("TERMLIBRE", "")
        CAMBIOTECNOLOGIA = request.POST.get("CAMBIOTECNOLOGIA", "")
        PREPAGO = request.POST.get("PREPAGO", "")
        SEGURO_FAM = request.POST.get("SEGURO_FAM", "")
        PEPENERGY = request.POST.get("PEPENERGY", "")
        ENERGYGO = request.POST.get("ENERGYGO", "")
        SMARTHOME = request.POST.get("SMARTHOME", "")
        MOADICIONAL = request.POST.get("MOADICIONAL", "")

        consulta=consulta2=consulta3=consulta4=consulta5=consulta6=consulta7=consulta8=consulta9=consulta10=consulta11=consulta12=consulta13=consulta14=consulta15=consulta16=consulta17=consulta18=consulta19=consulta20=consulta21=consulta22=consulta23=consulta24=consulta25=consulta26=consulta27=consulta28=consulta29=consulta30=consulta31=consulta32=consulta33=Q()


        if(DNI != ""):
            consulta=Q(DNI__contains=DNI)
        if(comercial != "---------"):
            consulta3=Q(comercial=comercial)
        if(telefono != ""):
            consulta3=Q(telefono__contains=telefono)
        if(direccion != ""):
            consulta4=Q(direccion__contains=direccion)
        if(poblacion != ""):
            consulta5=Q(poblacion__contains=poblacion)
        if(estado != "---------"):
            consulta6=Q(estado=estado)  
        if(operador != "---------"):
            consulta7=Q(operador__contains=operador)   
        if(desde_fc != ""):
            consulta8=Q(fecha_contacto__gte=desde_fc)
        if(hasta_fc != ""):
            consulta9=Q(fecha_contacto__lte=hasta_fc)  
        if(desde_fv != ""):
            consulta10=Q(fecha_venta__gte=desde_fv)
        if(hasta_fv != ""):
            consulta11=Q(fecha_venta__lte=hasta_fv)
        if(desde_fa != ""):
            consulta12=Q(fecha_agendado__gte=desde_fa)
        if(hasta_fa != ""):
            consulta13=Q(fecha_agendado__lte=hasta_fa)
        if(nombre != ""):
            consulta14=Q(nombre__contains=nombre)
        if(FMC_portaFijo == 'on'):
            consulta15=Q(FMC_portaFIJO__gt=0)
        if(FMC_FijoNuevo == 'on'):
            consulta16=Q(FMC_FijoNuevo__gt=0)
        if(PospagoMO == 'on'):
            consulta17=Q(PospagoMO__gt=0)
        if(PospagoMB_DUOMB == 'on'):
            consulta18=Q(PospagoMB_DUOMB__gt=0)
        if(CROSS_FijoPortado == 'on'):
            consulta19=Q(CROSS_FijoPortado__gt=0)
        if(CROSS_FijoNuevo == 'on'):
            consulta20=Q(CROSS_FijoNuevo__gt=0)
        if(RENUEVO == 'on'):
            consulta21=Q(RENUEVO__gt=0)
        if(RENUEVOSUBIDA == 'on'):
            consulta22=Q(RENUEVOSUBIDA__gt=0)
        if(TV == 'on'):
            consulta23=Q(TV__gt=0)
        if(SEGURO == 'on'):
            consulta24=Q(SEGURO__gt=0)
        if(ACCESORIOS == 'on'):
            consulta25=Q(ACCESORIOS__gt=0)
        if(TERMLIBRE == 'on'):
            consulta26=Q(TERMLIBRE__gt=0)
        if(CAMBIOTECNOLOGIA == 'on'):
            consulta27=Q(CAMBIOTECNOLOGIA__gt=0)
        if(PREPAGO == 'on'):
            consulta28=Q(PREPAGO__gt=0)
        if(SEGURO_FAM == 'on'):
            consulta29=Q(SEGURO_FAM__gt=0)
        if(PEPENERGY == 'on'):
            consulta30=Q(PEPENERGY__gt=0)
        if(ENERGYGO == 'on'):
            consulta31=Q(ENERGYGO__gt=0)
        if(SMARTHOME == 'on'):
            consulta32=Q(SMARTHOME__gt=0)
        if(MOADICIONAL == 'on'):
            consulta33=Q(MOADICIONAL__gt=0)

        to_search=dict()

        for param in request.POST:
            if param!="csrfmiddlewaretoken":
                to_search[param]=request.POST.get(param, "")

        aux = consulta&consulta2&consulta3&consulta4&consulta5&consulta6&consulta7&consulta8&consulta9&consulta10&consulta11&consulta12&consulta13&consulta14&consulta15&consulta16&consulta17&consulta18&consulta19&consulta20&consulta21&consulta22&consulta23&consulta24&consulta25&consulta26&consulta27&consulta28&consulta29&consulta30&consulta31&consulta32&consulta33
        clientes=Clientes.objects.filter(aux)
        todo=Clientes.objects.filter(aux).query


        if(general != ""):
            aux = Q(nombre__contains=general)|Q(DNI__contains=general)|Q(CP__contains=general)|Q(email__contains=general)|Q(telefono__contains=general)|Q(provincia__contains=general)|Q(poblacion__contains=general)|Q(direccion__contains=general)|Q(comercial__nombre__contains=general)
            clientes=Clientes.objects.filter(aux)
            todo=Clientes.objects.filter(aux).query
        
        paginator = Paginator(clientes, 25)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        context = {"clientes" : page_obj, "comerciales" : comerciales, "page_obj":page_obj , "total" : todo, "busqueda":to_search}
        return render(request,'form_busqueda.html', context)

    
    else:
        clientes = Clientes.objects.get_queryset().order_by('nombre')
        paginator = Paginator(clientes, 25)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {"titulo" : "Buscando un Cliente", "form" : form, "comerciales" : comerciales, "clientes":page_obj, "page_obj":page_obj}
        return render(request,'form_busqueda.html', context)


def descargarcsv(request):
    if(request.method=='POST'):
        DNI = request.POST.get("DNI", "")
        nombre = request.POST.get("nombre", "")
        comercial = request.POST.get("comercial", "")
        operador = request.POST.get("operador", "")
        telefono = request.POST.get("telefono", "")
        estado = request.POST.get("estado", "")
        general = request.POST.get("general", "")
        direccion = request.POST.get("direccion", "")
        poblacion = request.POST.get("poblacion", "")

        desde_fc = request.POST.get("desde_fc", "")
        hasta_fc = request.POST.get("hasta_fc", "")
        desde_fv = request.POST.get("desde_fv", "")
        hasta_fv = request.POST.get("hasta_fv", "")
        desde_fa = request.POST.get("desde_fa", "")
        hasta_fa = request.POST.get("hasta_fa", "")

        FMC_portaFijo = request.POST.get("FMC_portaFijo", "")
        FMC_FijoNuevo = request.POST.get("FMC_FijoNuevo", "")
        PospagoMO = request.POST.get("PospagoMO", "")
        PospagoMB_DUOMB = request.POST.get("PospagoMB_DUOMB", "")
        CROSS_FijoPortado = request.POST.get("CROSS_FijoPortado", "")
        CROSS_FijoNuevo = request.POST.get("CROSS_FijoNuevo", "")
        RENUEVO = request.POST.get("RENUEVO", "")
        RENUEVOSUBIDA = request.POST.get("RENUEVOSUBIDA", "")
        TV = request.POST.get("TV", "")
        SEGURO = request.POST.get("SEGURO", "")
        ACCESORIOS = request.POST.get("ACCESORIOS", "")
        TERMLIBRE = request.POST.get("TERMLIBRE", "")
        CAMBIOTECNOLOGIA = request.POST.get("CAMBIOTECNOLOGIA", "")
        PREPAGO = request.POST.get("PREPAGO", "")
        SEGURO_FAM = request.POST.get("SEGURO_FAM", "")
        PEPENERGY = request.POST.get("PEPENERGY", "")
        ENERGYGO = request.POST.get("ENERGYGO", "")
        SMARTHOME = request.POST.get("SMARTHOME", "")
        MOADICIONAL = request.POST.get("MOADICIONAL", "")

        consulta=consulta2=consulta3=consulta4=consulta5=consulta6=consulta7=consulta8=consulta9=consulta10=consulta11=consulta12=consulta13=consulta14=consulta15=consulta16=consulta17=consulta18=consulta19=consulta20=consulta21=consulta22=consulta23=consulta24=consulta25=consulta26=consulta27=consulta28=consulta29=consulta30=consulta31=consulta32=consulta33=Q()


        if(DNI != ""):
            consulta=Q(DNI__contains=DNI)
        if(comercial != "---------" and comercial != ""):
            consulta3=Q(comercial=comercial)
        if(telefono != ""):
            consulta3=Q(telefono__contains=telefono)
        if(direccion != ""):
            consulta4=Q(direccion__contains=direccion)
        if(poblacion != ""):
            consulta5=Q(poblacion__contains=poblacion)
        if(estado != "---------" and estado !=""):
            consulta6=Q(estado=estado)  
        if(operador != "---------" and operador != ""):
            consulta7=Q(operador__contains=operador)   
        if(desde_fc != ""):
            consulta8=Q(fecha_contacto__gte=desde_fc)
        if(hasta_fc != ""):
            consulta9=Q(fecha_contacto__lte=hasta_fc)  
        if(desde_fv != ""):
            consulta10=Q(fecha_venta__gte=desde_fv)
        if(hasta_fv != ""):
            consulta11=Q(fecha_venta__lte=hasta_fv)
        if(desde_fa != ""):
            consulta12=Q(fecha_agendado__gte=desde_fa)
        if(hasta_fa != ""):
            consulta13=Q(fecha_agendado__lte=hasta_fa)
        if(nombre != ""):
            consulta14=Q(nombre__contains=nombre)
        if(FMC_portaFijo == 'on'):
            consulta15=Q(FMC_portaFIJO__gt=0)
        if(FMC_FijoNuevo == 'on'):
            consulta16=Q(FMC_FijoNuevo__gt=0)
        if(PospagoMO == 'on'):
            consulta17=Q(PospagoMO__gt=0)
        if(PospagoMB_DUOMB == 'on'):
            consulta18=Q(PospagoMB_DUOMB__gt=0)
        if(CROSS_FijoPortado == 'on'):
            consulta19=Q(CROSS_FijoPortado__gt=0)
        if(CROSS_FijoNuevo == 'on'):
            consulta20=Q(CROSS_FijoNuevo__gt=0)
        if(RENUEVO == 'on'):
            consulta21=Q(RENUEVO__gt=0)
        if(RENUEVOSUBIDA == 'on'):
            consulta22=Q(RENUEVOSUBIDA__gt=0)
        if(TV == 'on'):
            consulta23=Q(TV__gt=0)
        if(SEGURO == 'on'):
            consulta24=Q(SEGURO__gt=0)
        if(ACCESORIOS == 'on'):
            consulta25=Q(ACCESORIOS__gt=0)
        if(TERMLIBRE == 'on'):
            consulta26=Q(TERMLIBRE__gt=0)
        if(CAMBIOTECNOLOGIA == 'on'):
            consulta27=Q(CAMBIOTECNOLOGIA__gt=0)
        if(PREPAGO == 'on'):
            consulta28=Q(PREPAGO__gt=0)
        if(SEGURO_FAM == 'on'):
            consulta29=Q(SEGURO_FAM__gt=0)
        if(PEPENERGY == 'on'):
            consulta30=Q(PEPENERGY__gt=0)
        if(ENERGYGO == 'on'):
            consulta31=Q(ENERGYGO__gt=0)
        if(SMARTHOME == 'on'):
            consulta32=Q(SMARTHOME__gt=0)
        if(MOADICIONAL == 'on'):
            consulta33=Q(MOADICIONAL__gt=0)

        consulta = consulta&consulta2&consulta3&consulta4&consulta5&consulta6&consulta7&consulta8&consulta9&consulta10&consulta11&consulta12&consulta13&consulta14&consulta15&consulta16&consulta17&consulta18&consulta19&consulta20&consulta21&consulta22&consulta23&consulta24&consulta25&consulta26&consulta27&consulta28&consulta29&consulta30&consulta31&consulta32&consulta33

        clientes = Clientes.objects.filter(consulta)

        if(general != ""):
            clientes = Clientes.objects.filter(nombre__contains=general) | Clientes.objects.filter(DNI__contains=general) | Clientes.objects.filter(email__contains=general) | Clientes.objects.filter(telefono__contains=general) | Clientes.objects.filter(CP__contains=general) | Clientes.objects.filter(provincia__contains=general) | Clientes.objects.filter(poblacion__contains=general) | Clientes.objects.filter(direccion__contains=general) | Clientes.objects.filter(CP=general) | Clientes.objects.filter(comercial__nombre__contains=general) 
    

        # df = pd.DataFrame(data, columns = ['Nombre', 'Origen', 'Fecha', 'Comercial', 'DNICIF', 'Segmento', 'Direccion', 'Localidad', 'Fijo', 'Movil', 'Operador', 'Estado', 'Motivo No', 'Fecha Agendado', 'Fecha Venta'])
        output = []
        response = HttpResponse (content_type='text/csv')
        writer = csv.writer(response)
        query_set = clientes
        #query_set =Clientes.objects.filter(general)
        #print(query_set)

        #Header

        writer.writerow(['Nombre', 'Origen', 'DNI', 'Comercial', 'Segmento', 'Direccion', 'Poblacion', 'Telefono', 'Estado', 'Operador'])
        for user in query_set:
            cliente = Clientes.objects.get(id=user.id)
            output.append([user.nombre,user.origen,user.DNI,user.comercial.nombre,user.segmento,user.direccion,user.poblacion,user.telefono,user.estado,user.operador])
        #CSV Data
        writer.writerows(output)
        return response

def descargarcom(request):
    busqueda = request.POST.get("busqueda", "")
    desde = request.POST.get("desde", "")
    hasta = request.POST.get("hasta", "")

    datos={}

    consulta=consulta1=consulta2=Q()

    comerciales = Comerciales.objects.filter(nombre__contains=busqueda)

    if(request.method=='POST' and busqueda != ""):
        if(desde != ""):
            consulta=Q(fecha_contacto__gte=desde)
        if(hasta != ""):
            consulta1=Q(fecha_contacto__lte=hasta)
        
        for com in comerciales:
            comercial = dict(
                    ID = com.id,
                    NOMBRE = com.nombre,
                    AGENDADOS = Clientes.objects.filter(Q(comercial=com.id)&Q(estado='AGENDADO')&consulta&consulta1).count(),
                    LLAMADOS = Clientes.objects.filter(Q(comercial=com.id)&Q(estado='LLAMADO')&consulta&consulta1).count(),
                    OFERTADOS = Clientes.objects.filter(Q(comercial=com.id)&Q(estado='OFERTADO')&consulta&consulta1).count(),
                    NOCONTESTA = Clientes.objects.filter(Q(comercial=com.id)&Q(estado='NO CONTESTA')&consulta&consulta1).count(),
                    NOINTERESA = Clientes.objects.filter(Q(comercial=com.id)&Q(estado='NO INTERESADO')&consulta&consulta1).count(),
                    VENDIDO = Clientes.objects.filter(Q(comercial=com.id)&Q(estado='VENDIDO')&consulta&consulta1).count(),
                    NOEXISTE = Clientes.objects.filter(Q(comercial=com.id)&Q(estado='NO EXISTE')&consulta&consulta1).count(),
                    GENERAL = 0,
                    VENTAVALOR = Clientes.objects.filter( Q(comercial=com.id) & Q(estado='VENDIDO')&consulta&consulta1).count(),
                    VENTASTOTALES = Clientes.objects.filter( Q(comercial=com.id) & ((Q(FMC_portaFIJO__gt=0) | Q(FMC_FijoNuevo__gt=0) | Q(PospagoMO__gt=0) | Q(PospagoMB_DUOMB__gt=0) | Q(CROSS_FijoPortado__gt=0) | Q(CROSS_FijoNuevo__gt=0) | Q(RENUEVO__gt=0) | Q(RENUEVOSUBIDA__gt=0) | Q(TV__gt=0) | Q(SEGURO__gt=0) | Q(ACCESORIOS__gt=0) | Q(TERMLIBRE__gt=0) | Q(CAMBIOTECNOLOGIA__gt=0) | Q(PREPAGO__gt=0) | Q(SEGURO_FAM__gt=0) | Q(PEPENERGY__gt=0) | Q(ENERGYGO__gt=0) | Q(SMARTHOME__gt=0) | Q(MOADICIONAL__gt=0)) & consulta & consulta1 )).count(),
            )

            general = comercial['AGENDADOS'] + comercial['LLAMADOS'] + comercial['OFERTADOS'] + comercial['NOCONTESTA'] + comercial['NOINTERESA'] + comercial['VENDIDO'] + comercial['NOEXISTE']
            comercial['GENERAL'] = general

            datos[com.nombre] = comercial
    else:
        todos = Comerciales.objects.all()

        if(desde != ""):
            consulta=Q(fecha_contacto__gte=desde)
        if(hasta != ""):
            consulta1=Q(fecha_contacto__lte=hasta)

        for com in todos:
            comercial = dict(
                ID = com.id,
                NOMBRE = com.nombre,
                AGENDADOS = Clientes.objects.filter(Q(comercial=com.id)&Q(estado='AGENDADO')&consulta&consulta1).count(),
                LLAMADOS = Clientes.objects.filter(Q(comercial=com.id)&Q(estado='LLAMADO')&consulta&consulta1).count(),
                OFERTADOS = Clientes.objects.filter(Q(comercial=com.id)&Q(estado='OFERTADO')&consulta&consulta1).count(),
                NOCONTESTA = Clientes.objects.filter(Q(comercial=com.id)&Q(estado='NO CONTESTA')&consulta&consulta1).count(),
                NOINTERESA = Clientes.objects.filter(Q(comercial=com.id)&Q(estado='NO INTERESADO')&consulta&consulta1).count(),
                VENDIDO = Clientes.objects.filter(Q(comercial=com.id)&Q(estado='VENDIDO')&consulta&consulta1).count(),
                NOEXISTE = Clientes.objects.filter(Q(comercial=com.id)&Q(estado='NO EXISTE')&consulta&consulta1).count(),
                GENERAL = 0,
                VENTAVALOR = Clientes.objects.filter( Q(comercial=com.id) & Q(estado='VENDIDO')&consulta&consulta1).count(),
                VENTASTOTALES = Clientes.objects.filter( Q(comercial=com.id) & ((Q(FMC_portaFIJO__gt=0) | Q(FMC_FijoNuevo__gt=0) | Q(PospagoMO__gt=0) | Q(PospagoMB_DUOMB__gt=0) | Q(CROSS_FijoPortado__gt=0) | Q(CROSS_FijoNuevo__gt=0) | Q(RENUEVO__gt=0) | Q(RENUEVOSUBIDA__gt=0) | Q(TV__gt=0) | Q(SEGURO__gt=0) | Q(ACCESORIOS__gt=0) | Q(TERMLIBRE__gt=0) | Q(CAMBIOTECNOLOGIA__gt=0) | Q(PREPAGO__gt=0) | Q(SEGURO_FAM__gt=0) | Q(PEPENERGY__gt=0) | Q(ENERGYGO__gt=0) | Q(SMARTHOME__gt=0) | Q(MOADICIONAL__gt=0)) & consulta & consulta1 )).count(),
            )

            general = comercial['AGENDADOS'] + comercial['LLAMADOS'] + comercial['OFERTADOS'] + comercial['NOCONTESTA'] + comercial['NOINTERESA'] + comercial['VENDIDO'] + comercial['NOEXISTE']
            comercial['GENERAL'] = general

            datos[com.nombre] = comercial

    output = []
    response = HttpResponse (content_type='text/csv')
    writer = csv.writer(response)
    #query_set = clientes
    #query_set =Clientes.objects.filter(general)
    #print(query_set)

    #Header

    #print(datos.values())

    writer.writerow(['Comercial', 'Agendado', 'Llamado', 'Ofertado', 'No contesta', 'No interesado', 'Vendido', 'No existe', 'Total general', 'Total venta valor', 'Total venta'])
    for comercial in datos:
        output.append([datos[comercial]['NOMBRE'], datos[comercial]['AGENDADOS'], datos[comercial]['LLAMADOS'], datos[comercial]['OFERTADOS'], datos[comercial]['NOCONTESTA'], datos[comercial]['NOINTERESA'], datos[comercial]['VENDIDO'],datos[comercial]['NOEXISTE'],datos[comercial]['GENERAL'],datos[comercial]['VENTAVALOR'],datos[comercial]['VENTASTOTALES']])

    #    output.append([campos.NOMBRE,campos.AGENDADOS,campos.LLAMADOS,campos.OFERTADOS,campos.NOCONTESTA,campos.NOINTERESA,campos.VENDIDO,campos.NOEXISTE,campos.GENERAL,campos.VENTAVALOR,campos.VENTASTOTALES])
    #CSV Data
    writer.writerows(output)
    return response

        