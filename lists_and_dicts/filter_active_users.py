"""
Problem:
Filter a list of user dictonaries to return active users.

Approach:
Think of it like checking IDs at a VIP event:

1. Look at each person(user) in the line (list)
2. Check their badge: Does it say "active = True"?
3. If yes -> let them in (keep in result)
4. If no -> sorry, not today (skip them)
5. Continue until everyone is checked"""

users = [
    {"name": "A", "active": True},
    {"name": "B", "active": False},
    {"name": "C", "active": True},
]

def get_active_users(users):
    return [user for user in users if user["active"]]


if __name__=="__main__":
    print(get_active_users(users))