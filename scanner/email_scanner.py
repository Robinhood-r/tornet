
# A list of suspicious TLDs
suspicious_tlds = [".tk", ".ml", ".xyz", ".ga", ".cf"]

# mail scanner function for emails
def email_scan(email):

    # A list for displaying the results of the scan
    findings = []


    # Spliting the email into 2 parts to determin the domain and the domain and the local part
    parts = email.split("@")
    domain = parts[1]

    # Checking  the email for suspicious tld
    for i in suspicious_tlds:

        if i in domain:
            findings.append("HIGH: Email is from a suspicious domain extension - treat with caution")
            break
    
    return findings




if __name__ == "__main__":
    print(email_scan("security@paypal-support.tk"))