import re

def assess_password(password: str) -> dict:
    """
    Assess password strength and return a report.

    Criteria:
      - Length ≥ 8
      - Contains lowercase
      - Contains uppercase
      - Contains digit
      - Contains special character
    """
    report = {
        'length': len(password),
        'has_lower': bool(re.search(r'[a-z]', password)),
        'has_upper': bool(re.search(r'[A-Z]', password)),
        'has_digit': bool(re.search(r'\d', password)),
        'has_special': bool(re.search(r'[^A-Za-z0-9]', password)),
    }

    # Count how many criteria are met (excluding length)
    criteria_met = sum([
        report['has_lower'],
        report['has_upper'],
        report['has_digit'],
        report['has_special'],
    ])

    # Determine strength
    if report['length'] >= 12 and criteria_met == 4:
        strength = 'Very Strong'
    elif report['length'] >= 10 and criteria_met >= 3:
        strength = 'Strong'
    elif report['length'] >= 8 and criteria_met >= 2:
        strength = 'Moderate'
    else:
        strength = 'Weak'

    report['strength'] = strength
    return report

def print_feedback(report: dict):
    """Print human‑friendly feedback based on the assessment report."""
    print(f"\nPassword Strength: {report['strength']}")
    print(f"- Length: {report['length']} characters", 
          "(OK)" if report['length'] >= 8 else "(too short)")
    print(f"- Lowercase letters: {'✓' if report['has_lower'] else '✗'}")
    print(f"- Uppercase letters: {'✓' if report['has_upper'] else '✗'}")
    print(f"- Digits: {'✓' if report['has_digit'] else '✗'}")
    print(f"- Special chars: {'✓' if report['has_special'] else '✗'}")

    # Suggestions
    suggestions = []
    if report['length'] < 8:
        suggestions.append("Make it at least 8 characters long.")
    if not report['has_lower']:
        suggestions.append("Add lowercase letters (a–z).")
    if not report['has_upper']:
        suggestions.append("Add uppercase letters (A–Z).")
    if not report['has_digit']:
        suggestions.append("Include digits (0–9).")
    if not report['has_special']:
        suggestions.append("Include special characters (e.g. !@#$%).")

    if suggestions:
        print("\nSuggestions to improve your password:")
        for s in suggestions:
            print(f" • {s}")
    else:
        print("\nYour password meets all recommended criteria!")

def main():
    print("=== Password Complexity Checker ===")
    pwd = input("Enter a password to assess: ")
    report = assess_password(pwd)
    print_feedback(report)

if __name__ == "__main__":
    main()
