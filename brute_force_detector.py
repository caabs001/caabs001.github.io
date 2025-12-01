import re
from collections import Counter


print("=" * 60)
print("BRUTE FORCE DETECTOR")
print("by Christian Sesay - Sierra Leone")
print("=" * 60)
log_file = "auth.log"
pattern = re.compile(r'from (\d+\.\d+\.\d+\.\d+).*')
attacks = []
print("\nScanning log file...")
try:
    with open(log_file, 'r', encoding="utf-8", errors="ignore") as file:
        for line in file:
            match = pattern.search(line)
            if match:
                ip = match.group(1)
                attacks.append(ip)
                print(f"Found attack from → {ip}")
except FileNotFoundError:
    print("Log file not found creating a fake test log for you...")
fake_log = [
    "Oct 10 10:00:01 server sshd[1234]: Failed password for invalid user admin from 192.168.1.100",
    "Oct 10 10:00:05 server sshd[1235]: Failed password for root from 192.168.1.100",
    "Oct 10 10:00:09 server sshd[1236]: Failed password for root from 45.79.123.45",
    "Oct 10 10:00:12 server sshd[1237]: Failed password for admin from 192.168.1.100",
    "Oct 10 10:00:15 server sshd[1238]: Failed password for root from 45.79.123.45",
    "Oct 10 10:00:18 server sshd[1239]: Failed password for root from 45.79.123.45",
    "Oct 10 10:00:21 server sshd[1240]: Failed password for root from 45.79.123.45",
]
print("\nHere are the exact fake logs:")
for i, line in enumerate(fake_log, 1):
    print(line)
for line in fake_log:
    match = pattern.search(line)
    if match:
        ip = match.group(1)
        attacks.append(ip)
        print(f"Found attack from → {ip}")

print("\n"+"="*60)
print("BRUTE FORCE DETECTION REPORT")
print("="*60)

counter = Counter(attacks)

for ip, count in counter.most_common():
    if count >= 3:
        print("ALERT → {ip} tried {count} times ← POSSIBLE BRUTE FORCE")
    else:
        print(f"{ip} → {count} failed attempts")

print("\nScan complete.")


