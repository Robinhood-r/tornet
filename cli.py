import argparse

from scanner.url_scanner import url_scan
from scanner.email_scanner import email_scan

# Creating the scanner's name as a banner
def print_banner():
    print(f"""
{RED}
 ████████╗ ██████╗ ██████╗ ███╗   ██╗███████╗████████╗
    ██╔══╝██╔═══██╗██╔══██╗████╗  ██║██╔════╝╚══██╔══╝
    ██║   ██║   ██║██████╔╝██╔██╗ ██║█████╗     ██║   
    ██║   ██║   ██║██╔══██╗██║╚██╗██║██╔══╝     ██║   
    ██║   ╚██████╔╝██║  ██║██║ ╚████║███████╗   ██║   
    ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   
{RESET}
{YELLOW}Phishing Scanner | by Danial R{RESET}
    """)

# Defining different colors for different alerts
RED = '\033[91m'
YELLOW = '\033[93m'
GREEN = '\033[92m'
RESET = '\033[0m'

parser = argparse.ArgumentParser(description="Tornet - URL and Email phishing scanner")
parser.add_argument("--url", help="URL to scan")
parser.add_argument("--email", help="Email to scan")
args = parser.parse_args()

# Calling the print function for TORNET
print_banner()

# Checking the given URL
if args.url:
    print(f"\nTornet - Scanning URL: {args.url}")
    print("─" * 60)
    print()
    results = url_scan(args.url)

    for i in results:
        if i.startswith("HIGH"):
            print(f"{RED}{i}{RESET}")
        elif i.startswith("MEDIUM"):
            print(f"{YELLOW}{i}{RESET}")
        elif i.startswith("LOW"):
            print(f"{GREEN}{i}{RESET}")
        print()


# Checking the given email
if args.email:
    print(f"\nTornet - Scanning Email: {args.email}")
    print("─" * 60)
    print()
    results = email_scan(args.email)

    for i in results:
        if i.startswith("HIGH"):
            print(f"{RED}{i}{RESET}")
        elif i.startswith("MEDIUM"):
            print(f"{YELLOW}{i}{RESET}")
        elif i.startswith("LOW"):
            print(f"{GREEN}{i}{RESET}")
        print()


