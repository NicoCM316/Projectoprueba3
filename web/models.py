from django.db import models


class Categoria(models.Model):
    id_categoria = models.AutoField(db_column='idCategoria', primary_key=True)
    categoria = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return str(self.categoria)


class Producto(models.Model):
    id_producto = models.AutoField(db_column='idProducto', primary_key=True)
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    lot = models.CharField(max_length=50, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
