# Find Large Files
"""
Problem: Your computer is slow. You need to find files larger than 100MB to delete them.
"""

import os

def find_large_files(folder_path, size_mb):
    """Returns a list of files larger than X MB."""
    large_files = []
    size_bytes = size_mb * 1024 * 1024
    
    for root, _, files in os.walk(folder_path):
        for file in files:
            path = os.path.join(root, file)
            try:
                if os.path.getsize(path) > size_bytes:
                    large_files.append(path)
            except FileNotFoundError:
                continue
    return large_files

    

if __name__=="__main__":
    find_large_files()