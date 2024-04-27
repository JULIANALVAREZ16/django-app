from django.contrib import admin
from .models import Cliente, Producto, clientes_productos, tipo_transaccion, transaccione

class clientField(admin.ModelAdmin):
    list_display =['id_cliente','nombre', 'apellidos', 'email','celular','password']

class productoField(admin.ModelAdmin):
    list_display =['id_producto', 'nombre_producto', 'abreviatura','descripcion']

class cliente_productoField(admin.ModelAdmin):
    list_display =['id_cli_pro', 'id_cliente', 'id_producto','numero_cuenta']

class tipo_transeccionField(admin.ModelAdmin):
    list_display =['id_tipo_trans', 'nombre', 'abreviatura','descripcion']

class transeccioneField(admin.ModelAdmin):
    list_display =['id_transaccion', 'id_cli_pro', 'monto','id_tipo_trans']


admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(clientes_productos)
admin.site.register(tipo_transaccion)
admin.site.register(transaccione)


