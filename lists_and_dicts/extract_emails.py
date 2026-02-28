"""
Problem:
Extract all email address from a list of user dictionaries.

Approach:
Think of it like collecting email addresses from a contact list:

1. Look at each user's information card (dictionary)
2. Check if they have provided an email address
3. If yes → take their email and add to our collection
4. If no → skip them and move to next user
5. Continue until all users are checked
"""

def extract_emails(data):
    return [u['email'] for u in data if 'email' in u]

if __name__=="__main__":
    
    users = [
        {"name": "A", "email": "a@mail.com"},
        {"name": "B"},
        {"name": "C", "email": "c@mail.com"},
    ]
    print(extract_emails(users))