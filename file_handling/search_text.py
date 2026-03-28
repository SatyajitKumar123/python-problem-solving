# Search Text in File (Mini Grep)
"""
Problem: You need to find which line contains an error message in a huge log file.
"""

def search_in_file(file_path, keyword):
    """Returns lines containing the keyword."""
    matches = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                if keyword in line:
                    matches.append(line.strip())
    except FileNotFoundError:
        return []
    return matches

if __name__=="__main__":
    search_in_file()