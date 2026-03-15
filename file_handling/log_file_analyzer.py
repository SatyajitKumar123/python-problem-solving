# Log File Error Analyzer
"""
Real-World Use: DevOps engineers scan server logs to count critical errors.
"""

def analyze_logs(file_path):
    """
    Counts occurences of 'ERROR' and 'WARNING' in a log file.
    """
    counts = {"ERROR": 0, "WARNING": 0}

    try:
        with open(file_path, 'r') as f:
            for line in f:
                if "ERROR" in line:
                    counts["ERROR"] += 1
                elif "WARNING" in line:
                    counts["WARNING"] += 1
        return counts
    except FileNotFoundError:
        return None
    
def run_tests():
    test_file = "test.log"
    with open(test_file, 'w') as f:
        f.write("INFO: Start\n")
        f.write("ERROR: Disk full\n")
        f.write("WARNING: Low memory\n")
        f.write("ERROR: Connection lost\n")
    
    result = analyze_logs(test_file)
    assert result["ERROR"] == 2
    assert result["WARNING"] == 1
    
    assert analyze_logs("missing.log") is None
    
    import os
    os.remove(test_file)
    print("All log_file_analyzer tests passed.")

if __name__=="__main__":
    run_tests()