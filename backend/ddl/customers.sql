CREATE TABLE bank.Customers (
    CustomerID UUID PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) NOT NULL UNIQUE,
    PhoneNumber VARCHAR(20) NOT NULL UNIQUE,
    SocialSecurityNumber VARCHAR(11) NOT NULL UNIQUE,
    DateOfBirth DATE NOT NULL,
    Cust_Address VARCHAR(255) NOT NULL ,
    Password_hash VARCHAR(255) NOT NULL

);


