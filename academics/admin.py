from django.contrib import admin
from.models import User, Person, Students, Identification_type, Cities, Deparments, Countries
# Register your models here.
class UserFields(admin.ModelAdmin):
    list_display =('email', 'password', 'status')
    
class PersonFields (admin.ModelAdmin):
    list_display=('first_name', 'last_name','id_ident_type','ident_number','id_exp_city','address','mobile')

    #admin.site.register(User, UserFields)
    #admin.site.register(Person, PersonFields) 

admin.site.register(User)
admin.site.register(Person)
admin.site.register(Students)
admin.site.register(Identification_type)
admin.site.register(Cities)
admin.site.register(Deparments)
admin.site.register(Countries)

