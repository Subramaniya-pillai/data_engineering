#  <p align="center"> Supply Chain Monitoring and Optimization Platform </p>


### Objective:
Build a practical system to track orders, inventory, and shipments using real-world tools like MySQL,
MongoDB, Python, PySpark, Azure Databricks, and Azure DevOps.


###  <p align="center"> Week 1 – Database Foundations: MySQL & MongoDB </p>


### Capstone Tasks:
Create MySQL tables for orders, suppliers, inventory

Perform basic CRUD operations

Write stored procedures (e.g., auto reorder trigger)

Store shipment logs in MongoDB

Create indexes for efficient querying

### <p align="center"> MySQL Schema Definition </p>
```
-- Create Suppliers Table
CREATE TABLE suppliers (
    supplier_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    contact_info VARCHAR(255)
);

-- Create Inventory Table
CREATE TABLE inventory (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(100) NOT NULL,
    quantity INT NOT NULL,
    reorder_level INT NOT NULL,
    supplier_id INT,
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);

-- Create Orders Table
CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT,
    quantity INT NOT NULL,
    order_date DATE NOT NULL,
    status VARCHAR(50),
    FOREIGN KEY (product_id) REFERENCES inventory(product_id)
);
```

### Insert sample data into 'suppliers' table

```
INSERT INTO suppliers (name, contact_info) VALUES 
('energon supplies', 'mani@hexaware.com'),
('Beta Distributors', 'nithya@beta.com');
```

### Insert sample data into 'inventory' table
```
INSERT INTO inventory (product_name, quantity, reorder_level, supplier_id) VALUES
('Laptop', 50, 20, 1),   -- 50 laptops in stock, reorder if below 20, supplied by supplier with ID 1
('Mouse', 100, 30, 2);   -- 100 mice in stock, reorder if below 30, supplied by supplier with ID 2
```

### Insert a sample order into 'orders' table
```
INSERT INTO orders (product_id, quantity, order_date, status) VALUES
(1, 10, CURDATE(), 'Pending');  -- Order 10 units of product_id 1 (Laptop), order date is current date, status Pending
```
###  <p align="center">CRUD Examples </p>


### Read all records from 'inventory' table
```
SELECT * FROM inventory;
```
### Update the quantity of a product (reduce Laptop quantity by 10)
```
UPDATE inventory SET quantity = quantity - 10 WHERE product_id = 1;
```
### Delete an order with order_id = 1
```
DELETE FROM orders WHERE order_id = 1;
```
### Stored Procedure for Auto Reorder:
This procedure automatically creates new orders for products where stock is below the reorder level

```
/ Change delimiter to allow procedure creation
DELIMITER //

CREATE PROCEDURE auto_reorder()
BEGIN
    -- Insert new orders for all products with quantity less than reorder_level
    INSERT INTO orders (product_id, quantity, order_date, status)
    SELECT product_id, reorder_level * 2, CURDATE(), 'Pending'  -- Order double the reorder level quantity
    FROM inventory
    WHERE quantity < reorder_level;
END //

-- Reset delimiter back to default
DELIMITER ;

-- Call the stored procedure to place automatic reorder orders
CALL auto_reorder();

``` 
### <p align="center">mongo db </p>

### Creating Database
```
use supply_chain_db;
```
### Insert sample shipment logs into 'shipments' collection
```
 db.shipments.insertMany([
...   {
...     shipment_id: 1,
...     order_id: 101,
...     status: "In Transit",
...     last_updated: new Date("2025-06-01T10:00:00Z"),
...     location: "Warehouse A"
...   },
...   {
...     shipment_id: 2,
...     order_id: 102,
...     status: "Delivered",
...     last_updated: new Date("2025-05-30T15:30:00Z"),
...     location: "Customer Address"
...   }
... ]);
```
###  Create index on 'order_id' to speed up queries by order
```
db.shipments.createIndex({ order_id: 1 });
```

### Create compound index on 'status' and 'last_updated' for filtered queries
```
db.shipments.createIndex({ status: 1, last_updated: -1 });
```
