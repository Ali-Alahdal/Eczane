-- ecazne_db veritabanı oluşturuluyor
create database ecazne_db;

-- Kullanılacak veritabanı seçiliyor
default use ecazne_db;

-- Etki grupları tablosu (ör: antibiyotik, analjezik)
CREATE TABLE EffectGroup (
    effect_group_id INT AUTO_INCREMENT PRIMARY KEY,
    effect_group VARCHAR(100) NOT NULL
);

-- İlaç formu tablosu (ör: tablet, şurup)
CREATE TABLE Form (
    form_id INT AUTO_INCREMENT PRIMARY KEY,
    form_name VARCHAR(100) NOT NULL
);

-- Firma tablosu (ilaç üreticileri)
CREATE TABLE Company (
    company_id INT AUTO_INCREMENT PRIMARY KEY,
    company_name VARCHAR(100) NOT NULL
);

-- Kurum tablosu (ör: SGK, özel sigorta)
CREATE TABLE Institution (
    institution_id INT AUTO_INCREMENT PRIMARY KEY,
    institution VARCHAR(100) NOT NULL
);

-- Raf tablosu (ilaçların bulunduğu raflar)
CREATE TABLE Shelf (
    shelf_id INT AUTO_INCREMENT PRIMARY KEY,
    shelf_location VARCHAR(100) NOT NULL
);

-- Reçete veriliş tablosu
CREATE TABLE PrescriptionIssuance (
    issuance_id INT AUTO_INCREMENT PRIMARY KEY,
    issuance_no VARCHAR(100) NOT NULL
);

-- Müşteri tablosu
CREATE TABLE Customer (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    email VARCHAR(254)
);

-- İlaç tablosu
CREATE TABLE Medicine (
    medicine_id INT AUTO_INCREMENT PRIMARY KEY,
    barcode VARCHAR(50) UNIQUE NOT NULL,
    medicine_name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    in_stock INT NOT NULL,
    company_id INT NOT NULL,
    form_id INT NOT NULL,
    effect_group_id INT NOT NULL,
    shelf_id INT,
    prescription_id INT,
    FOREIGN KEY (company_id) REFERENCES Company(company_id),
    FOREIGN KEY (form_id) REFERENCES Form(form_id),
    FOREIGN KEY (effect_group_id) REFERENCES EffectGroup(effect_group_id),
    FOREIGN KEY (shelf_id) REFERENCES Shelf(shelf_id),
    FOREIGN KEY (prescription_id) REFERENCES PrescriptionIssuance(issuance_id)
);

-- İlaç satış tablosu
CREATE TABLE MedicineSale (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    sale_price DECIMAL(10,2) NOT NULL,
    quantity INT NOT NULL,
    sale_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    medicine_id INT NOT NULL,
    barcode VARCHAR(50) NOT NULL,
    institution_id INT,
    customer_id INT,
    FOREIGN KEY (medicine_id) REFERENCES Medicine(medicine_id),
    FOREIGN KEY (institution_id) REFERENCES Institution(institution_id),
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);

-- CRUD işlemleri için saklı yordamlar (Stored Procedures)

-- İlaç ekleme prosedürü
DELIMITER //
CREATE PROCEDURE InsertMedicine(
    IN p_barcode VARCHAR(50),
    IN p_medicine_name VARCHAR(100),
    IN p_price DECIMAL(10,2),
    IN p_in_stock INT,
    IN p_company_id INT,
    IN p_form_id INT,
    IN p_effect_group_id INT,
    IN p_shelf_id INT,
    IN p_prescription_id INT
)
BEGIN
    INSERT INTO Medicine (barcode, medicine_name, price, in_stock, company_id, form_id, effect_group_id, shelf_id, prescription_id)
    VALUES (p_barcode, p_medicine_name, p_price, p_in_stock, p_company_id, p_form_id, p_effect_group_id, p_shelf_id, p_prescription_id);
END //
DELIMITER ;

-- İlaç güncelleme prosedürü
DELIMITER //
CREATE PROCEDURE UpdateMedicine(
    IN p_medicine_id INT,
    IN p_barcode VARCHAR(50),
    IN p_medicine_name VARCHAR(100),
    IN p_price DECIMAL(10,2),
    IN p_in_stock INT,
    IN p_company_id INT,
    IN p_form_id INT,
    IN p_effect_group_id INT,
    IN p_shelf_id INT,
    IN p_prescription_id INT
)
BEGIN
    UPDATE Medicine SET barcode=p_barcode, medicine_name=p_medicine_name, price=p_price, in_stock=p_in_stock, company_id=p_company_id, form_id=p_form_id, effect_group_id=p_effect_group_id, shelf_id=p_shelf_id, prescription_id=p_prescription_id
    WHERE medicine_id=p_medicine_id;
