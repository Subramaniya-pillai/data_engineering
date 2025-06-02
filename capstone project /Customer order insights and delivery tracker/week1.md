# <p align="center" > Capstone Project: Customer Order Insights & Delivery Tracker  </p>

## Week 1: Database Foundations – MySQL & MongoDB

---

##  Objective
Create a system to:
- Track customer orders and delivery status
- Generate customer and delivery insights
- Use MySQL for structured data and MongoDB for unstructured customer feedback

---


##  MySQL Deliverables

###  Table Design (DDL)

```
CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(15)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    order_date DATE,
    delivery_date DATE,
    status VARCHAR(50),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE delivery_status (
    delivery_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT,
    status VARCHAR(50),
    updated_at DATETIME,
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);
```
### CRUD Operations

Insert Sample Data
```
-- Customers
INSERT INTO customers (name, email, phone)
VALUES 
('mani', '.com', '1234567890'),
('Bob', 'bob@example.com', '2345678901'),
('Charlie', 'charlie@example.com', '3456789012');

-- Orders
INSERT INTO orders (customer_id, order_date, delivery_date, status)
VALUES 
(1, '2025-06-01', '2025-06-05', 'Delivered'),
(1, '2025-06-10', '2025-06-14', 'Delayed'),
(2, '2025-06-02', '2025-06-06', 'Delivered'),
(3, '2025-06-03', '2025-06-09', 'Delayed');

-- Delivery Status
INSERT INTO delivery_status (order_id, status, updated_at)
VALUES 
(1, 'Delivered', NOW()),
(2, 'Delayed', NOW()),
(3, 'Delivered', NOW()),
(4, 'Delayed', NOW());

```

###  Read 

```
SELECT * FROM orders WHERE customer_id = 1;
```
### Update 
```
UPDATE orders SET status = 'Delivered' WHERE order_id = 2;
```

### Delete 
```
DELETE FROM delivery_status WHERE delivery_id = 4;
```

### Stored Procedure: Delayed Deliveries
```
DELIMITER $$

CREATE PROCEDURE GetDelayedDeliveries(IN cust_id INT)
BEGIN
    SELECT o.order_id, o.delivery_date, o.status
    FROM orders o
    WHERE o.customer_id = cust_id AND o.status = 'Delayed';
END$$

DELIMITER ;
```

### Call:
```
CALL GetDelayedDeliveries(1);

```
# <p align="center" > MongoDB Deliverables </p>

 
###  Insert Sample Feedback
```
use customer_feedback

db.feedback.insertMany([
  {
    customer_id: 1,
    feedback: "The order was late but customer service was helpful.",
    date: new Date("2025-06-01")
  },
  {
    customer_id: 2,
    feedback: "Fast delivery. Great experience!",
    date: new Date("2025-06-02")
  },
  {
    customer_id: 1,
    feedback: "Package was damaged on arrival.",
    date: new Date("2025-06-12")
  },
  {
    customer_id: 3,
    feedback: "Delivery was delayed, but I was informed in advance.",
    date: new Date("2025-06-13")
  },
  {
    customer_id: 2,
    feedback: "Smooth and quick ordering process.",
    date: new Date("2025-06-15")
  }
])
```
###  Index by Customer ID
```
db.feedback.createIndex({ customer_id: 1 })
```
