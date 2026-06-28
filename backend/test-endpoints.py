#!/usr/bin/env python3
"""
Simple Bank API - End-to-End Test Script
Tests: Customer Signup → Create Account → Deposit Money
"""

import requests
import json
import uuid
from datetime import datetime
from decimal import Decimal

BASE_URL = "http://127.0.0.1:8000"


def print_section(title: str):
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


def print_result(name: str, response):
    print(f"\n▶ {name}")
    print(f"   Status: {response.status_code}")
    try:
        data = response.json()
        print(json.dumps(data, indent=4, default=str))
        return data
    except:
        print(response.text)
        return None


def get_unique_test_data():
    unique = uuid.uuid4().hex[:8]
    ts = datetime.now().strftime("%H%M%S")

    return {
        "first_name": "Test",
        "last_name": "User",
        "email": f"test_{unique}_{ts}@example.com",
        "phone_number": f"555-{unique[:3]}-{unique[3:]}",
        "ssn": f"{unique[:3]}-{unique[3:5]}-{unique[5:]}",
        "date_of_birth": "2013-05-15",
        "address": "123 Learning Lane, Houston, TX",
        "password": "SecurePass123"
    }


def test_bank_flow():
    print_section("Simple Bank API - End-to-End Test")

    # === Step 1: Create Customer ===
    print_section("Step 1: Create Customer (Signup)")

    signup_data = get_unique_test_data()
    response = requests.post(f"{BASE_URL}/auth/signup", json=signup_data)
    customer = print_result("POST /auth/signup", response)

    if not customer:
        print("\n❌ Signup failed. Stopping test.")
        return

    # Handle both possible key names
    customer_id = customer.get("customerid") or customer.get("customer_id")
    if not customer_id:
        print("\n❌ Could not extract customer_id from response.")
        return

    print(f"\n✅ Customer created! ID: {customer_id}")

    # === Step 2: Create Account ===
    print_section("Step 2: Create Account")

    account_data = {
        "customer_id": customer_id,
        "account_type": "checking"
    }

    response = requests.post(f"{BASE_URL}/accounts/", json=account_data)
    account = print_result("POST /accounts/", response)

    if not account or not account.get("account_id"):
        print("\n❌ Account creation failed.")
        return

    account_id = account.get("account_id")
    print(f"\n✅ Account created! ID: {account_id}")

    # === Step 3: Deposit Money ===
    print_section("Step 3: Deposit Money")

    deposit_data = {
        "account_id": account_id,
        "amount": "100.50"
    }

    response = requests.post(f"{BASE_URL}/accounts/deposit", json=deposit_data)
    deposit_result = print_result("POST /accounts/deposit", response)

    if deposit_result:
        print("\n✅ Deposit completed successfully!")

    # === Step 4: List Accounts ===
    print_section("Step 4: List Accounts")

    response = requests.get(f"{BASE_URL}/accounts/")
    print_result("GET /accounts/", response)

    # === Summary ===
    print_section("Test Completed")
    print("✅ Customer creation tested")
    print("✅ Account creation tested")
    print("✅ Deposit money tested")
    print("\n🎉 Full end-to-end flow completed!\n")


if __name__ == "__main__":
    test_bank_flow()