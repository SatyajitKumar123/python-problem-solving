# Directory Tree Printer
"""
Problem: You want to show the structure of your project in a README file.
"""

import os

def print_tree(start_path, indent=""):
    """Prints a visual tree of files and folders."""
    items = os.listdir(start_path)
    items.sort()
    
    for i, item in enumerate(items):
        path = os.path.join(start_path, item)
        is_last = (i == len(items) - 1)
        marker = "└── " if is_last else "├── "
        
        print(f"{indent}{marker}{item}")

        if os.path.isdir(path):
            new_indent = indent + ("    " if is_last else "│   ")
            print_tree(path, new_indent)
            
if __name__=="__main__":
    print_tree()