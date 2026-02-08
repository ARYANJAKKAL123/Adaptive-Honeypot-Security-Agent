# 📚 Learning Notes & Reference

**Authors:** Aryan Jakkal & Dhirayshil Sarwade  
**Project:** Adaptive File System Honeypot Agent

---

## 📌 HOW TO USE THIS FILE

- Write down important concepts you learn
- Keep code snippets for reference
- Note useful commands
- Ask questions here

---

## 🎯 Project Overview

**What We're Building:**
- File system monitoring agent (watches files/folders)
- Threat detection algorithm (scores suspicious behavior)
- Automatic decoy deployment (creates fake files to trap attackers)
- Alert system (notifies when decoys are accessed)
- Simple dashboard (shows activity)

**Why It's Important:**
- Real-world cybersecurity application
- Catches attackers in action
- Adaptive and intelligent
- Can be deployed on any server

---

## 📖 Key Concepts Learned

### Week 1-2: Foundation

**Virtual Environments:**
```
What: Isolated Python environment for your project
Why: Keeps project dependencies separate
How: python -m venv venv
```

**Watchdog Library:**
```
What: Python library for monitoring file system events
Why: Detects when files are created, modified, deleted
How: 
```

**YAML Configuration:**
```
What: Human-readable config file format
Why: Easy to read and modify settings
How: Uses indentation like Python
```

**Threat Scoring:**
```
What: Algorithm to calculate how suspicious behavior is
Why: Determines when to deploy decoys
How: Assign points for suspicious actions (0-100 scale)
```

---

### Week 3-4: Core Features

**Faker Library:**
```
What: Generates realistic fake data
Why: Creates convincing decoy files
How: 
```

**Decoy Strategy:**
```
What: Fake files that look real to attackers
Why: Traps attackers and alerts you
How: 
```

**Alert System:**
```
What: Notification when suspicious activity detected
Why: Immediate response to threats
How: 
```

---

### Week 5-6: Service & Dashboard

**Windows Service:**
```
What: Program that runs in background
Why: Agent runs automatically on server
How: 
```

**Web Dashboard:**
```
What: Web interface to view activity
Why: Easy monitoring and management
How: 
```

---

## 💻 Useful Commands

### Python Commands
```bash
# Run your agent
python src/agent/main.py

# Run tests
pytest

# Install new package
pip install package-name

# Check installed packages
pip list
```

### Git Commands
```bash
# Check status
git status

# Add all changes
git add .

# Commit with message
git commit -m "message"

# Push to GitHub
git push

# View commit history
git log --oneline

# Create new branch
git checkout -b branch-name
```

### Virtual Environment
```bash
# Activate (Windows)
venv\Scripts\activate

# Deactivate
deactivate

# Check if active (look for (venv) in prompt)
```

---

## 🔍 Code Snippets

### Basic File Monitoring
```python
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"File created: {event.src_path}")
    
    def on_modified(self, event):
        print(f"File modified: {event.src_path}")

# Usage
observer = Observer()
observer.schedule(MyHandler(), path=".", recursive=True)
observer.start()
```

### Reading YAML Config
```python
import yaml

with open('config/config.yaml', 'r') as file:
    config = yaml.safe_load(file)
    
print(config['agent']['name'])
```

### Using Faker
```python
from faker import Faker

fake = Faker()

# Generate fake data
fake_name = fake.name()
fake_email = fake.email()
fake_password = fake.password()
```

### Basic Logging
```python
import logging

logging.basicConfig(
    filename='logs/events.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("This is an info message")
logging.warning("This is a warning")
logging.error("This is an error")
```

---

## ❓ Questions & Answers

### Q: Why use virtual environment?
**A:** Keeps your project dependencies isolated. Different projects can use different versions of libraries without conflicts.

### Q: What is a threat score?
**A:** A number (0-100) that represents how suspicious behavior is. Higher score = more suspicious. When score > threshold, deploy decoys.

### Q: How do decoys work?
**A:** They're fake files that look real. When an attacker accesses them, you know they're up to no good and can alert/block them.

### Q: What's the difference between monitoring and detection?
**A:** Monitoring = watching file activity. Detection = analyzing that activity to find suspicious patterns.

---

## 📝 My Questions

**Questions to ask teacher/mentor:**

```
1. 

2. 

3. 

```

---

## 💡 Ideas & Improvements

**Things I want to try:**

```
1. 

2. 

3. 

```

---

## 🐛 Common Errors & Solutions

### Error: "Module not found"
**Solution:** Make sure virtual environment is activated and package is installed
```bash
pip install package-name
```

### Error: "Permission denied"
**Solution:** Run as administrator or check file permissions

### Error: "Git push rejected"
**Solution:** Pull first, then push
```bash
git pull
git push
```

---

## 📚 Useful Resources

**Python Documentation:**
- https://docs.python.org/3/

**Watchdog Documentation:**
- https://python-watchdog.readthedocs.io/

**Faker Documentation:**
- https://faker.readthedocs.io/

**Git Tutorial:**
- https://git-scm.com/docs

---

**Keep adding to this file as you learn!** 📖
