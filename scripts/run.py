"""
Simple Launcher - Easy way to run the virus and antivirus scripts
Just double-click this file or run: python run.py
"""

import os
import sys
import subprocess

def print_menu():
    """Display the main menu."""
    print("\n" + "=" * 60)
    print("  EDUCATIONAL VIRUS & ANTIVIRUS - LAUNCHER")
    print("=" * 60)
    print("\nWhat would you like to do?")
    print("\n1. Run Antivirus Scanner (scan for threats)")
    print("2. Run Virus Simulation (delete a test file)")
    print("3. Run Antivirus with Quarantine (scan and remove threats)")
    print("4. Open Shell (run commands directly)")
    print("5. Exit")
    print("\n" + "-" * 60)

def run_antivirus():
    """Run the antivirus scanner."""
    print("\n🔍 Running Antivirus Scanner...")
    print("-" * 60)
    try:
        # Get the script directory
        script_dir = os.path.dirname(os.path.abspath(__file__))
        antivirus_path = os.path.join(script_dir, "antivirus.py")
        subprocess.run([sys.executable, antivirus_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running antivirus: {e}")
    except FileNotFoundError:
        print("❌ Error: antivirus.py not found!")

def run_virus():
    """Run the virus simulation - choose which victim file to delete."""
    print("\n⚠️  Running Virus Simulation...")
    print("-" * 60)
    print("NOTE: Real viruses target EXISTING files without asking!")
    print("-" * 60)
    
    # Get existing victim files
    existing_files, all_victim_files = get_victim_files()
    
    # If no victim files exist, offer to create them
    if not existing_files:
        print("\n❌ No victim files found!")
        print("\nA REAL VIRUS would target files that ALREADY EXIST.")
        print("For this demo, we need to create some victim files first.")
        create = input("\nWould you like to create victim files? (y/n): ").lower()
        if create == 'y':
            create_victim_files()
            existing_files, _ = get_victim_files()
        else:
            print("Cancelled.")
            return
    
    # Show available victim files
    print(f"\n📋 Found {len(existing_files)} victim file(s) to target:")
    print("-" * 60)
    for i, filepath in enumerate(existing_files, 1):
        filename = os.path.basename(filepath)  # Show just the filename
        print(f"  {i}. {filename}")
    print("-" * 60)
    
    # Let user choose which file to delete
    try:
        choice = input(f"\nWhich victim file should the virus delete? (1-{len(existing_files)}): ").strip()
        choice_num = int(choice)
        
        if 1 <= choice_num <= len(existing_files):
            target_file = existing_files[choice_num - 1]
            filename = os.path.basename(target_file)  # Just the filename for display
            
            print(f"\n🎯 Target selected: {filename}")
            print("\n⚠️  WARNING: In a REAL virus, this would happen WITHOUT asking!")
            print("   (We're asking for safety in this educational version)")
            confirm = input(f"\nSimulate deletion of '{target_file}'? (y/n): ").lower()
            
            if confirm == 'y':
                try:
                    # Get the script directory
                    script_dir = os.path.dirname(os.path.abspath(__file__))
                    virus_path = os.path.join(script_dir, "simple_virus.py")
                    subprocess.run([sys.executable, virus_path, target_file], check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Error running virus: {e}")
                except FileNotFoundError:
                    print("❌ Error: simple_virus.py not found!")
            else:
                print("Cancelled.")
        else:
            print(f"❌ Invalid choice! Please enter a number between 1 and {len(existing_files)}")
    except ValueError:
        print("❌ Invalid input! Please enter a number.")
    except Exception as e:
        print(f"❌ Error: {e}")

def run_antivirus_quarantine():
    """Run antivirus with quarantine option."""
    print("\n🔍 Running Antivirus Scanner with Quarantine...")
    print("-" * 60)
    try:
        # Get the script directory
        script_dir = os.path.dirname(os.path.abspath(__file__))
        antivirus_path = os.path.join(script_dir, "antivirus.py")
        subprocess.run([sys.executable, antivirus_path, "--quarantine"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running antivirus: {e}")
    except FileNotFoundError:
        print("❌ Error: antivirus.py not found!")

def get_victim_files():
    """Get list of victim files that exist."""
    # Get parent directory (where victim_files folder should be)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    victim_folder = os.path.join(parent_dir, "victim_files")
    # Create folder if it doesn't exist
    if not os.path.exists(victim_folder):
        os.makedirs(victim_folder)
    
    victim_files = [
        "criminal_history.txt",
        "bank_accounts.txt",
        "secret_plans.txt",
        "classified_documents.txt",
        "private_evidence.txt",
        # New sample victim files
        "confidential_notes.txt",
        "personal_finances.txt",
        "employee_records.txt",
        "project_blueprint.txt",
        "system_configs.txt",
        "photo_archive.txt",
        "email_archive.txt"
    ]
    # Check for files in the victim_files folder
    existing_files = []
    for filename in victim_files:
        filepath = os.path.join(victim_folder, filename)
        if os.path.exists(filepath):
            existing_files.append(filepath)
    
    return existing_files, victim_files

def create_victim_files():
    """Create the sample victim files for the simulation."""
    # Get parent directory (where victim_files folder should be)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    victim_folder = os.path.join(parent_dir, "victim_files")
    # Create folder if it doesn't exist
    if not os.path.exists(victim_folder):
        os.makedirs(victim_folder)
        print(f"📁 Created folder: {victim_folder}")
    
    victim_files = [
        ("criminal_history.txt", "Detailed criminal history and records of past activities."),
        ("bank_accounts.txt", "List of bank accounts and financial information."),
        ("secret_plans.txt", "Confidential plans and strategies for upcoming projects."),
        ("classified_documents.txt", "Classified documents for educational simulation only."),
        ("private_evidence.txt", "Private notes and evidence for demo use."),
        # New sample victim files
        ("confidential_notes.txt", "Confidential notes and meeting summaries (demo content)."),
        ("personal_finances.txt", "Personal finance overview and budgeting notes (demo)."),
        ("employee_records.txt", "Employee records sample data for simulation."),
        ("project_blueprint.txt", "Project blueprint and architecture overview (sample)."),
        ("system_configs.txt", "System configuration settings (example content)."),
        ("photo_archive.txt", "List of photo filenames and metadata (sample)."),
        ("email_archive.txt", "Email subjects and dates (example archive).")
    ]
    
    created = 0
    already_exist = 0
    
    for filename, content in victim_files:
        filepath = os.path.join(victim_folder, filename)
        if os.path.exists(filepath):
            already_exist += 1
        else:
            try:
                with open(filepath, 'w') as f:
                    f.write(content + "\n")
                created += 1
            except Exception as e:
                print(f"❌ Error creating {filename}: {e}")
    
    if created > 0:
        print(f"✅ Created {created} victim file(s) in {victim_folder}/")
    if already_exist > 0:
        print(f"ℹ️  {already_exist} file(s) already exist in {victim_folder}/")
    
    if created == 0 and already_exist == 0:
        print("❌ No files were created")
    elif created + already_exist == len(victim_files):
        print(f"\n✅ All {len(victim_files)} victim files are ready in {victim_folder}/")

def open_shell():
    """Open an interactive Python shell."""
    print("\n🐚 Opening Python Shell...")
    print("-" * 60)
    print("You can run Python commands here.")
    print("Type 'exit()' to return to the menu.")
    print("-" * 60)
    print()
    
    # Import code module for interactive shell
    try:
        import code
        # Create a local namespace with useful imports
        local_vars = {
            'os': os,
            'sys': sys,
            'subprocess': subprocess,
        }
        # Start interactive shell
        shell = code.InteractiveConsole(locals=local_vars)
        shell.interact(banner="Python Shell (type exit() to return)", exitmsg="Returning to menu...")
    except ImportError:
        print("❌ Error: Could not start interactive shell")
        print("You can still run commands manually:")
        print("  python antivirus.py")
        print("  python simple_virus.py <file>")

def main():
    """Main function with menu loop."""
    while True:
        print_menu()
        
        try:
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == '1':
                run_antivirus()
            elif choice == '2':
                run_virus()
            elif choice == '3':
                run_antivirus_quarantine()
            elif choice == '4':
                open_shell()
            elif choice == '5':
                print("\n👋 Goodbye!")
                break
            else:
                print("\n❌ Invalid choice! Please enter 1-5.")
            
            if choice != '5' and choice != '4':  # Don't pause after shell
                input("\nPress Enter to continue...")
                
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()

