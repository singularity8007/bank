#!/usr/bin/env python3
"""
Proper Endpoint Tester for the Educational Bank Project
Tests in correct order: Customer → Account → (later Transactions)
"""

import requests
import json
from uuid import UUID

BASE_URL = "http://127.0.0.1:8000"

def print_result(name, response):
    print(f"\n{'='*70}")
    print(f"Testing: {name}")
    print(f"Status Code: {response.status_code}")
    try:
        data = response.json()
        print(json.dumps(data, indent=2, default=str))
        return data
    except:
        print(response.text)
        return None


def test_bank_flow():
    print("🚀 Starting Proper Bank API Test Flow\n")

    # ========== 1. Create a Customer (Signup) ==========
    signup_data = {
        "first_name": "Hamza",
        "last_name": "Mehmood",
        "email": "hamza.test3@example.com",
        "phone_number": "555-111-2222",
        "ssn": "111-22-3333",
        "date_of_birth": "2013-08-20",
        "address": "789 Learning Street, Houston, TX",
        "password": "TestPass456"
    }
    
    signup_response = requests.post(f"{BASE_URL}/auth/signup", json=signup_data)
    customer_data = print_result("1. POST /auth/signup (Create Customer)", signup_response)
    
    if not customer_data or "customer_id" not in customer_data:
        print("❌ Signup failed. Cannot continue.")
        return
    
    real_customer_id = customer_data["customer_id"]
    print(f"\n✅ Real Customer ID captured: {real_customer_id}")

    # ========== 2. Create an Account using real customer_id ==========
    account_data = {
        "account_type": "checking"
    }
    
    # We need to temporarily modify how we call the account endpoint
    # For now, we'll use the router directly with the real ID
    print("\n" + "="*70)
    print("Note: Account creation currently uses placeholder in code.")
    print("We'll update the account router next to accept real customer_id.")
    print("="*70)

    # For immediate testing, let's just list accounts (will be empty or show previous)
    list_response = requests.get(f"{BASE_URL}/accounts/")
    print_result("2. GET /accounts/ (List Accounts)", list_response)

    print("\n🎉 Basic flow test completed!")
    print("Next step: We will update the account creation to use real customer_id.")


if __name__ == "__main__":
    test_bank_flow()
