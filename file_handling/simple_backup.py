# Simple Backup Script
"""
Problem: You are about to edit a config file. You want a safe copy first.
"""

import shutil
import os
from datetime import datetime

def create_backup(file_path):
    """Creates a copy of the file with a timestamp."""
    if not os.path.exists(file_path):
        return False
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base, ext = os.path.splitext(file_path)
    backup_name = f"{base}_backup_{timestamp}{ext}"

    shutil.copy2(file_path, backup_name)
    return backup_name


if __name__=="__main__":
    create_backup()