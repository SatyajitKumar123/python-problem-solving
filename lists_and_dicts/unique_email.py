"""
Problem:
Remove duplicate emails from a list, keeping only unique ones.

Approach:
Think of it like filtering party invitations:

1. You have a list of email addresses, but some people were invited twice
2. Sets are like magical bags that can only hold unique items
3. Convert the list to a set - duplicates automatically disappear!
4. Convert back to a list for the final result
"""

def unique_emails(emails):
    return list(set(emails))


if __name__=="__main__":
    
    test_lists = [
        ["a@mail.com", "b@mail.com", "a@mail.com"],           
        ["x@mail.com", "y@mail.com", "z@mail.com"],           
        ["same@mail.com", "same@mail.com", "same@mail.com"],  
        [],                                                     
        ["a@mail.com", "a@mail.com", "b@mail.com", "b@mail.com"],  
        ["", "test@mail.com", ""],                              
    ]
    
    for i, emails in enumerate(test_lists, 1):
        unique = unique_emails(emails)
        
        print(f"Test {i}")
        print(f"  Original ({len(emails)}): {emails}")
        print(f"  Unique ({len(unique)}):   {unique}")