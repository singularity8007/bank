CREATE TABLE AuditLog (
    
    audit_id        SERIAL PRIMARY KEY,
    customer_id     UUID REFERENCES Customers(CustomerID),
    account_id      UUID REFERENCES Account(ACCOUNT_ID),
    event_type      VARCHAR(100) NOT NULL,  -- e.g. LOGIN, LOGOUT, ACCOUNT_OPENED, ACCOUNT_CLOSED, DEPOSIT, WITHDRAWAL, TRANSFER_INITIATED, TRANSFER_SETTLED, ROLLBACK
    event_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ip_address      VARCHAR(45),            -- supports IPv4 and IPv6
    description     TEXT,                   -- human-readable detail
    outcome         VARCHAR(20) NOT NULL     -- SUCCESS or FAILURE

);