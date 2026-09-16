import re

def check_password_strength(password):
    """
    Checks a password against several strength criteria and returns
    whether it's Strong or Weak, along with the reasons.
    """
    min_length = 8
    issues = []
    
    if len(password) < min_length:
        issues.append(f"Must be at least {min_length} characters long")
    
    if not re.search(r"[0-9]", password):
        issues.append("Must contain at least 1 number")
    
    if not re.search(r"[A-Z]", password):
        issues.append("Must contain at least 1 uppercase letter")
    
    if not re.search(r"[a-z]", password):
        issues.append("Must contain at least 1 lowercase letter")
    
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>_\-+=~`\[\];']", password):
        issues.append("Must contain at least 1 special character")
    
    is_strong = len(issues) == 0
    return is_strong, issues

def main():
    print("=" * 45)
    print("       PASSWORD STRENGTH CHECKER")
    print("=" * 45)
    
    password = input("Enter a password to check: ")
    
    is_strong, issues = check_password_strength(password)
    
    print()
    if is_strong:
        print("✅ Result: STRONG password!")
    else:
        print("❌ Result: WEAK password")
        print("\nIssues found:")
        for issue in issues:
            print(f"  - {issue}")
    print()

if __name__ == "__main__":
    main()