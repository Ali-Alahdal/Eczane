from django.shortcuts import render, redirect, get_object_or_404
from django.db import connection
from .forms import (
    EffectGroupForm, FormForm, CompanyForm, InstitutionForm, ShelfForm,
    PrescriptionIssuanceForm, CustomerForm, MedicineForm, MedicineSaleForm
)

# --- EffectGroup CRUD ---
def effectgroup_list(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM EffectGroup")
        columns = [col[0] for col in cursor.description]
        effectgroups = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return render(request, 'pharmacy/effectgroup_list.html', {'effectgroups': effectgroups})

def effectgroup_create(request):
    if request.method == 'POST':
        form = EffectGroupForm(request.POST)
        if form.is_valid():
            with connection.cursor() as cursor:
                cursor.callproc('InsertEffectGroup', [form.cleaned_data['effect_group']])
            return redirect('effectgroup_list')
    else:
        form = EffectGroupForm()
    return render(request, 'pharmacy/effectgroup_form.html', {'form': form, 'effectgroup': None})

def effectgroup_update(request, pk):
    with connection.cursor() as cursor:
        cursor.callproc('GetEffectGroupById', [pk])
        row = cursor.fetchone()
        if not row:
            return redirect('effectgroup_list')
        columns = [col[0] for col in cursor.description]
        effectgroup = dict(zip(columns, row))
    if request.method == 'POST':
        form = EffectGroupForm(request.POST)
        if form.is_valid():
            with connection.cursor() as cursor:
                cursor.callproc('UpdateEffectGroup', [pk, form.cleaned_data['effect_group']])
            return redirect('effectgroup_list')
    else:
        form = EffectGroupForm(initial=effectgroup)
    return render(request, 'pharmacy/effectgroup_form.html', {'form': form, 'effectgroup': effectgroup})

def effectgroup_delete(request, pk):
    with connection.cursor() as cursor:
        cursor.callproc('GetEffectGroupById', [pk])
        row = cursor.fetchone()
        if not row:
            return redirect('effectgroup_list')
        columns = [col[0] for col in cursor.description]
        effectgroup = dict(zip(columns, row))
    if request.method == 'POST':
        with connection.cursor() as cursor:
            cursor.callproc('DeleteEffectGroup', [pk])
        return redirect('effectgroup_list')
    return render(request, 'pharmacy/effectgroup_confirm_delete.html', {'effectgroup': effectgroup})

# --- Form CRUD ---
def form_list(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Form")
        columns = [col[0] for col in cursor.description]
        forms = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return render(request, 'pharmacy/form_list.html', {'forms': forms})

def form_create(request):
    if request.method == 'POST':
        form = FormForm(request.POST)
        if form.is_valid():
            with connection.cursor() as cursor:
                cursor.callproc('InsertForm', [form.cleaned_data['form_name']])
            return redirect('form_list')
    else:
        form = FormForm()
    return render(request, 'pharmacy/form_form.html', {'form': form, 'form_obj': None})

def form_update(request, pk):
    with connection.cursor() as cursor:
        cursor.callproc('GetFormById', [pk])
        row = cursor.fetchone()
        if not row:
            return redirect('form_list')
        columns = [col[0] for col in cursor.description]
        form_obj = dict(zip(columns, row))
    if request.method == 'POST':
        form = FormForm(request.POST)
        if form.is_valid():
            with connection.cursor() as cursor:
                cursor.callproc('UpdateForm', [pk, form.cleaned_data['form_name']])
            return redirect('form_list')
    else:
        form = FormForm(initial=form_obj)
    return render(request, 'pharmacy/form_form.html', {'form': form, 'form_obj': form_obj})

def form_delete(request, pk):
    with connection.cursor() as cursor:
        cursor.callproc('GetFormById', [pk])
        row = cursor.fetchone()
        if not row:
            return redirect('form_list')
        columns = [col[0] for col in cursor.description]
        form_obj = dict(zip(columns, row))
    if request.method == 'POST':
        with connection.cursor() as cursor:
            cursor.callproc('DeleteForm', [pk])
        return redirect('form_list')
    return render(request, 'pharmacy/form_confirm_delete.html', {'form_obj': form_obj})

# --- Company CRUD ---
def company_list(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Company")
        columns = [col[0] for col in cursor.description]
        companies = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return render(request, 'pharmacy/company_list.html', {'companies': companies})

def company_create(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            with connection.cursor() as cursor:
                cursor.callproc('InsertCompany', [form.cleaned_data['company_name']])
            return redirect('company_list')
    else:
        form = CompanyForm()
    return render(request, 'pharmacy/company_form.html', {'form': form, 'company': None})

def company_update(request, pk):
    with connection.cursor() as cursor:
        cursor.callproc('GetCompanyById', [pk])
        row = cursor.fetchone()
        if not row:
            return redirect('company_list')
        columns = [col[0] for col in cursor.description]
        company = dict(zip(columns, row))
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            with connection.cursor() as cursor:
                cursor.callproc('UpdateCompany', [pk, form.cleaned_data['company_name']])
            return redirect('company_list')
    else:
        form = CompanyForm(initial=company)
    return render(request, 'pharmacy/company_form.html', {'form': form, 'company': company})

def company_delete(request, pk):
    with connection.cursor() as cursor:
        cursor.callproc('GetCompanyById', [pk])
        row = cursor.fetchone()
        if not row:
            return redirect('company_list')
        columns = [col[0] for col in cursor.description]
        company = dict(zip(columns, row))
    if request.method == 'POST':
        with connection.cursor() as cursor:
            cursor.callproc('DeleteCompany', [pk])
        return redirect('company_list')
    return render(request, 'pharmacy/company_confirm_delete.html', {'company': company})

# --- Institution CRUD ---
def institution_list(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Institution")
        columns = [col[0] for col in cursor.description]
        institutions = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return render(request, 'pharmacy/institution_list.html', {'institutions': institutions})

def institution_create(request):
    if request.method == 'POST':
        form = InstitutionForm(request.POST)
        if form.is_valid():
            with connection.cursor() as cursor:
                cursor.callproc('InsertInstitution', [form.cleaned_data['institution']])
            return redirect('institution_list')
    else:
        form = InstitutionForm()
    return render(request, 'pharmacy/institution_form.html', {'form': form, 'institution': None})

def institution_update(request, pk):
    with connection.cursor() as cursor:
        cursor.callproc('GetInstitutionById', [pk])
        row = cursor.fetchone()
        if not row:
            return redirect('institution_list')
        columns = [col[0] for col in cursor.description]
        institution = dict(zip(columns, row))
    if request.method == 'POST':
        form = InstitutionForm(request.POST)
        if form.is_valid():
            with connection.cursor() as cursor:
                cursor.callproc('UpdateInstitution', [pk, form.cleaned_data['institution']])
            return redirect('institution_list')
    else:
        form = InstitutionForm(initial=institution)
    return render(request, 'pharmacy/institution_form.html', {'form': form, 'institution': institution})

def institution_delete(request, pk):
    with connection.cursor() as cursor:
        cursor.callproc('GetInstitutionById', [pk])
        row = cursor.fetchone()
        if not row:
            return redirect('institution_list')
        columns = [col[0] for col in cursor.description]
        institution = dict(zip(columns, row))
    if request.method == 'POST':
        with connection.cursor() as cursor:
            cursor.callproc('DeleteInstitution', [pk])
        return redirect('institution_list')
    return render(request, 'pharmacy/institution_confirm_delete.html', {'institution': institution})

# --- Shelf CRUD ---
def shelf_list(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Shelf")
        columns = [col[0] for col in cursor.description]
        shelves = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return render(request, 'pharmacy/shelf_list.html', {'shelves': shelves})

def shelf_create(request):
    if request.method == 'POST':
        form = ShelfForm(request.POST)
        if form.is_valid():
            with connection.cursor() as cursor:
                cursor.callproc('InsertShelf', [form.cleaned_data['shelf_location']])
            return redirect('shelf_list')
    else:
        form = ShelfForm()
    return render(request, 'pharmacy/shelf_form.html', {'form': form, 'shelf': None})

def shelf_update(request, pk):
    with connection.cursor() as cursor:
        cursor.callproc('GetShelfById', [pk])
        row = cursor.fetchone()
        if not row:
            return redirect('shelf_list')
        columns = [col[0] for col in cursor.description]
        shelf = dict(zip(columns, row))
    if request.method == 'POST':
        form = ShelfForm(request.POST)
        if form.is_valid():
            with connection.cursor() as cursor:
                cursor.callproc('UpdateShelf', [pk, form.cleaned_data['shelf_location']])
            return redirect('shelf_list')
    else:
        form = ShelfForm(initial=shelf)
    return render(request, 'pharmacy/shelf_form.html', {'form': form, 'shelf': shelf})

def shelf_delete(request, pk):
    with connection.cursor() as cursor:
        cursor.callproc('GetShelfById', [pk])
        row = cursor.fetchone()
        if not row:
            return redirect('shelf_list')
        columns = [col[0] for col in cursor.description]
        shelf = dict(zip(columns, row))
    if request.method == 'POST':
        with connection.cursor() as cursor:
            cursor.callproc('DeleteShelf', [pk])
        return redirect('shelf_list')
    return render(request, 'pharmacy/shelf_confirm_delete.html', {'shelf': shelf})

# --- PrescriptionIssuance CRUD ---
def prescriptionissuance_list(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM PrescriptionIssuance")
        columns = [col[0] for col in cursor.description]
        issuances = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return render(request, 'pharmacy/prescriptionissuance_list.html', {'issuances': issuances})

def prescriptionissuance_create(request):
    if request.method == 'POST':
        form = PrescriptionIssuanceForm(request.POST)
        if form.is_valid():
            with connection.cursor() as cursor:
                cursor.callproc('InsertPrescriptionIssuance', [form.cleaned_data['issuance_no']])
            return redirect('prescriptionissuance_list')
    else:
        form = PrescriptionIssuanceForm()
    return render(request, 'pharmacy/prescriptionissuance_form.html', {'form': form, 'issuance': None})

def prescriptionissuance_update(request, pk):
    with connection.cursor() as cursor:
        cursor.callproc('GetPrescriptionIssuanceById', [pk])
        row = cursor.fetchone()
        if not row:
            return redirect('prescriptionissuance_list')
        columns = [col[0] for col in cursor.description]
        issuance = dict(zip(columns, row))
    if request.method == 'POST':
        form = PrescriptionIssuanceForm(request.POST)
        if form.is_valid():
            with connection.cursor() as cursor:
                cursor.callproc('UpdatePrescriptionIssuance', [pk, form.cleaned_data['issuance_no']])
            return redirect('prescriptionissuance_list')
    else:
        form = PrescriptionIssuanceForm(initial=issuance)
    return render(request, 'pharmacy/prescriptionissuance_form.html', {'form': form, 'issuance': issuance})

def prescriptionissuance_delete(request, pk):
    with connection.cursor() as cursor:
        cursor.callproc('GetPrescriptionIssuanceById', [pk])
        row = cursor.fetchone()
        if not row:
            return redirect('prescriptionissuance_list')
        columns = [col[0] for col in cursor.description]
        issuance = dict(zip(columns, row))
    if request.method == 'POST':
        with connection.cursor() as cursor:
            cursor.callproc('DeletePrescriptionIssuance', [pk])
        return redirect('prescriptionissuance_list')
    return render(request, 'pharmacy/prescriptionissuance_confirm_delete.html', {'issuance': issuance})

# --- Customer CRUD ---
def customer_list(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Customer")
        columns = [col[0] for col in cursor.description]
        customers = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return render(request, 'pharmacy/customer_list.html', {'customers': customers})

def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            with connection.cursor() as cursor:
                cursor.callproc('InsertCustomer', [form.cleaned_data['name'], form.cleaned_data['phone'], form.cleaned_data['email']])
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'pharmacy/customer_form.html', {'form': form, 'customer': None})

def customer_update(request, pk):
    with connection.cursor() as cursor:
        cursor.callproc('GetCustomerById', [pk])
        row = cursor.fetchone()
        if not row:
            return redirect('customer_list')
        columns = [col[0] for col in cursor.description]
        customer = dict(zip(columns, row))
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            with connection.cursor() as cursor:
                cursor.callproc('UpdateCustomer', [pk, form.cleaned_data['name'], form.cleaned_data['phone'], form.cleaned_data['email']])
            return redirect('customer_list')
    else:
        form = CustomerForm(initial=customer)
    return render(request, 'pharmacy/customer_form.html', {'form': form, 'customer': customer})

def customer_delete(request, pk):
    with connection.cursor() as cursor:
        cursor.callproc('GetCustomerById', [pk])
        row = cursor.fetchone()
        if not row:
            return redirect('customer_list')
        columns = [col[0] for col in cursor.description]
        customer = dict(zip(columns, row))
    if request.method == 'POST':
        with connection.cursor() as cursor:
            cursor.callproc('DeleteCustomer', [pk])
        return redirect('customer_list')
    return render(request, 'pharmacy/customer_confirm_delete.html', {'customer': customer})

# --- MedicineSale CRUD ---
def medicinesale_list(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM MedicineSale")
        columns = [col[0] for col in cursor.description]
        sales = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return render(request, 'pharmacy/medicinesale_list.html', {'sales': sales})

def medicinesale_create(request):
    medicine_id_prefill = request.GET.get('medicine_id')
    with connection.cursor() as cursor:
        cursor.execute("SELECT medicine_id, medicine_name FROM Medicine")
        medicines = cursor.fetchall()
        cursor.execute("SELECT institution_id, institution FROM Institution")
        institutions = cursor.fetchall()
        cursor.execute("SELECT customer_id, name FROM Customer")
        customers = cursor.fetchall()
    if request.method == 'POST':
        form = MedicineSaleForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            medicine_id = int(request.POST.get('medicine_id') or 0) or None
            institution_id = request.POST.get('institution_id')
            institution_id = int(institution_id) if institution_id else None
            customer_id = request.POST.get('customer_id')
            customer_id = int(customer_id) if customer_id else None
            with connection.cursor() as cursor:
                cursor.callproc('InsertMedicineSale', [
                    data['sale_price'], data['quantity'], medicine_id, data['barcode'], institution_id, customer_id
                ])
            return redirect('medicinesale_list')
    else:
        initial = {}
        if medicine_id_prefill:
            initial['medicine_id'] = medicine_id_prefill
        form = MedicineSaleForm(initial=initial)
    return render(request, 'pharmacy/medicinesale_form.html', {
        'form': form,
        'sale': None,
        'medicines': medicines,
        'institutions': institutions,
        'customers': customers
    })

def medicinesale_update(request, pk):
    with connection.cursor() as cursor:
        cursor.callproc('GetMedicineSaleById', [pk])
        row = cursor.fetchone()
        if not row:
            return redirect('medicinesale_list')
        columns = [col[0] for col in cursor.description]
        sale = dict(zip(columns, row))
        cursor.execute("SELECT medicine_id, medicine_name FROM Medicine")
        medicines = cursor.fetchall()
        cursor.execute("SELECT institution_id, institution FROM Institution")
        institutions = cursor.fetchall()
        cursor.execute("SELECT customer_id, name FROM Customer")
        customers = cursor.fetchall()
    if request.method == 'POST':
        form = MedicineSaleForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            medicine_id = int(request.POST.get('medicine_id') or 0) or None
            institution_id = request.POST.get('institution_id')
            institution_id = int(institution_id) if institution_id else None
            customer_id = request.POST.get('customer_id')
            customer_id = int(customer_id) if customer_id else None
            with connection.cursor() as cursor:
                cursor.callproc('UpdateMedicineSale', [
                    pk, data['sale_price'], data['quantity'], medicine_id, data['barcode'], institution_id, customer_id
                ])
            return redirect('medicinesale_list')
    else:
        form = MedicineSaleForm(initial=sale)
    return render(request, 'pharmacy/medicinesale_form.html', {
        'form': form,
        'sale': sale,
        'medicines': medicines,
        'institutions': institutions,
        'customers': customers
    })

def medicinesale_delete(request, pk):
    with connection.cursor() as cursor:
        cursor.callproc('GetMedicineSaleById', [pk])
        row = cursor.fetchone()
        if not row:
            return redirect('medicinesale_list')
        columns = [col[0] for col in cursor.description]
        sale = dict(zip(columns, row))
    if request.method == 'POST':
        with connection.cursor() as cursor:
            cursor.callproc('DeleteMedicineSale', [pk])
        return redirect('medicinesale_list')
    return render(request, 'pharmacy/medicinesale_confirm_delete.html', {'sale': sale})

# --- Statistics View ---
def statistics_view(request):
    stats = {}
    with connection.cursor() as cursor:
        cursor.execute('SELECT COUNT(*) FROM Medicine')
        stats['total_medicines'] = cursor.fetchone()[0]
        cursor.execute('SELECT COUNT(*) FROM Customer')
        stats['total_customers'] = cursor.fetchone()[0]
        cursor.execute('SELECT COUNT(*) FROM MedicineSale')
        stats['total_sales'] = cursor.fetchone()[0]
        cursor.execute('SELECT COUNT(*) FROM Company')
        stats['total_companies'] = cursor.fetchone()[0]
        cursor.execute('SELECT COUNT(*) FROM Institution')
        stats['total_institutions'] = cursor.fetchone()[0]
        cursor.execute('SELECT COUNT(*) FROM Shelf')
        stats['total_shelves'] = cursor.fetchone()[0]
        cursor.execute('SELECT COUNT(*) FROM EffectGroup')
        stats['total_effectgroups'] = cursor.fetchone()[0]
        cursor.execute('SELECT COUNT(*) FROM Form')
        stats['total_forms'] = cursor.fetchone()[0]
        cursor.execute('SELECT COUNT(*) FROM PrescriptionIssuance')
        stats['total_prescriptions'] = cursor.fetchone()[0]
    return render(request, 'pharmacy/statistics.html', {'stats': stats})

def medicine_list(request):
    stats = {}
    with connection.cursor() as cursor:
        cursor.execute('SELECT COUNT(*) FROM Medicine')
        stats['total_medicines'] = cursor.fetchone()[0]
        cursor.execute('SELECT COUNT(*) FROM Customer')
        stats['total_customers'] = cursor.fetchone()[0]
        cursor.execute('SELECT COUNT(*) FROM MedicineSale')
        stats['total_sales'] = cursor.fetchone()[0]
        cursor.execute('SELECT COUNT(*) FROM Company')
        stats['total_companies'] = cursor.fetchone()[0]
        cursor.execute("SELECT * FROM Medicine")
        columns = [col[0] for col in cursor.description]
        medicines = [dict(zip(columns, row)) for row in cursor.fetchall()]
    # Turkish translations for table headers and buttons
    tr_labels = {
        'barcode': 'Barkod',
        'medicine_name': 'İlaç Adı',
        'price': 'Fiyat',
        'in_stock': 'Stok',
        'company_id': 'Firma',
        'form_id': 'Form',
        'effect_group_id': 'Etki Grubu',
        'shelf_id': 'Raf',
        'prescription_id': 'Reçete',
        'edit': 'Düzenle',
        'delete': 'Sil',
        'add_sale': 'Satış Ekle',
        'medicines': 'İlaçlar',
        'customers': 'Müşteriler',
        'sales': 'Satışlar',
        'companies': 'Firmalar',
        'actions': 'İşlemler',
        'statistics': 'İstatistikler',
        'total_medicines': 'Toplam İlaç',
        'total_customers': 'Toplam Müşteri',
        'total_sales': 'Toplam Satış',
        'total_companies': 'Toplam Firma',
    }
    return render(request, 'pharmacy/medicine_list.html', {'medicines': medicines, 'stats': stats, 'tr_labels': tr_labels})

def medicine_create(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT company_id, company_name FROM Company")
        companies = cursor.fetchall()
        cursor.execute("SELECT form_id, form_name FROM Form")
        forms = cursor.fetchall()
        cursor.execute("SELECT effect_group_id, effect_group FROM EffectGroup")
        effectgroups = cursor.fetchall()
        cursor.execute("SELECT shelf_id, shelf_location FROM Shelf")
        shelves = cursor.fetchall()
        cursor.execute("SELECT issuance_id, issuance_no FROM PrescriptionIssuance")
        issuances = cursor.fetchall()
    if request.method == 'POST':
        data = request.POST
        with connection.cursor() as cursor:
            cursor.callproc('InsertMedicine', [
                data['barcode'], data['medicine_name'], data['price'], data['in_stock'],
                data['company_id'], data['form_id'], data['effect_group_id'],
                data.get('shelf_id') or None, data.get('prescription_id') or None
            ])
        return redirect('medicine_list')
    return render(request, 'pharmacy/medicine_form.html', {
        'companies': companies,
        'forms': forms,
        'effectgroups': effectgroups,
        'shelves': shelves,
        'issuances': issuances,
        'medicine': None
    })

def medicine_update(request, pk):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Medicine WHERE medicine_id = %s", [pk])
        row = cursor.fetchone()
        if not row:
            return redirect('medicine_list')
        columns = [col[0] for col in cursor.description]
        medicine = dict(zip(columns, row))
        cursor.execute("SELECT company_id, company_name FROM Company")
        companies = cursor.fetchall()
        cursor.execute("SELECT form_id, form_name FROM Form")
        forms = cursor.fetchall()
        cursor.execute("SELECT effect_group_id, effect_group FROM EffectGroup")
        effectgroups = cursor.fetchall()
        cursor.execute("SELECT shelf_id, shelf_location FROM Shelf")
        shelves = cursor.fetchall()
        cursor.execute("SELECT issuance_id, issuance_no FROM PrescriptionIssuance")
        issuances = cursor.fetchall()
    if request.method == 'POST':
        data = request.POST
        with connection.cursor() as cursor:
            cursor.callproc('UpdateMedicine', [
                pk, data['barcode'], data['medicine_name'], data['price'], data['in_stock'],
                data['company_id'], data['form_id'], data['effect_group_id'],
                data.get('shelf_id') or None, data.get('prescription_id') or None
            ])
        return redirect('medicine_list')
    return render(request, 'pharmacy/medicine_form.html', {
        'form': None,
        'medicine': medicine,
        'companies': companies,
        'forms': forms,
        'effectgroups': effectgroups,
        'shelves': shelves,
        'issuances': issuances
    })

def medicine_delete(request, pk):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Medicine WHERE medicine_id = %s", [pk])
        row = cursor.fetchone()
        if not row:
            return redirect('medicine_list')
        columns = [col[0] for col in cursor.description]
        medicine = dict(zip(columns, row))
    if request.method == 'POST':
        with connection.cursor() as cursor:
            cursor.callproc('DeleteMedicine', [pk])
        return redirect('medicine_list')
    return render(request, 'pharmacy/medicine_confirm_delete.html', {'medicine': medicine})

def get_total_stock_for_company(request, company_id):
    total_stock = 0
    with connection.cursor() as cursor:
        cursor.execute('SELECT GetTotalStockForCompany(%s)', [company_id])
        row = cursor.fetchone()
        if row:
            total_stock = row[0]
    return render(request, 'pharmacy/company_total_stock.html', {'company_id': company_id, 'total_stock': total_stock})
