import argparse

from scanner.url_scanner import url_scan
from scanner.email_scanner import email_scan

parser = argparse.ArgumentParser(description="Tornet - URL and Email phishing scanner")
parser.add_argument("--url", help="URL to scan")
parser.add_argument("--email", help="Email to scan")
args = parser.parse_args()


# Checking the given URL
if args.url:
    print(f"\nTornet - Scanning URL: {args.url}")
    print("─" * 40)
    results = url_scan(args.url)
    for i in results:
        print(f"{i}")

# Checking the given email
if args.email:
    print(f"\nTornet - Scanning Email: {args.email}")
    print("─" * 40)
    results = email_scan(args.email)
    for i in results:
        print(f"{i}")