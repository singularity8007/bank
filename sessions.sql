CREATE TABLE Session (
    
    session_id      VARCHAR(128) PRIMARY KEY,  -- secure random token, generated server-side
    customer_id     INT NOT NULL REFERENCES Customers(CustomerID),
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_active_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expires_at      TIMESTAMP NOT NULL,
    is_active       BOOLEAN DEFAULT TRUE,
    ip_address      VARCHAR(45)

);