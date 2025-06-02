# <p align="center" > Capstone Project: Customer Order Insights & Delivery Tracker  </p>


### <p align="center" >  Week 1: Database Foundations – MySQL & MongoDB </p>


---

##  Objective
Create a system to:
- Track customer orders and delivery status
- Generate customer and delivery insights
- Use MySQL for structured data and MongoDB for unstructured customer feedback

---


### CREATE DATABASE
```
CREATE DATABASE customer_orders;
```

### USE DATABASE
```
USE customer_orders;
```
### CREATE SCHEMA
```
CREATE SCHEMA orders;
```
CREATE TABLE: customers
```
CREATE TABLE orders.customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);
```
CREATE TABLE: orders
```
CREATE TABLE orders.orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    delivery_date DATE,
    FOREIGN KEY (customer_id) REFERENCES orders.customers(customer_id) ON DELETE CASCADE
);
```
CREATE TABLE: delivery_status
```
CREATE TABLE orders.delivery_status (
    status_id INT PRIMARY KEY,
    order_id INT,
    status VARCHAR(50),
    last_updated DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (order_id) REFERENCES orders.orders(order_id) ON DELETE CASCADE
);
```
### inserting data
```
INSERT INTO orders.customers
INSERT INTO orders.customers (customer_id, name, email) VALUES
(1, 'mani', 'mani@email.com'),
(2, 'saravana', 'saravna@email.com'),
(3, 'shakthi', 'shathi@email.com');

-- INSERT INTO orders.orders
INSERT INTO orders.orders (order_id, customer_id, order_date, delivery_date) VALUES
(101, 1, '2025-05-25', '2025-05-30'),
(102, 1, '2025-05-28', '2025-06-02'),
(103, 2, '2025-05-27', '2025-06-05'),
(104, 3, '2025-05-29', '2025-06-10');

-- INSERT INTO orders.delivery_status
INSERT INTO orders.delivery_status (status_id, order_id, status) VALUES
(1, 101, 'Delivered'),
(2, 102, 'In Transit'),
(3, 103, 'Pending'),
(4, 104, 'Delivered');
```
### CRUD OPERATIONS

### INSERT (CREATE)
```
INSERT INTO orders.orders (order_id, customer_id, order_date, delivery_date)
VALUES (105, 1, '2025-05-25', '2025-05-30');
```
### SELECT (READ)
```
SELECT * FROM orders.orders;
```
### UPDATE
```
UPDATE orders.orders
SET delivery_date = '2025-06-01'
WHERE order_id = 101;
```
### DELETE
```
DELETE FROM orders.orders WHERE order_id = 101;
```

### STORED PROCEDURE: Delayed Deliveries for a Customer
```
DELIMITER $$

CREATE PROCEDURE orders.GetDelayedDeliveries(IN CustomerId INT)
BEGIN
    SELECT o.order_id, o.delivery_date
    FROM orders.orders o
    JOIN orders.delivery_status d ON o.order_id = d.order_id
    WHERE o.customer_id = CustomerId
      AND o.delivery_date < CURDATE()
      AND d.status <> 'Delivered';
END $$

DELIMITER ;
```
### CALL PROCEDURE (example)
```
CALL orders.GetDelayedDeliveries(1);
```
### <p align="center" > MongoDB </p>

###  Tasks
- Create a MongoDB database and collection  
- Insert sample feedback documents  
- Index the collection by `customer_id`  
- Perform basic queries

---

##  MongoDB Script

```js
// 1. Use or Create Database
use customer_orders;

// 2. Create Collection & Insert Sample Feedback
db.feedback.insertMany([
  {
    customer_id: 1,
    name: "Mani",
    feedback: "Delivery was late and packaging was poor.",
    timestamp: new Date()
  },
  {
    customer_id: 2,
    name: "Mothesh",
    feedback: "Very satisfied with the fast delivery!",
    timestamp: new Date()
  },
  {
    customer_id: 3,
    name: "Saravana",
    feedback: "Received the wrong item. Support helped quickly.",
    timestamp: new Date()
  },
  {
    customer_id: 4,
    name: "Manoj",
    feedback: "Item was damaged. Not happy.",
    timestamp: new Date()
  },
  {
    customer_id: 5,
    name: "Jeeva",
    feedback: "Great service, will order again!",
    timestamp: new Date()
  },
  {
    customer_id: 6,
    name: "Nithya",
    feedback: "Late delivery but excellent support team.",
    timestamp: new Date()
  }
]);
```

3. Create Index on customer_id
```
db.feedback.createIndex({ customer_id: 1 });
```
4. Query Feedback for a Specific Customer
```
db.feedback.find({ customer_id: 3 });
```
