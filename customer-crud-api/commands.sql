-- task3

--Task 3.1 — Create Table
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    phone VARCHAR(15) NOT NULL,
    city VARCHAR(100) NOT NULL,
    age INTEGER CHECK (age >= 18),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


--Task 3.2 — Insert Sample Data
INSERT INTO customers (name, email, phone, city, age)
VALUES
('Aman Sharma', 'aman.sharma@example.com', '9876543210', 'Delhi', 25),
('Simran Kaur', 'simran.kaur@example.com', '9876543211', 'Chandigarh', 28),
('Rohit Verma', 'rohit.verma@example.com', '9876543212', 'Ludhiana', 32),
('Neha Gupta', 'neha.gupta@example.com', '9876543213', 'Amritsar', 24),
('Karan Mehta', 'karan.mehta@example.com', '9876543214', 'Rajpura', 35);

--Task 3.3 — Read Data
select * from customers
select * from customers where customer_id=10
select * from customers where city='Amritsar'

--Task 3.4 — Update Data
update customers set name='Sam' where customer_id=1
select * from customers where customer_id=1;

update customers set phone='909090909090' where customer_id=101
select * from customers where customer_id=101;

update customers set city='New York' where customer_id=110
select * from customers where customer_id=110

--Task 3.5 — Delete Data
delete from customers where customer_id=111