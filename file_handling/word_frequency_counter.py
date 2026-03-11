# Word Frequency Counter (Integration)
"""
Concept: File I/O, Dictionaries, Sorting, String Manipulation.
Goal: Read a text file and count how often every word appears. This combines almost everything learned above.
"""

import string

def count_words(filename):
    word_count = {}
    
    try:
        with open(filename, "r", encoding="utf-8") as f:
            text = f.read().lower()
            
            # Remove punctuation
            text = text.translate(str.maketrans('', '', string.punctuation))

            words = text.split()
            
            for word in words:
                word_count[word] = word_count.get(word, 0) + 1
                
        sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

        print(f"\nTop 10 Words in {filename}:")
        for word, count in sorted_words[:10]:
            print(f"{word}: {count}")

    except FileNotFoundError:
        print(f"File '{filename}' not found.")

if __name__=="__main__":
    test_file = "sample.txt"
    with open(test_file, "w") as f:
        f.write("Hello world. Hello Python. Python is great. World is big.")
    
    count_words(test_file)