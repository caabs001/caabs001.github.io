import re
#import requests
#from urllib.parse import urlparse

print("=" * 70)
print("   PHISHING URL & EMAIL SCANNER")
print("   by Christian Sesay - Sierra Leone ")
print("=" * 70)

print("\nWhat do you want to check?")
print("1 → Suspicious URL")
print("2 → Suspicious email (paste full text)")
choice = input("\nEnter 1 or 2 → ")
if choice == "1":
    url = input("\nPaste the suspicious URL here → ").strip()
    print("\nScanning URL...")

elif choice == "2":
    url = input("\nPaste the full email (including headers) below, then press Enter twice:")
    email_lines = []
    while True:
        line = input()
        if line == "":
            break
            email_lines.append(line)
        email_text = "\n".join(email_lines)
        print("\nScanning email...")
else:
    print("Invalid choice - run again and pick 1 or 2")
def check_url(url):
    score = 0
    warnings = []

    if any(short in url.lower() for short in ["bit.ly", "tinyurl", "goo.gl", "t.co", "ow.ly"]):
        score += 40
        warnings.append("Shortened link detected (often used in phishing)")

    suspicious_tlds = [".tk", ".ml", ".ga", ".cf", ".gq", ".xyz", ".top", ".club"]
    domain = url.lower().split("://")[-1].split("/")[0]
    for tld in suspicious_tlds:
        if tld in domain:
            score += 30
        warnings.append(f"Suspicious domain ending {tld}")
        break
    if url.startswith("http://"):
        score += 30
        warnings.append("Not using HTTPS")
        print("\n"+"-" * 50)
        if score >= 70:
            print("VERDICT → HIGHLY DANGEROUS (Phishing likely)")
        elif score >= 40:
            print("VERDICT → SUSPICIOUS (Be very careful)")
        else:
            print("VERDICT → Probably safe")
        print("-" * 50)
    if warnings:
        print("Reasons: ")
        for w in warnings:
            print(f" •{w}")
    else:
        print(" • No red flags found")
def check_mail(text):
    score = 0
    warnings = []

    lines = text.lower()
    if any(word in lines for word in ["urgent", "immediately", "account suspended", "verify now", "payment failed"]):
        score += 35
        warnings.append("Urgency / threat words detected")

    if "click here" in lines or "login" in lines and "link" in lines:
        score += 30
        warnings.append("Suspicious call-to-action")

    if re.search(r"from:.*(gmail|yahoo|hotmail) *subject:.*(security|verify|payment)", lines):
        score += 25
        warnings.append("Fake bank/billing email pattern")

    print("\n"+"-" * 50)
    if score >= 60:
        print("VERDICT → PHISHING EMAIL (Delete immediately)")
    elif score >= 30:
        print("VERDICT → HIGHLY SUSPICIOUS")
    else:
        print("VERDICT → Probably legitimate")
    print("-" * 50)
    if warnings:
        print("Red flags found:")
        for w in warnings:
            print(f" •{w}")
    else:
        print(" • No obvious phishing signs")

if choice == "1":
    if 'url' in locals():
        check_url(url)
    else:
        print("No URL entered")
elif choice == "2":
    if 'email_text' in locals():
        check_mail(email_text)
    else:
        print("No email entered")







