"""
EDUCATIONAL PURPOSE - Simple Antivirus Scanner
This script detects and handles the simple_virus.py script.
"""

import os
import sys
import hashlib
import re

class SimpleAntivirus:
    """
    A simple antivirus scanner that detects malicious patterns
    and the educational virus script.
    """
    
    def __init__(self):
        self.virus_signatures = []
        self.suspicious_patterns = [
            r'os\.remove\s*\(',
            r'os\.unlink\s*\(',
            r'shutil\.rmtree\s*\(',
            r'__import__\s*\(',
            r'eval\s*\(',
            r'exec\s*\(',
        ]
        self.scan_results = []
    
    def calculate_file_hash(self, file_path):
        """Calculate SHA-256 hash of a file."""
        try:
            hash_sha256 = hashlib.sha256()
            with open(file_path, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_sha256.update(chunk)
            return hash_sha256.hexdigest()
        except Exception as e:
            print(f"Error calculating hash: {e}")
            return None
    
    def scan_file(self, file_path):
        """
        Scan a file for malicious patterns and known virus signatures.
        """
        if not os.path.exists(file_path):
            return {"status": "error", "message": "File not found"}
        
        if not file_path.endswith('.py'):
            return {"status": "skipped", "message": "Not a Python file"}
        
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            file_hash = self.calculate_file_hash(file_path)
            threats_found = []
            suspicious_lines = []
            
            # Check for suspicious patterns
            for pattern in self.suspicious_patterns:
                matches = re.finditer(pattern, content, re.IGNORECASE)
                for match in matches:
                    line_num = content[:match.start()].count('\n') + 1
                    suspicious_lines.append({
                        "line": line_num,
                        "pattern": pattern,
                        "match": match.group()
                    })
            
            # Check for known virus file
            if 'simple_virus.py' in file_path or 'delete_target_file' in content:
                threats_found.append("Known educational virus pattern detected")
            
            # Check for file deletion operations
            if 'os.remove' in content or 'os.unlink' in content:
                if 'delete_target_file' in content or 'EDUCATIONAL' not in content:
                    threats_found.append("File deletion operation detected")
            
            result = {
                "file": file_path,
                "hash": file_hash,
                "threats": threats_found,
                "suspicious_lines": suspicious_lines,
                "status": "infected" if threats_found else "clean"
            }
            
            return result
            
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    def scan_directory(self, directory_path):
        """Scan all Python files in a directory."""
        results = []
        
        if not os.path.exists(directory_path):
            print(f"Error: Directory not found: {directory_path}")
            return results
        
        print(f"Scanning directory: {directory_path}")
        print("-" * 60)
        
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    result = self.scan_file(file_path)
                    results.append(result)
                    self.display_result(result)
        
        return results
    
    def display_result(self, result):
        """Display scan result in a readable format."""
        if result.get("status") == "error":
            print(f"❌ ERROR: {result.get('file', 'Unknown')} - {result.get('message')}")
            return
        
        if result.get("status") == "skipped":
            return
        
        file_name = os.path.basename(result.get("file", "Unknown"))
        
        if result.get("status") == "infected":
            print(f"⚠️  THREAT DETECTED: {file_name}")
            print(f"   File: {result.get('file')}")
            print(f"   Hash: {result.get('hash')}")
            print(f"   Threats found:")
            for threat in result.get("threats", []):
                print(f"     - {threat}")
            if result.get("suspicious_lines"):
                print(f"   Suspicious code at lines:")
                for line_info in result.get("suspicious_lines", []):
                    print(f"     Line {line_info['line']}: {line_info['match']}")
            print()
        else:
            print(f"✅ CLEAN: {file_name}")
    
    def quarantine_file(self, file_path, quarantine_dir="quarantine"):
        """Move a file to quarantine directory."""
        try:
            if not os.path.exists(quarantine_dir):
                os.makedirs(quarantine_dir)
            
            file_name = os.path.basename(file_path)
            quarantine_path = os.path.join(quarantine_dir, file_name)
            
            # If file already exists in quarantine, add timestamp
            if os.path.exists(quarantine_path):
                import time
                timestamp = int(time.time())
                name, ext = os.path.splitext(file_name)
                quarantine_path = os.path.join(quarantine_dir, f"{name}_{timestamp}{ext}")
            
            os.rename(file_path, quarantine_path)
            print(f"📦 Quarantined: {file_path} -> {quarantine_path}")
            return True
        except Exception as e:
            print(f"❌ Error quarantining file: {e}")
            return False
    
    def scan_and_quarantine(self, directory_path, auto_quarantine=False):
        """Scan directory and optionally quarantine threats."""
        results = self.scan_directory(directory_path)
        
        infected_files = [r for r in results if r.get("status") == "infected"]
        
        if infected_files:
            print(f"\n⚠️  Found {len(infected_files)} infected file(s)")
            
            if auto_quarantine:
                print("\nQuarantining infected files...")
                for result in infected_files:
                    self.quarantine_file(result.get("file"))
            else:
                print("\nTo quarantine these files, run with --quarantine flag")
        else:
            print(f"\n✅ Scan complete: No threats detected")
        
        return results

def main():
    """Main function for the antivirus scanner."""
    scanner = SimpleAntivirus()
    
    # Default scan directory is current directory
    scan_path = "."
    auto_quarantine = False
    
    # Parse command line arguments
    if len(sys.argv) > 1:
        scan_path = sys.argv[1]
    
    if "--quarantine" in sys.argv or "-q" in sys.argv:
        auto_quarantine = True
    
    print("=" * 60)
    print("  SIMPLE ANTIVIRUS SCANNER (Educational Purpose)")
    print("=" * 60)
    print()
    
    if os.path.isfile(scan_path):
        # Scan single file
        result = scanner.scan_file(scan_path)
        scanner.display_result(result)
        
        if result.get("status") == "infected" and auto_quarantine:
            scanner.quarantine_file(scan_path)
    else:
        # Scan directory
        scanner.scan_and_quarantine(scan_path, auto_quarantine)
    
    print("\n" + "=" * 60)
    print("Scan complete!")

if __name__ == "__main__":
    main()

