# JSON Configuration Loader
"""
Real-World Use: Applications often store settings (database URLs, API keys) in JSON config files.
"""

import json
import os

def load_config(file_path, defaults=None):
    if defaults is None:
        defaults = {}
        
    if not os.path.exists(file_path):
        print(f"Config file '{file_path}' not found. Using defaults.")
        return defaults
    
    try:
        with open(file_path, 'r') as f:
            config = json.load(f)
            # Merge defaults with loaded config (loaded takes precedence)
            return {**defaults, **config}
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        return defaults
    
def run_tests():
    # Test 1: Missing file returns defaults
    assert load_config("nonexistent.json", {"debug": True}) == {"debug": True}
    
    # Test 2: Create a temp file and load it
    test_file = "test_config.json"
    with open(test_file, 'w') as f:
        json.dump({"theme": "dark"}, f)
    
    result = load_config(test_file, {"theme": "light", "debug": False})
    assert result["theme"] == "dark"  # File value overrides default
    assert result["debug"] == False   # Default value persists
    
    os.remove(test_file)
    print("All json_config_loader tests passed.")
    
if __name__=="__main__":
    run_tests()