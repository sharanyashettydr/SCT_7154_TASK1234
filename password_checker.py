import re

def check_password_strength(password):
    strength = 0
    criteria = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "digit": bool(re.search(r"[0-9]", password)),
        "special_char": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    }

    print("\n🔍 Password Check:")
    for key, value in criteria.items():
        if value:
            strength += 1
            print(f"✅ Contains {key.replace('_', ' ')}")
        else:
            print(f"❌ Missing {key.replace('_', ' ')}")

    # Final result
    print("\n🔒 Password Strength:")
    if strength == 5:
        print("💪 Very Strong")
    elif strength >= 4:
        print("👍 Strong")
    elif strength >= 3:
        print("🟡 Medium")
    elif strength >= 2:
        print("⚠️ Weak")
    else:
        print("❌ Very Weak")

def main():
    print("=== Password Strength Checker ===")
    while True:
        pwd = input("\nEnter your password: ")
        check_password_strength(pwd)

        choice = input("\nWould you like to test another password? (y/n): ").lower()
        if choice != 'y':
            print("👋 Thank you for using the password checker!")
            break

if __name__ == "__main__":
    main()
