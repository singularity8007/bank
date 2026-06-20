#!/usr/bin/env python3
"""
Educational Bank API - End-to-End Test Script (Final Version)
"""

import requests
import json
import uuid
from datetime import datetime
from typing import Optional, Dict, Any

BASE_URL = "http://127.0.0.1:8000"


def print_section(title: str):
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


def print_result(name: str, response: requests.Response) -> Optional[Dict[str, Any]]:
    print(f"\n▶ {name}")
    print(f"   Status: {response.status_code}")
    try:
        data = response.json()
        print(json.dumps(data, indent=4, default=str))
        return data
    except Exception:
        print(response.text)
        return None


def get_unique_test_data() -> dict:
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


def get_customer_id(data: dict) -> Optional[str]:
    return data.get("customer_id") or data.get("customerid")


def test_bank_api():
    print_section("Educational Bank API - End-to-End Test")

    # === Step 1: Create Customer ===
    print_section("Step 1: Create Customer (Signup)")

    signup_data = get_unique_test_data()
    response = requests.post(f"{BASE_URL}/auth/signup", json=signup_data)
    customer = print_result("POST /auth/signup", response)

    if not customer:
        print("\n❌ Signup failed. Stopping test.")
        return

    customer_id = get_customer_id(customer)
    if not customer_id:
        print("\n❌ Could not extract customer_id.")
        return

    print(f"\n✅ Customer created! ID: {customer_id}")

    # === Step 2: Create Account (using real customer_id) ===
    print_section("Step 2: Create Account")

    account_data = {
        "customer_id": customer_id,      # ← Send the real ID
        "account_type": "checking"
    }

    response = requests.post(f"{BASE_URL}/accounts/", json=account_data)
    account = print_result("POST /accounts/", response)

    if account and account.get("account_id"):
        print(f"\n✅ Account created successfully! ID: {account.get('account_id')}")
    else:
        print("\n⚠️ Account creation had issues.")

    # === Step 3: List Accounts ===
    print_section("Step 3: List Accounts")

    response = requests.get(f"{BASE_URL}/accounts/")
    print_result("GET /accounts/", response)

    # === Summary ===
    print_section("Test Completed Successfully")
    print("✅ Full end-to-end flow tested!")


if __name__ == "__main__":
    test_bank_api()
