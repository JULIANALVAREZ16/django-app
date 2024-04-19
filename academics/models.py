import datetime
from django.db import models
# Create your models here.

class DateTimeModel(models.Model):
    created_at = models.DateTimeField(default = datetime.datetime.now())
    updated_at = models.DateTimeField(default = datetime.datetime.now())
    deleted_at = models.DateTimeField(null =True, blank = True)

    class Meta:
        abstract =True

class User(DateTimeModel):
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length =250)
    status = models.BooleanField(default = True)


    #def __str__(self):
    #   return f "{self.email}-{self.password}"

class Identification_type(DateTimeModel):
    name = models.CharField(max_length = 50)
    abrev = models.CharField(max_length = 10)
    descrip = models.CharField(max_length = 100)

class Countries(DateTimeModel):
    name = models.CharField(max_length = 100)
    abrev = models.CharField(max_length =10)
    descrip = models.CharField(max_length =10)
    

class Deparments(DateTimeModel):
    name = models.CharField(max_length = 100)
    abrev = models.CharField(max_length =10)
    descrip = models.CharField(max_length =10)
    id_country = models.ForeignKey(Countries, on_delete=models.CASCADE)


class Cities(DateTimeModel):
    name = models.CharField(max_length = 100)
    abrev = models.CharField(max_length =10)
    descrip = models.CharField(max_length =10)
    id_dept = models.ForeignKey(Deparments, on_delete=models.CASCADE)


class Person(DateTimeModel):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    id_ident_type = models.ForeignKey(Identification_type, on_delete=models.CASCADE)
    ident_number = models.CharField(max_length =15)
    id_exp_city = models.ForeignKey(Cities, on_delete=models.CASCADE)
    address = models.CharField(max_length =150)
    mobile = models.CharField(max_length =50)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)

class Students(DateTimeModel):
    code = models.CharField(max_length = 50)
    id_person = models.ForeignKey(Person, on_delete=models.CASCADE)
    status = models.BooleanField(default = True)


