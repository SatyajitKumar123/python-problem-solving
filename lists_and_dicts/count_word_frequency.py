"""
Problem:
Count how many times each word appears in a sentence.

Approach:
1. Clean the text - Convert to lowercase and remove punctuation so 'The' and 'the' count as same word
2. Split into words - Break the cleaned text into a list of individual words
3. Count frequencies - Loop through each word and use a dictionary to track counts
    * If word exists in dictionary - increment its value by 1
    * If word doesn't exist - add it with value 1
"""

def word_frequency(text):
    words = text.lower().replace('.', '').replace(',', '').split()
    freq = {}
    
    for word in words:
        freq[word] = freq.get(word, 0) + 1
        
    return freq

if __name__=="__main__":
    text = "The cat chased the mouse, but the mouse was too fast for the cat and the cat got lazy." 
    print(f"word frequency: \n{word_frequency(text)}")