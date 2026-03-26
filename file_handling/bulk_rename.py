# Bulk File Renamer (Add Prefix)
"""
Problem: You have 50 images named img_01.jpg, img_02.jpg and want them to be vacation_img_01.jpg.
"""

import os

def add_prefix_to_files(folder_path, prefix):
    """Adds a prefix to all files in a specific folder."""
    if not os.path.exists(folder_path):
        return False
    
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            new_name = f"{prefix}{filename}"
            os.rename(
                os.path.join(folder_path, filename),
                os.path.join(folder_path, new_name)
            )
    return True

if __name__=="__main__":
    add_prefix_to_files()