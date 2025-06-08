from django import forms
from .models import EffectGroup, Form, Company, Institution, Shelf, PrescriptionIssuance, Customer, Medicine, MedicineSale

class EffectGroupForm(forms.Form):
    effect_group = forms.CharField(max_length=100, label='Etki Grubu')

class FormForm(forms.Form):
    form_name = forms.CharField(max_length=100, label='Form Adı')

class CompanyForm(forms.Form):
    company_name = forms.CharField(max_length=100, label='Firma Adı')

class InstitutionForm(forms.Form):
    institution = forms.CharField(max_length=100, label='Kurum Adı')

class ShelfForm(forms.Form):
    shelf_location = forms.CharField(max_length=100, label='Raf Konumu')

class PrescriptionIssuanceForm(forms.Form):
    issuance_no = forms.CharField(max_length=100, label='Reçete Numarası')

class CustomerForm(forms.Form):
    name = forms.CharField(max_length=100, label='Müşteri Adı')
    phone = forms.CharField(max_length=20, required=False, label='Telefon')
    email = forms.EmailField(required=False, label='E-posta')

class MedicineForm(forms.Form):
    barcode = forms.CharField(max_length=50, label='Barkod')
    medicine_name = forms.CharField(max_length=100, label='İlaç Adı')
    price = forms.DecimalField(max_digits=10, decimal_places=2, label='Fiyat')
    in_stock = forms.IntegerField(label='Stok Miktarı')
    company_id = forms.ModelChoiceField(queryset=Company.objects.all(), label='Firma')
    form_id = forms.ModelChoiceField(queryset=Form.objects.all(), label='Form')
    effect_group_id = forms.ModelChoiceField(queryset=EffectGroup.objects.all(), label='Etki Grubu')
    shelf_id = forms.ModelChoiceField(queryset=Shelf.objects.all(), required=False, label='Raf')
    prescription_id = forms.ModelChoiceField(queryset=PrescriptionIssuance.objects.all(), required=False, label='Reçete')

class MedicineSaleForm(forms.Form):
    sale_price = forms.DecimalField(max_digits=10, decimal_places=2, label='Satış Fiyatı')
    quantity = forms.IntegerField(label='Adet')
    medicine_id = forms.ModelChoiceField(queryset=Medicine.objects.all(), label='İlaç')
    barcode = forms.CharField(max_length=50, label='Barkod')
    institution_id = forms.ModelChoiceField(queryset=Institution.objects.all(), required=False, label='Kurum')
    customer_id = forms.ModelChoiceField(queryset=Customer.objects.all(), required=False, label='Müşteri')
