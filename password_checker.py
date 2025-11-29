import re

print("\n" + "="*60)
print("        PASSWORD STRENGTH ANALYZER")
print("        by Christian Sesay – Sierra Leone")
print("="*60 + "\n")

# ← THIS IS WHERE YOU TYPE (you will see the letters)
password = input("Enter your password here → ")

print("\n" + "—"*50)
print("ANALYZING YOUR PASSWORD...")
print("—"*50)

score = 0
tips = []

# Length
if len(password) >= 12:
    score += 25
    print("Length (12+ chars)      → Excellent (+25)")
elif len(password) >= 8:
    score += 15
    print("Length (8–11 chars)     → Good (+15)")
else:
    tips.append("Make it 12+ characters long")
    print("Length                  → Too short")

# Lowercase
if re.search(r"[a-z]", password):
    score += 15
    print("Lowercase letters       → Found (+15)")
else:
    tips.append("Add lowercase letters")

# Uppercase
if re.search(r"[A-Z]", password):
    score += 20
    print("Uppercase letters       → Found (+20)")
else:
    tips.append("Add uppercase letters")

# Numbers
if re.search(r"[0-9]", password):
    score += 20
    print("Numbers                 → Found (+20)")
else:
    tips.append("Add numbers")

# Symbols
if re.search(r"[^a-zA-Z0-9]", password):
    score += 20
    print("Symbols (!@#$ etc)      → Found (+20)")
else:
    tips.append("Add symbols (!@#$%^&*)")

# Bad patterns
bad = ["123", "abc", "password", "qwerty", "letmein"]
if any(word in password.lower() for word in bad):
    score -= 20
    tips.append("Avoid common sequences")
    print("Common pattern found    → –20 points")

# Final result
print("\n" + "="*60)
print(f"FINAL SCORE: {score}/100")

if score >= 90:
    print("RATING → EXTREMELY STRONG")
elif score >= 75:
    print("RATING → STRONG")
elif score >= 60:
    print("RATING → MEDIUM")
else:
    print("RATING → WEAK")

if tips:
    print("\nTo make it stronger:")
    for tip in tips:
        print("   • " + tip)
else:
    print("\nPERFECT PASSWORD! You're safe.")

print("\nThanks for using my tool!\n")