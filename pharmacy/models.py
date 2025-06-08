from django.db import models

# Create your models here.

class EffectGroup(models.Model):
    effect_group_id = models.AutoField(primary_key=True)
    effect_group = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'EffectGroup'

class Form(models.Model):
    form_id = models.AutoField(primary_key=True)
    form_name = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'Form'

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'Company'

class Institution(models.Model):
    institution_id = models.AutoField(primary_key=True)
    institution = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'Institution'

class Shelf(models.Model):
    shelf_id = models.AutoField(primary_key=True)
    shelf_location = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'Shelf'

class PrescriptionIssuance(models.Model):
    issuance_id = models.AutoField(primary_key=True)
    issuance_no = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'PrescriptionIssuance'

class Medicine(models.Model):
    medicine_id = models.AutoField(primary_key=True)
    barcode = models.CharField(max_length=50, unique=True)
    medicine_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.IntegerField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    effect_group = models.ForeignKey(EffectGroup, on_delete=models.CASCADE)
    shelf = models.ForeignKey(Shelf, on_delete=models.SET_NULL, null=True)
    prescription = models.ForeignKey(PrescriptionIssuance, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        db_table = 'Medicine'

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    
    class Meta:
        db_table = 'Customer'

class MedicineSale(models.Model):
    sale_id = models.AutoField(primary_key=True)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    sale_date = models.DateTimeField(auto_now_add=True)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    barcode = models.CharField(max_length=50)
    institution = models.ForeignKey(Institution, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        db_table = 'MedicineSale'
