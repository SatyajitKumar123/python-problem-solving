# CSV User Exporter
""" 
Real-World Use: Exporting a list of users to a CSV file for Excel/Spreadsheets.
"""

import csv


def export_users_to_csv(users, filename):
    """
    Take a list of user dicts and writes them to a CSV file.
    """
    if not users:
        return False
    
    keys = users[0].keys()
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(users)
    return True


if __name__ == "__main__":
    export_users_to_csv()