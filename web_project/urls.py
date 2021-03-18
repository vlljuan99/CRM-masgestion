from django.contrib import admin
from django.urls import path, include

#Aquí pondremos todas las rutas del proyecto
#Para '', llamaremos a la función index

urlpatterns = [
    path('admin/', admin.site.urls), #este es el admin de Django, ya se quitará
    path('CRM/', include('CRM.urls', namespace='CRM'))
]
