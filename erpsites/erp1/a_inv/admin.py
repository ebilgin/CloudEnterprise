from django.contrib import admin
from a_inv.models import *

# Inlines
    
class Supplier_Address_Inline(admin.TabularInline):
    model = Supplier_Address
    extra = 1

# Custom Admins
class Supplier_Admin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['supplier_name']}),
        ('Other information', {'fields': ['supplier_details'], 'classes': ['collapse']}),
    ]
    inlines = [Supplier_Address_Inline]
    

class Supplier_Address_Admin(admin.ModelAdmin):
    list_display = ('supplier_id','address_type_code', 'address_id')
    
   
    
class Address_Admin(admin.ModelAdmin):   
    list_display = ('line_1_2', 'city','state','zip_code','is_domestic') 
    def line_1_2(self, obj):
        return ("%s, %s" % (obj.line_1, obj.line_2))
    line_1_2.short_description = 'Address' 
    list_filter = ['country']
    search_fields = ['city']



# Register your models here.  

admin.site.register(Address_Type)

admin.site.register(Supplier,Supplier_Admin)
admin.site.register(Address,Address_Admin)
admin.site.register(Supplier_Address,Supplier_Address_Admin)
