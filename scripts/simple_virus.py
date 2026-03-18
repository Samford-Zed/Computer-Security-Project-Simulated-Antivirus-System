"""
EDUCATIONAL PURPOSE ONLY - Simple File Deletion "Virus"
This script demonstrates basic malware behavior for learning purposes.
DO NOT use this maliciously.
"""

import os
import sys

def delete_target_file(target_path):
    """
    Attempts to delete a target file.
    This simulates malicious file deletion behavior.
    """
    try:
        if os.path.exists(target_path):
            os.remove(target_path)
            print(f"[VIRUS SIMULATION] File deleted: {target_path}")
            return True
        else:
            print(f"[VIRUS SIMULATION] File not found: {target_path}")
            return False
    except PermissionError:
        print(f"[VIRUS SIMULATION] Permission denied: {target_path}")
        return False
    except Exception as e:
        print(f"[VIRUS SIMULATION] Error: {e}")
        return False

def main():
    """
    Main function that simulates virus behavior.
    In a real scenario, this might be more sophisticated.
    """
    # Default target file (for demonstration)
    # In a real malicious scenario, this might target system files
    target_file = "test_file.txt"
    
    # Check if a target file is provided as argument
    if len(sys.argv) > 1:
        target_file = sys.argv[1]
    
    print("[VIRUS SIMULATION] Starting file deletion simulation...")
    print(f"[VIRUS SIMULATION] Target: {target_file}")
    
    # Simulate the deletion
    delete_target_file(target_file)
    
    print("[VIRUS SIMULATION] Simulation complete.")

if __name__ == "__main__":
    main()

