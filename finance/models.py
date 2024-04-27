from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.

class DateTimeModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract =True

class Cliente(DateTimeModel):
    id_cliente = models.AutoField(primary_key=True, unique=True, blank=False,null=False)
    nombre = models.CharField(max_length=30, blank=False,null=False)
    apellidos = models.CharField(max_length=30, blank=False,null=False)
    email = models.CharField(max_length = 100, blank=False,null=False)
    celular = models.CharField(max_length=10, blank=False,null=False)
    password = models.CharField(max_length=250, blank=True)
    
    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(Cliente, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre+ ' ' + self.apellidos + ' - ' + self.email + ' - ' + self.celular


class Producto(DateTimeModel):
    id_producto = models.AutoField(primary_key=True, unique=True, blank=False,null=False)
    nombre_producto = models.CharField(max_length=100, blank=False,null=False)
    abreviatura = models.CharField(max_length=10, blank=False,null=False)
    descripcion =models.CharField(max_length=400, blank=False,null=False)

    def __str__(self):
        return self.nombre_producto + ' - ' + self.abreviatura + ' - ' + self.descripcion
    

class clientes_productos(DateTimeModel):
    id_cli_pro = models.AutoField(primary_key=True, unique=True, blank=False,null=False)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=False,null=False)
    id_producto = models.ForeignKey(Producto,on_delete=models.CASCADE, blank=False,null=False)
    numero_cuenta = models.CharField(max_length=50, blank=False,null=False)

    def __str__(self):
        return self.id_cliente.nombre + ' - ' + self.id_producto.nombre_producto + ' - ' + self.numero_cuenta

class tipo_transaccion(DateTimeModel):
    id_tipo_trans = models.AutoField(primary_key=True, unique=True, blank=False,null=False)
    nombre = models.CharField(max_length=100, blank=False,null=False)
    abreviatura = models.CharField(max_length=10, blank=False,null=False)
    descripcion =models.CharField(max_length=400, blank=False,null=False)

    def __str__(self):
        return  self.nombre + ' - ' + self.abreviatura + ' - ' + self.descripcion

class transaccione(DateTimeModel):
    id_transaccion = models.AutoField(primary_key=True, unique=True, blank=False,null=False)
    id_cli_pro = models.ForeignKey(clientes_productos,on_delete=models.CASCADE, blank=False,null=False)
    monto = models.CharField(max_length=100, blank=False,null=False)
    id_tipo_trans = models.ForeignKey(tipo_transaccion,on_delete=models.CASCADE, blank=False,null=False)
    def __str__(self):
        return self.id_cli_pro.id_cliente.nombre+ ' ' + self.id_cli_pro.id_cliente.apellidos + ' - ' + self.id_tipo_trans.nombre  + ' - ' + self.monto