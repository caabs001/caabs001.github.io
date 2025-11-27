#Burte-Force Attack Detector 
#Author: Christian Sesay 
#Date: November 2025

import re 
from collections import Counter 

log_file = "auth.log" 

failed_pattern = re compile(r"Failed password for.*from(\S+)")

ip_list = []

with open(log_file, "r" ,encoding="latin-1") as f:
 for line in f:
  match = failed_pattern search(line)
  if match:
   ip_list append(match group(1))

#Count attempts per IP
attempts = Counter(ip_list)

print("===BRUTE-FORCE ATTACK DETECTION REPORT===\n")
print(f"Author: Christian Sesay\n")

for ip, count in attempts.most_common():
 if count > 5
  prnt(f"ALERT: {ip} {count} failed login attempts (possible brute-force)")
else:
 print(f"{ip} {count} failed attempts")

print("\nScan complete.")