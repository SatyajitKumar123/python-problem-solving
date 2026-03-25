# User Data Normalizer
"""
Real-World Use: Cleaning user input before saving to a database (trimming spaces, lowercasing emails).
"""

def normalize_users(users):
    """
    Cleans user strips whitespace and lowercases emails.
    """
    cleaned = []
    for user in users:
        clean_user = {
            "name": user.get("name", "").strip().title(),
            "email": user.get("email", "").strip().lower()
        }
        cleaned.append(clean_user)
    return cleaned


if __name__=="__main__":
    normalize_users()