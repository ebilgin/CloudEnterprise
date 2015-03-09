from django.db import models

# Reference Tables    

class Address_Type(models.Model):
    address_type_code = models.CharField(max_length=10, primary_key=True)
    address_type_description = models.CharField(max_length=200, blank=True)
    def __unicode__(self):
        return self.address_type_code

# Create your models here.

class Supplier(models.Model):
    supplier_idn = models.AutoField(primary_key=True)
    supplier_name = models.CharField(max_length=200)
    supplier_details = models.CharField(max_length=1000, blank=True)
    def __unicode__(self):
        return self.supplier_name
    
    
class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    line_1 = models.CharField(max_length=200, verbose_name="Address Line 1")
    line_2 = models.CharField(max_length=200, blank=True, help_text="Apt., Suite etc.")
    line_3 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=200, blank=True)
    
    country = models.CharField(max_length=200, blank=True)
    address_details = models.CharField(max_length=200, blank=True)
    def is_domestic(self):
        return self.country == "USA"
    #is_domestic.admin_order_field = "country"
    is_domestic.boolean = True
    is_domestic.short_description = "Domestic?"
    
    def __unicode__(self):
        return self.line_1
    
class Supplier_Address(models.Model):
    supplier_address_id = models.AutoField(primary_key=True)
    supplier_id = models.ForeignKey(Supplier)
    address_id = models.ForeignKey(Address)
    address_type_code = models.ForeignKey(Address_Type)
    supplier_address_details = models.CharField(max_length=200, blank=True)
    def __unicode__(self):
        return (unicode(self.supplier_id)+" "+unicode(self.address_id))
    
    
    

    