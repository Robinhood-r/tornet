
# A list of suspicious TLDs
suspicious_tlds = [".tk", ".ml", ".xyz", ".ga", ".cf"]

# This dictionary maps fake characters to real characters to check for the use of lookalike characters in the domain
lookalikes = {
    "1": "l",
    "0": "o",
    "3": "e",
    "rn": "m"
}

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
    
    # Checking for lookalikes in domain
    for fake, real in lookalikes.items():
            if fake in domain:
                findings.append(f"MEDIUM: '{fake}' may be impersonating '{real}'")
                break


    return findings



if __name__ == "__main__":
    print(email_scan("support@paypa1.com"))