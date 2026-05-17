-- Create the database schema if it does not exist
CREATE DATABASE IF NOT EXISTS momo_db;

USE momo_db;

DROP TABLE IF EXISTS Transaction_Tags;
DROP TABLE IF EXISTS Tags;
DROP TABLE IF EXISTS Transactions;
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Transaction_Categories;
DROP TABLE IF EXISTS System_logs;

-- Transaction_categories table
CREATE TABLE Transaction_Categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT
);

-- Users table
CREATE TABLE Users(
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    phone_number VARCHAR(15) UNIQUE NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Transactions table
CREATE TABLE Transactions(
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    sender_id INT NOT NULL,
    receiver_id  INT NOT NULL,
    category_id INT NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    transaction_date DATETIME NOT NULL,
    status ENUM('Success', 'Failed', 'Pending') DEFAULT 'Success',

    CONSTRAINT fk_sender FOREIGN KEY (sender_id) REFERENCES Users(user_id),
    CONSTRAINT fk_receiver FOREIGN KEY (receiver_id) REFERENCES Users(user_id),
    CONSTRAINT fk_category FOREIGN KEY (category_id) REFERENCES Transaction_Categories(category_id),
    CONSTRAINT chk_amount_positive CHECK (amount > 0),
    CONSTRAINT chk_parties CHECK (sender_id <> receiver_id)
);

-- System Logs table
CREATE TABLE System_logs(
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    event_type VARCHAR(50),
    description TEXT NOT NULL,
    log_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tag management table
CREATE TABLE Tags (
    tag_id INT AUTO_INCREMENT PRIMARY KEY,
    tag_name VARCHAR(50) NOT NULL UNIQUE
);

-- Transactions Tags table
CREATE TABLE Transaction_Tags (
    transaction_id INT NOT NULL,
    tag_id INT NOT NULL,
    PRIMARY KEY (transaction_id, tag_id),
    FOREIGN KEY (transaction_id) REFERENCES Transactions(transaction_id),
    FOREIGN KEY (tag_id) REFERENCES Tags(tag_id)
);

-- Seed Transaction_Categories
INSERT INTO Transaction_Categories (name, description) VALUES
('P2P Transfer', 'Direct mobile wallet transfer between two individual subscribers'),
('Merchant Payment', 'Retail purchasing settlement at an authorized vendor POS'),
('Cash-In', 'Physical currency deposit into wallet via a registered agent booth'),
('Cash-Out', 'Physical currency withdrawal from wallet executed at an agent booth'),
('Utility Bill', 'Settlement of public utility accounts like electrical power, water, or internet');

-- Seed Users
INSERT INTO Users (full_name, phone_number) VALUES
('John Doe', '+233241111111'),
('Jane Smith', '+233242222222'),
('Kofi Mensah', '+233243333333'),
('Ama Serwaa', '+233244444444'),
('Kwame Osei', '+233245555555');

-- Seed Transactions
INSERT INTO Transactions (sender_id, receiver_id, category_id, amount, transaction_date, status) VALUES
(1, 2, 1, 150.00, '2026-05-10 10:15:00', 'Success'),
(3, 4, 2, 45.50, '2026-05-11 11:20:00', 'Success'),
(5, 1, 3, 500.00, '2026-05-12 14:05:00', 'Success'),
(2, 3, 4, 100.00, '2026-05-13 16:45:00', 'Failed'),
(4, 5, 5, 85.20, '2026-05-14 09:30:00', 'Pending');

-- Seed System_logs
INSERT INTO System_logs (event_type, description) VALUES
('SMS_PARSE_SUCCESS', 'Successfully extracted SMS ID TX99238 into XML mapping schema.'),
('DB_INSUFFICIENT_FUNDS', 'Transaction failed for User ID 2 due to ledger validation error.'),
('SMS_PARSE_FAIL', 'Malformed string token encountered when processing text payload.'),
('API_TIMEOUT', 'Gateway timeout recorded while fetching third-party billing database.'),
('CRON_CLEANUP', 'Successfully executed daily indexing and temporary log compression cycles.');

-- Seed Tags
INSERT INTO Tags (tag_name) VALUES
('High-Value'),
('Suspected Fraud'),
('Reversed'),
('Business Expense'),
('Tax Exempt');

-- Seed Transaction_Tags
INSERT INTO Transaction_Tags (transaction_id, tag_id) VALUES
(3, 1), 
(4, 2), 
(4, 3), 
(1, 4), 
(2, 5);
