# Adaptive File System Honeypot Agent

**Final Year Diploma Project - 2025**  
**Authors:** Aryan Jakkal & Dhirayshil Sarwade  
**Status:** 🟢 In Development (Week 1 - 7% Complete)

---

## 📋 Project Overview

An adaptive file system honeypot that monitors file activity, detects suspicious behavior, and automatically deploys decoy files to trap attackers.

### Key Features

- 🔍 **Real-time File Monitoring** - Detects file creation, modification, and deletion
- 🎯 **Threat Detection** - Scores suspicious behavior using custom algorithm
- 🎭 **Adaptive Decoy Deployment** - Automatically creates fake files when threats detected
- 🚨 **Alert System** - Notifies when attackers access decoys
- 📊 **Dashboard** - Web interface to monitor activity

---

## 🚀 Current Features (Implemented)

### ✅ Day 1-2: Project Setup
- Virtual environment configured
- Project structure created
- Dependencies installed (watchdog, pyyaml, faker, pytest)
- Git repository initialized

### ✅ Day 3-4: File Monitoring System
- **FileMonitor class** - Monitors file system events
- **Event detection** - Tracks file created, modified, deleted
- **Observer pattern** - Continuous monitoring using watchdog library
- **Test suite** - Verified monitoring functionality

**Files:** `src/monitor/file_monitor.py`

---

## 🔄 In Progress

### 🔨 Day 5-6: Event Logging (Next)
- Logger class for persistent event storage
- Timestamp tracking
- Log levels (INFO, WARNING, ERROR)
- File-based logging system

---

## 📊 Development Progress

**Overall:** 7% Complete (4/56 days)

### Week 1-2: Foundation (29% Complete)
- [x] Day 1-2: Project setup
- [x] Day 3-4: File monitoring
- [ ] Day 5-6: Event logging
- [ ] Day 7-8: Testing & bug fixes
- [ ] Day 9-10: Threat detection algorithm
- [ ] Day 11-12: Scoring system
- [ ] Day 13-14: Week review

### Week 3-4: Core Features (0% Complete)
- [ ] Day 15-16: Decoy file generator
- [ ] Day 17-18: Decoy deployment
- [ ] Day 19-20: Decoy tracking
- [ ] Day 21-22: Alert system
- [ ] Day 23-24: Email/log alerts
- [ ] Day 25-26: Integration testing
- [ ] Day 27-28: Week review

### Week 5-6: Service & Dashboard (0% Complete)
- [ ] Day 29-30: Windows service setup
- [ ] Day 31-32: Service testing
- [ ] Day 33-34: Web dashboard
- [ ] Day 35-36: Dashboard features
- [ ] Day 37-38: Real-time updates
- [ ] Day 39-40: Polish
- [ ] Day 41-42: Week review

### Week 7-8: Testing & Documentation (0% Complete)
- [ ] Day 43-56: System testing, bug fixes, documentation, presentation prep

---

## 🛠️ Technology Stack

**Language:** Python 3.14  
**Key Libraries:**
- `watchdog` - File system monitoring
- `pyyaml` - Configuration management
- `faker` - Decoy file generation
- `pytest` - Testing framework

**Development Tools:**
- Git for version control
- Virtual environment for dependency isolation

---

## 📁 Project Structure

```
Adaptive-Honeypot-Security-Agent/
├── src/
│   ├── agent/          # Main agent entry point
│   ├── monitor/        # File monitoring system ✅
│   ├── decoy/          # Decoy file generation
│   └── alert/          # Alert system
├── config/             # Configuration files
│   └── config.yaml     # Main configuration
├── tests/              # Test files
├── logs/               # Log files (generated)
├── docs/               # Learning documentation (private)
└── README.md           # This file
```

---

## 🚀 How to Run

### Prerequisites
- Python 3.10 or higher
- Git

### Setup
```bash
# Clone the repository
git clone https://github.com/ARYANJAKKAL123/Adaptive-Honeypot-Security-Agent.git
cd Adaptive-Honeypot-Security-Agent

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -e ".[dev]"
```

### Run File Monitor (Current Feature)
```bash
# Test the file monitoring system
python src/monitor/file_monitor.py
```

This will:
1. Create a `test_monitor` folder
2. Start monitoring it for file changes
3. Print events to console
4. Press Ctrl+C to stop

---

## 🧪 Testing

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_monitor.py
```

---

## 📖 Documentation

- **Learning Materials:** See `docs/` folder (private, not in repo)
- **Code Documentation:** Inline comments and docstrings in source files
- **Configuration:** See `config/config.yaml` for settings

---

## 🎯 Project Goals

### Educational Goals
- Learn file system monitoring techniques
- Understand threat detection algorithms
- Practice Python OOP and design patterns
- Build a complete, working security tool

### Technical Goals
- Real-time file system monitoring
- Adaptive threat response
- Deployable security agent
- Professional code quality

---

## 📝 Recent Updates

### February 8, 2026
- ✅ Completed Day 3-4: File monitoring system
- ✅ Implemented FileMonitor class with event detection
- ✅ Tested monitoring on test folder
- 📊 Progress: 7% complete

### February 8, 2026
- ✅ Completed Day 1-2: Project setup
- ✅ Organized project structure
- ✅ Configured development environment

---

## 🤝 Contributing

This is a student project for educational purposes. Not accepting external contributions at this time.

---

## 📄 License

Educational project - All rights reserved

---

## 👥 Authors

**Aryan Jakkal** - Developer  
**Dhirayshil Sarwade** - Developer

3rd Year Diploma Students  
Final Year Project - 2025

---

## 📚 Learning Resources

For detailed learning materials and daily progress tracking, see the `docs/` folder:
- [`docs/START_HERE.md`](docs/START_HERE.md) - Getting started guide
- [`docs/1_DAILY_TASKS.md`](docs/1_DAILY_TASKS.md) - Daily task checklist
- [`docs/2_PROGRESS_TRACKER.md`](docs/2_PROGRESS_TRACKER.md) - Progress tracking
- [`docs/3_LEARNING_NOTES.md`](docs/3_LEARNING_NOTES.md) - Learning notes and reference

---

**Last Updated:** February 8, 2026
