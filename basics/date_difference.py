# Date Difference Calculator
"""
Real-World Use: Calculating days until a deadline, user age, subscription duration.
"""

from datetime import datetime

def days_between(date_str1, date_str2):
    """
    Calculates days between two 'YYYY-MM-DD' strings.
    """

    fmt = "%Y-%m-%d"
    d1 = datetime.strptime(date_str1, fmt)
    d2 = datetime.strptime(date_str2, fmt)
    
    delta = d2 - d1
    return abs(delta.days)


if __name__=="__main__":
    days_between()