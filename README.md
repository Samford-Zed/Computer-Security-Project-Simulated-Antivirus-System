
# Educational Virus and Antivirus System

### Easiest Way:
1. **Double-click `START_HERE.bat`** - Opens the menu
2. OR run: `python scripts\run.py`

### Menu Options:
1. **Run Antivirus Scanner** - Scans for threats
2. **Run Virus Simulation** - Delete a victim file
3. **Run Antivirus with Quarantine** - Scan and remove threats
4. **Open Shell** - Run commands directly
5. **Exit** - Close the program

## 📋 How to Run

### Run the Antivirus:
- **Option 1**: Choose "Run Antivirus Scanner" from menu
- **Command line**: `python scripts\antivirus.py`

The antivirus will:
- Scan all Python files
- Show which files are threats
- Display file hashes
- Show suspicious code patterns

### Run the Virus Simulation:
- **Option 2**: Choose "Run Virus Simulation" from menu
- **Command line**: `python scripts\simple_virus.py victim_files\filename.txt`

The virus will:
- Show list of victim files
- Let you choose which one to delete
- Delete the selected file

### Run Antivirus with Quarantine:
- **Option 3**: Choose "Run Antivirus with Quarantine"
- **Command line**: `python scripts\antivirus.py --quarantine`

This will:
- Scan for threats
- Move infected files to `quarantine` folder
- Keep your files safe

### Open Shell (Option 4):
- Opens an interactive Python shell
- Run commands directly
- Type `exit()` to return to menu

## 📁 Folder Structure

```
virus/
├── scripts/
│   ├── run.py              - Main launcher with menu
│   ├── antivirus.py         - Antivirus scanner
│   └── simple_virus.py     - Virus simulation
├── docs/
│   └── README.md            - This file
├── victim_files/            - Folder with test files
│   ├── criminal_history.txt
│   ├── bank_accounts.txt
│   ├── secret_plans.txt
│   ├── classified_documents.txt
│   ├── private_evidence.txt
│   ├── confidential_notes.txt
│   ├── personal_finances.txt
│   ├── employee_records.txt
│   ├── project_blueprint.txt
│   ├── system_configs.txt
│   ├── photo_archive.txt
│   └── email_archive.txt
└── START_HERE.bat           - Quick start (Windows)
```

## ⚠️ Important Notes

- **DO NOT use maliciously**
- **Only for educational purposes**
- **Only run on files you own**
- **Use responsibly**

## 🔧 Troubleshooting

**Python not found?**
- Try: `py scripts\run.py` instead of `python scripts\run.py`
- Make sure Python is installed

**Files not found?**
- Make sure you're in the correct folder
- Run from the `virus` directory


