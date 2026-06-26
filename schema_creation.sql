-- Create the schema
--CREATE SCHEMA IF NOT EXISTS bank;

-- Grant all privileges on the schema to db_user
GRANT ALL PRIVILEGES ON SCHEMA bank TO db_user;

-- Grant privileges on all existing tables in the schema
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA bank TO db_user;

-- Grant privileges on all existing sequences in the schema
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA bank TO db_user;

-- Grant privileges on all existing functions in the schema
GRANT ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA bank TO db_user;
-- Grant USAGE (ability to access/see the schema)
GRANT USAGE ON SCHEMA bank TO db_user;

-- Grant CREATE (ability to create objects in the schema)
GRANT CREATE ON SCHEMA bank TO db_user;

-- Set default privileges for future objects created in the schema
ALTER DEFAULT PRIVILEGES IN SCHEMA bank
    GRANT ALL PRIVILEGES ON TABLES TO db_user;

ALTER DEFAULT PRIVILEGES IN SCHEMA bank
    GRANT ALL PRIVILEGES ON SEQUENCES TO db_user;

ALTER DEFAULT PRIVILEGES IN SCHEMA bank
    GRANT ALL PRIVILEGES ON FUNCTIONS TO db_user;

ALTER DEFAULT PRIVILEGES IN SCHEMA bank
    GRANT ALL PRIVILEGES ON ROUTINES TO db_user;
    -- If Account table is in the bank schema
GRANT USAGE ON SCHEMA bank TO db_user;
GRANT REFERENCES ON bank.account TO db_user;

-- If Account table is in a DIFFERENT schema (e.g., public)
GRANT USAGE ON SCHEMA public TO db_user;
GRANT REFERENCES ON public.account TO db_user;
-- Explicitly grant REFERENCES on the already-existing Account table
GRANT REFERENCES ON bank.account TO db_user;

-- Also grant it on all existing tables to avoid this happening again
GRANT REFERENCES ON ALL TABLES IN SCHEMA bank TO db_user;

-- Ensure future tables created by the superuser also get this
ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA bank
    GRANT ALL PRIVILEGES ON TABLES TO db_user;