END //
DELIMITER ;

-- İlaç silme prosedürü
DELIMITER //
CREATE PROCEDURE DeleteMedicine(IN p_medicine_id INT)
BEGIN
    DELETE FROM Medicine WHERE medicine_id=p_medicine_id;
END //
DELIMITER ;

-- Barkoda göre ilaç sorgulama prosedürü
DELIMITER //
CREATE PROCEDURE GetMedicineByBarcode(IN p_barcode VARCHAR(50))
BEGIN
    SELECT * FROM Medicine WHERE barcode=p_barcode;
END //
DELIMITER ;

-- Diğer tüm tablolar için benzer CRUD prosedürleri (Company, Customer, EffectGroup, Form, Institution, Shelf, PrescriptionIssuance, MedicineSale)

-- Kullanıcı tanımlı fonksiyon örneği: Bir firmanın toplam stok miktarını döndürür
DELIMITER //
CREATE FUNCTION GetTotalStockForCompany(p_company_id INT) RETURNS INT
READS SQL DATA
BEGIN
    DECLARE total_stock INT;
    SELECT SUM(in_stock) INTO total_stock FROM Medicine WHERE company_id = p_company_id;
    RETURN IFNULL(total_stock, 0);
END //
DELIMITER ;

-- Tetikleyiciler (Triggers) örnekleri

-- Satış sonrası stok güncelleme tetikleyicisi
DELIMITER //
CREATE TRIGGER AfterMedicineSaleInsert
AFTER INSERT ON MedicineSale
FOR EACH ROW
BEGIN
    UPDATE Medicine SET in_stock = in_stock - NEW.quantity WHERE medicine_id = NEW.medicine_id;
END //
DELIMITER ;

-- Negatif stok önleyici tetikleyici
DELIMITER //
CREATE TRIGGER BeforeMedicineSaleInsert
BEFORE INSERT ON MedicineSale
FOR EACH ROW
BEGIN
    IF (SELECT in_stock FROM Medicine WHERE medicine_id = NEW.medicine_id) < NEW.quantity THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Yeterli stok yok.';
    END IF;
END //
DELIMITER ;

-- CRUD için EffectGroup
DELIMITER //
CREATE PROCEDURE InsertEffectGroup(IN p_effect_group VARCHAR(100))
BEGIN
    INSERT INTO EffectGroup (effect_group) VALUES (p_effect_group);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE UpdateEffectGroup(IN p_effect_group_id INT, IN p_effect_group VARCHAR(100))
BEGIN
    UPDATE EffectGroup SET effect_group = p_effect_group WHERE effect_group_id = p_effect_group_id;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE DeleteEffectGroup(IN p_effect_group_id INT)
BEGIN
    DELETE FROM EffectGroup WHERE effect_group_id = p_effect_group_id;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE GetEffectGroupById(IN p_effect_group_id INT)
BEGIN
    SELECT * FROM EffectGroup WHERE effect_group_id = p_effect_group_id;
END //
DELIMITER ;

-- CRUD için Form
DELIMITER //
CREATE PROCEDURE InsertForm(IN p_form_name VARCHAR(100))
BEGIN
    INSERT INTO Form (form_name) VALUES (p_form_name);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE UpdateForm(IN p_form_id INT, IN p_form_name VARCHAR(100))
BEGIN
    UPDATE Form SET form_name = p_form_name WHERE form_id = p_form_id;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE DeleteForm(IN p_form_id INT)
BEGIN
    DELETE FROM Form WHERE form_id = p_form_id;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE GetFormById(IN p_form_id INT)
BEGIN
    SELECT * FROM Form WHERE form_id = p_form_id;
END //
DELIMITER ;

-- CRUD için Company
DELIMITER //
CREATE PROCEDURE InsertCompany(IN p_company_name VARCHAR(100))
BEGIN
    INSERT INTO Company (company_name) VALUES (p_company_name);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE UpdateCompany(IN p_company_id INT, IN p_company_name VARCHAR(100))
BEGIN
    UPDATE Company SET company_name = p_company_name WHERE company_id = p_company_id;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE DeleteCompany(IN p_company_id INT)
BEGIN
    DELETE FROM Company WHERE company_id = p_company_id;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE GetCompanyById(IN p_company_id INT)
BEGIN
    SELECT * FROM Company WHERE company_id = p_company_id;
END //
DELIMITER ;

-- CRUD için Institution
DELIMITER //
CREATE PROCEDURE InsertInstitution(IN p_institution VARCHAR(100))
BEGIN
    INSERT INTO Institution (institution) VALUES (p_institution);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE UpdateInstitution(IN p_institution_id INT, IN p_institution VARCHAR(100))
