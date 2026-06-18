#!/usr/bin/env python3
"""
Simple Endpoint Tester for the Educational Bank Project
Run this while your server is running: uvicorn app.main:app --reload
"""

import requests
import json

BASE_URL = "http://127.0.0.1:8000"

def print_result(name, response):
    print(f"\n{'='*60}")
    print(f"Testing: {name}")
    print(f"Status Code: {response.status_code}")
    try:
        print("Response:", json.dumps(response.json(), indent=2))
    except:
        print("Response:", response.text)
    print("✅ SUCCESS" if response.status_code in [200, 201] else "❌ FAILED")


def test_all():
    print("🚀 Testing all endpoints...\n")

    # 1. Root
    print_result("GET /", requests.get(f"{BASE_URL}/"))

    # 2. Health
    print_result("GET /health", requests.get(f"{BASE_URL}/health"))

    # 3. Signup
    signup_data = {
        "first_name": "Hamza",
        "last_name": "Mehmood",
        "email": "hamza.test@example.com",
        "phone_number": "555-987-6543",
        "ssn": "987-65-4321",
        "date_of_birth": "2013-08-20",
        "address": "456 Test Street, Houston, TX",
        "password": "TestPass123"
    }
    print_result("POST /auth/signup", requests.post(f"{BASE_URL}/auth/signup", json=signup_data))

    # 4. Create Account
    print_result("POST /accounts/", requests.post(f"{BASE_URL}/accounts/", json={"account_type": "checking"}))

    # 5. List Accounts
    print_result("GET /accounts/", requests.get(f"{BASE_URL}/accounts/"))

    print("\n🎉 Testing complete!")


if __name__ == "__main__":
    test_all()
