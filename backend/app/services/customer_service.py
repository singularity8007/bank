from app.database import get_connection
from app.logging_config import logger
from argon2 import PasswordHasher
import uuid

ph = PasswordHasher()


def create_customer(customer_data):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            password_hash = ph.hash(customer_data.password)
            customer_id = uuid.uuid4()

            query = """
                INSERT INTO customers (
                    customerid, 
                    firstname, 
                    lastname, 
                    email, 
                    phonenumber, 
                    socialsecuritynumber, 
                    dateofbirth, 
                    cust_address, 
                    password_hash
                ) VALUES (
                    %(customerid)s,
                    %(firstname)s,
                    %(lastname)s,
                    %(email)s,
                    %(phonenumber)s,
                    %(socialsecuritynumber)s,
                    %(dateofbirth)s,
                    %(cust_address)s,
                    %(password_hash)s
                )
                RETURNING customerid, firstname, lastname, email
            """

            params = {
                "customerid": customer_id,
                "firstname": customer_data.first_name,
                "lastname": customer_data.last_name,
                "email": customer_data.email,
                "phonenumber": customer_data.phone_number,
                "socialsecuritynumber": customer_data.ssn,
                "dateofbirth": customer_data.date_of_birth,
                "cust_address": customer_data.address,
                "password_hash": password_hash
            }

            cur.execute(query, params)
            result = cur.fetchone()
            conn.commit()

            logger.info(f"Customer created successfully: {result['email']}")
            return result

    except Exception as e:
        conn.rollback()
        logger.error(f"Error creating customer: {e}")
        raise
    finally:
        conn.close()


def get_customer_by_email(email: str):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT customerid, firstname, lastname, email 
                FROM customers 
                WHERE email = %(email)s
            """, {"email": email})
            return cur.fetchone()
    finally:
        conn.close()