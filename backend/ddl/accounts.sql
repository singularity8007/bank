--DROP TABLE IF EXISTS bank.Account CASCADE;
CREATE TABLE Bank.Account (
    Customer_ID UUID NOT NULL,
    ACCOUNT_ID UUID PRIMARY KEY,
    --password_hash VARCHAR(255) NOT NULL,
    Create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Account_type VARCHAR(50) NOT NULL,
    Available_balance DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    Current_balance DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    Account_Status VARCHAR(50) NOT NULL,
    FOREIGN KEY (Customer_ID) REFERENCES Bank.Customers(CustomerID)


);