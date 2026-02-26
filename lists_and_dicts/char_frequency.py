""" 
Problem:
count the frequency of each character in a string.

Approach:
1. Start with an empty tally sheet (dictionary)
2. Look at each character one by one
3. Ask: "Have I seen this character before?"
   - If YES → add 1 to their count
   - If NO → add them to the sheet with count 1
4. Continue until all characters are counted

The `.get(ch, 0)` trick:
- `counts.get(ch, 0)` means: "Get the current count for ch, or 0 if it doesn't exist"
- Then we add 1 and store it back
- This handles both new and existing characters in one line!

"""

def char_count(text):
    counts = {}
    for ch in text:
        counts[ch] = counts.get(ch, 0) + 1
    return counts


if __name__=="__main__":
    test_strings = [
        "backend",           
        "hello",              
        "mississippi",       
        "",                  
        "a",                 
        "aaa",               
        "Hello World!",       
        "112233",             
    ]
    
    for text in test_strings:
        result = char_count(text)
        print(f"Text: '{text}'")
        print(f"Counts: {result}")