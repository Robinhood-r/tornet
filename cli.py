import argparse

from scanner.url_scanner import url_scan
from scanner.email_scanner import email_scan

parser = argparse.ArgumentParser(description="Tornet - URL and Email phishing scanner")
parser.add_argument("--url", help="URL to scan")
parser.add_argument("--email", help="Email to scan")
args = parser.parse_args()

if args.url:
    results = url_scan(args.url)
    print(results)

if args.email:
    results = email_scan(args.email)
    print(results)