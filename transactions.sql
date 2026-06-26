CREATE TABLE bank.Transaction (
    SOURCE_ACCOUNT_ID UUID,
    Receipient_Account_ID UUID,
    TRANSACTION_ID UUID PRIMARY KEY,
    amount DECIMAL(10, 2) NOT NULL,
    Tansaction_type VARCHAR(50) NOT NULL,
    Transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (SOURCE_ACCOUNT_ID) REFERENCES Bank.Account(ACCOUNT_ID),
    FOREIGN KEY (Receipient_Account_ID) REFERENCES Bank.Account(ACCOUNT_ID),
    Transaction_Status VARCHAR(50) NOT NULL,
    Notes VARCHAR(512),
    transaction_direction VARCHAR(8) NOT NULL -- INCOMING or OUTGOING

);

