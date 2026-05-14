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

-- Transcations table
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
    CONSTRAINT fk_category FOREIGN KEY (category_id) REFERENCES Transaction_Categories(categorY_id),
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

-- Tag manegement table
CREATE TABLE Tags (
    tag_id INT AUTO_INCREMENT PRIMARY KEY,
    tag_name VARCHAR(50) NOT NULL UNIQUE
);

-- Transactions Tage table
CREATE TABLE Transaction_Tags (
    transaction_id INT NOT NULL,
    tag_id INT NOT NULL,
    PRIMARY KEY (transaction_id, tag_id),
    FOREIGN KEY (transaction_id) REFERENCES Transactions(transaction_id),
    FOREIGN KEY (tag_id) REFERENCES Tags(tag_id)
);