BEGIN
    UPDATE Institution SET institution = p_institution WHERE institution_id = p_institution_id;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE DeleteInstitution(IN p_institution_id INT)
BEGIN
    DELETE FROM Institution WHERE institution_id = p_institution_id;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE GetInstitutionById(IN p_institution_id INT)
BEGIN
    SELECT * FROM Institution WHERE institution_id = p_institution_id;
END //
DELIMITER ;

-- CRUD için Shelf
DELIMITER //
CREATE PROCEDURE InsertShelf(IN p_shelf_location VARCHAR(100))
BEGIN
    INSERT INTO Shelf (shelf_location) VALUES (p_shelf_location);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE UpdateShelf(IN p_shelf_id INT, IN p_shelf_location VARCHAR(100))
BEGIN
    UPDATE Shelf SET shelf_location = p_shelf_location WHERE shelf_id = p_shelf_id;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE DeleteShelf(IN p_shelf_id INT)
BEGIN
    DELETE FROM Shelf WHERE shelf_id = p_shelf_id;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE GetShelfById(IN p_shelf_id INT)
BEGIN
    SELECT * FROM Shelf WHERE shelf_id = p_shelf_id;
END //
DELIMITER ;

-- CRUD için PrescriptionIssuance
DELIMITER //
CREATE PROCEDURE InsertPrescriptionIssuance(IN p_issuance_no VARCHAR(100))
BEGIN
    INSERT INTO PrescriptionIssuance (issuance_no) VALUES (p_issuance_no);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE UpdatePrescriptionIssuance(IN p_issuance_id INT, IN p_issuance_no VARCHAR(100))
BEGIN
    UPDATE PrescriptionIssuance SET issuance_no = p_issuance_no WHERE issuance_id = p_issuance_id;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE DeletePrescriptionIssuance(IN p_issuance_id INT)
BEGIN
    DELETE FROM PrescriptionIssuance WHERE issuance_id = p_issuance_id;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE GetPrescriptionIssuanceById(IN p_issuance_id INT)
BEGIN
    SELECT * FROM PrescriptionIssuance WHERE issuance_id = p_issuance_id;
END //
DELIMITER ;

-- CRUD için Customer
DELIMITER //
CREATE PROCEDURE InsertCustomer(IN p_name VARCHAR(100), IN p_phone VARCHAR(20), IN p_email VARCHAR(254))
BEGIN
    INSERT INTO Customer (name, phone, email) VALUES (p_name, p_phone, p_email);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE UpdateCustomer(IN p_customer_id INT, IN p_name VARCHAR(100), IN p_phone VARCHAR(20), IN p_email VARCHAR(254))
BEGIN
    UPDATE Customer SET name = p_name, phone = p_phone, email = p_email WHERE customer_id = p_customer_id;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE DeleteCustomer(IN p_customer_id INT)
BEGIN
    DELETE FROM Customer WHERE customer_id = p_customer_id;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE GetCustomerById(IN p_customer_id INT)
BEGIN
    SELECT * FROM Customer WHERE customer_id = p_customer_id;
END //
DELIMITER ;

-- CRUD için MedicineSale
DELIMITER //
CREATE PROCEDURE InsertMedicineSale(
    IN p_sale_price DECIMAL(10,2),
    IN p_quantity INT,
    IN p_medicine_id INT,
    IN p_barcode VARCHAR(50),
    IN p_institution_id INT,
    IN p_customer_id INT
)
BEGIN
    INSERT INTO MedicineSale (sale_price, quantity, medicine_id, barcode, institution_id, customer_id)
    VALUES (p_sale_price, p_quantity, p_medicine_id, p_barcode, p_institution_id, p_customer_id);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE UpdateMedicineSale(
    IN p_sale_id INT,
    IN p_sale_price DECIMAL(10,2),
    IN p_quantity INT,
    IN p_medicine_id INT,
    IN p_barcode VARCHAR(50),
    IN p_institution_id INT,
    IN p_customer_id INT
)
BEGIN
    UPDATE MedicineSale SET sale_price = p_sale_price, quantity = p_quantity, medicine_id = p_medicine_id, barcode = p_barcode, institution_id = p_institution_id, customer_id = p_customer_id
    WHERE sale_id = p_sale_id;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE DeleteMedicineSale(IN p_sale_id INT)
BEGIN
    DELETE FROM MedicineSale WHERE sale_id = p_sale_id;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE GetMedicineSaleById(IN p_sale_id INT)
BEGIN
    SELECT * FROM MedicineSale WHERE sale_id = p_sale_id;
END //
DELIMITER ;
