from django.urls import path
from . import views

urlpatterns = [
    # Home
    path("", views.medicine_list, name="home"),

    # Medicine CRUD
    path('medicines/', views.medicine_list, name='medicine_list'),
    path('medicines/create/', views.medicine_create, name='medicine_create'),
    path('medicines/<int:pk>/edit/', views.medicine_update, name='medicine_update'),
    path('medicines/<int:pk>/delete/', views.medicine_delete, name='medicine_delete'),

    # EffectGroup CRUD
    path('effectgroups/', views.effectgroup_list, name='effectgroup_list'),
    path('effectgroups/create/', views.effectgroup_create, name='effectgroup_create'),
    path('effectgroups/<int:pk>/edit/', views.effectgroup_update, name='effectgroup_update'),
    path('effectgroups/<int:pk>/delete/', views.effectgroup_delete, name='effectgroup_delete'),

    # Form CRUD
    path('forms/', views.form_list, name='form_list'),
    path('forms/create/', views.form_create, name='form_create'),
    path('forms/<int:pk>/edit/', views.form_update, name='form_update'),
    path('forms/<int:pk>/delete/', views.form_delete, name='form_delete'),

    # Company CRUD
    path('companies/', views.company_list, name='company_list'),
    path('companies/create/', views.company_create, name='company_create'),
    path('companies/<int:pk>/edit/', views.company_update, name='company_update'),
    path('companies/<int:pk>/delete/', views.company_delete, name='company_delete'),
    path('companies/<int:company_id>/total_stock/', views.get_total_stock_for_company, name='company_total_stock'),

    # Institution CRUD
    path('institutions/', views.institution_list, name='institution_list'),
    path('institutions/create/', views.institution_create, name='institution_create'),
    path('institutions/<int:pk>/edit/', views.institution_update, name='institution_update'),
    path('institutions/<int:pk>/delete/', views.institution_delete, name='institution_delete'),

    # Shelf CRUD
    path('shelves/', views.shelf_list, name='shelf_list'),
    path('shelves/create/', views.shelf_create, name='shelf_create'),
    path('shelves/<int:pk>/edit/', views.shelf_update, name='shelf_update'),
    path('shelves/<int:pk>/delete/', views.shelf_delete, name='shelf_delete'),

    # PrescriptionIssuance CRUD
    path('prescriptionissuances/', views.prescriptionissuance_list, name='prescriptionissuance_list'),
    path('prescriptionissuances/create/', views.prescriptionissuance_create, name='prescriptionissuance_create'),
    path('prescriptionissuances/<int:pk>/edit/', views.prescriptionissuance_update, name='prescriptionissuance_update'),
    path('prescriptionissuances/<int:pk>/delete/', views.prescriptionissuance_delete, name='prescriptionissuance_delete'),

    # Customer CRUD
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/create/', views.customer_create, name='customer_create'),
    path('customers/<int:pk>/edit/', views.customer_update, name='customer_update'),
    path('customers/<int:pk>/delete/', views.customer_delete, name='customer_delete'),

    # MedicineSale CRUD
    path('medicinesales/', views.medicinesale_list, name='medicinesale_list'),
    path('medicinesales/create/', views.medicinesale_create, name='medicinesale_create'),
    path('medicinesales/<int:pk>/edit/', views.medicinesale_update, name='medicinesale_update'),
    path('medicinesales/<int:pk>/delete/', views.medicinesale_delete, name='medicinesale_delete'),

    # Statistics
    path('statistics/', views.statistics_view, name='pharmacy_statistics'),
]
