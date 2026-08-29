#!/usr/bin/env python3
"""Fetch users from JSONPlaceholder and write name, email, and company to a CSV file."""
import csv
import sys

import requests

API_URL = "https://jsonplaceholder.typicode.com/users"
OUTPUT_FILE = "users.csv"


def fetch_users():
    response = requests.get(API_URL, timeout=10)
    response.raise_for_status()
    return response.json()


def write_csv(users, output_path):
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "email", "company"])
        for user in users:
            writer.writerow([
                user.get("name", ""),
                user.get("email", ""),
                user.get("company", {}).get("name", ""),
            ])


def main():
    users = fetch_users()
    write_csv(users, OUTPUT_FILE)
    print(f"Wrote {len(users)} users to {OUTPUT_FILE}")


if __name__ == "__main__":
    try:
        main()
    except requests.RequestException as e:
        print(f"Failed to fetch users: {e}", file=sys.stderr)
        sys.exit(1)
