# Tornet

A phishing scanner for URLs and emails.

## What it does
**Tornet** is comprised of 2 main components: Email scanner and URL scanner.

The **email scanner** checks the entire email for suspicious domains, keywords, and anything that could be a potential phishing email address. It categorizes them into LOW, MEDIUM, and HIGH alert based on the email

The **URL scanner** checks the entire URL for: use of HTTP, use of shorteners, suspicious keywords, IP addresses, and lookalike characters . It categorizes them into LOW, MEDIUM, and HIGH alert based on the words used in the URL

## How to run
python3 scanner/url_scanner.py
