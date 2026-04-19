import re

def transform_text(text):
    # Days of the week (always capitalized)
    days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]

    # Lowercase
    lower = text.lower()

    # Uppercase
    upper = text.upper()

    # Sentence case (first letter uppercase, rest lowercase)
    sentence = text.capitalize()

    # Title case (capitalize first letter of each word, rest lowercase)
    title = text.title()

    # Special rule: capitalize days of the week
    def capitalize_days(s):
        for day in days:
            s = re.sub(day, day.capitalize(), s, flags=re.IGNORECASE)
        return s

    lower = capitalize_days(lower)
    upper = capitalize_days(upper)
    sentence = capitalize_days(sentence)
    title = capitalize_days(title)

    return {
        "lowercase": lower,
        "uppercase": upper,
        "sentence_case": sentence,
        "title_case": title
    }

# Example strings
texts = [
    "tomorrow is tuesday.",
    "TOMORROW is tuesday?",
    "then What? wedNesday?"
]

for t in texts:
    print(f"Original: {t}")
    results = transform_text(t)
    for k,v in results.items():
        print(f"{k}: {v}")
    print()


