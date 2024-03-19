from django.contrib import admin
from.models import User, Persons, Students, Identification_type, Cities, Deparments, Countries
# Register your models here.
admin.site.register(User)
admin.site.register(Persons)
admin.site.register(Students)
admin.site.register(Identification_type)
admin.site.register(Cities)
admin.site.register(Deparments)
admin.site.register(Countries)