# ✅ Daily Tasks & Checklists

**Authors:** Aryan Jakkal & Dhirayshil Sarwade  
**Project:** Adaptive File System Honeypot Agent

---

## 📌 HOW TO USE THIS FILE

**Simple 3-step process:**

1. **Check boxes ✅** as you complete each task
2. **Write what you learned** after each day
3. **Tell me when done:** "I completed Day X"

**Then I'll automatically update your progress tracker!** 🤖

---

## 📅 Day 1-2: Project Setup ✅ COMPLETED

**Date Completed:** February 8, 2026

**Tasks:**
- [x] Created virtual environment
- [x] Created project folders
- [x] Created pyproject.toml
- [x] Installed dependencies
- [x] Created main.py
- [x] Created config.yaml
- [x] Set up Git

**What I Learned:**
```
1. Virtual environments keep project dependencies isolated
2. pyproject.toml is the modern way to configure Python projects
3. Git workflow: status → add → commit → push
```

---

## 📅 Day 3-4: File Monitoring Basics ✅ COMPLETED

**Date Completed:** February 8, 2026

**Tasks:**
- [x] Learn watchdog library
- [x] Create FileMonitor class in `src/monitor/file_monitor.py`
- [x] Implement file change detection (created, modified, deleted)
- [x] Test monitoring on a test folder
- [x] Log events to console

**Code to Write:**
```python
# src/monitor/file_monitor.py
- FileMonitor class ✅
- on_created() method ✅
- on_modified() method ✅
- on_deleted() method ✅
```

**What I Learned:**
```
1. Watchdog library uses Observer pattern to monitor file system events in real-time
2. FileSystemEventHandler provides methods (on_created, on_modified, on_deleted) that run when files change
3. Observer.schedule() watches a directory continuously and calls event handlers automatically
4. Indentation is critical in Python - functions inside vs outside classes behave differently 

2. 

3. 
```

---

## 📅 Day 5-6: Event Logging ✅ COMPLETED

**Date Completed:** February 8, 2026

**Tasks:**
- [x] Create Logger class in `src/monitor/logger.py`
- [x] Log events to `logs/events.log` file
- [x] Add timestamps to logs
- [x] Add log levels (INFO, WARNING, ERROR)
- [x] Test logging system

**Code to Write:**
```python
# src/monitor/logger.py
- EventLogger class ✅
- log_info() method ✅
- log_warning() method ✅
- log_error() method ✅
- Format: [timestamp] [level] message ✅
```

**What I Learned:**
```
1. Python's logging module provides professional logging with timestamps and levels
2. Log levels (INFO, WARNING, ERROR) help categorize events by severity
3. Logging to files creates permanent records unlike print() statements
4. Relative imports (.logger) are used to import modules from the same package
5. Instance variables (self.logger) make objects available to all class methods
```
```
1. 

2. 

3. 
```

---

## 📅 Day 7-8: Testing & Bug Fixes ✅ COMPLETED

**Date Completed:** February 13, 2026

**Tasks:**
- [x] Write unit tests in `tests/simple_test.py`
- [x] Test logger creation and log levels
- [x] Test FileMonitor creation and event handling
- [x] Fix bugs (indentation, imports, typos)
- [x] All 4 tests passing successfully

**What I Learned:**
```
1. Testing is essential - write tests to verify code works correctly before moving forward
2. Try-except blocks catch errors gracefully without crashing the program
3. Mock objects let you test code without needing real files or events
4. Python's logging module has limitations - basicConfig() only works once per program
5. Indentation and function placement are critical in Python - functions must be defined before they're called
6. Tuple unpacking and generator expressions make code cleaner and more Pythonic
```

---

## 📅 Day 9-10: Threat Detection Algorithm ✅ COMPLETED

**Date Completed:** February 17, 2026

**Tasks:**
- [x] Create ThreatDetector class in `src/monitor/threat_detector.py`
- [x] Design scoring system (0-100 scale)
- [x] Implement basic rules:
  - Rapid file access = +20 points
  - Unusual time access = +15 points
  - Sensitive files = +25 points
  - Multiple deletions = +30 points
- [x] Test with sample data

**Code to Write:**
```python
# src/monitor/threat_detector.py
- ThreatDetector class ✅
- calculate_threat_score() method ✅
- Rules for suspicious behavior ✅
- check_rapid_access() method ✅
- check_unusual_time() method ✅
- check_sensitive_files() method ✅
- check_deletions() method ✅
- get_threat_level() method ✅
- get_threat_info() method ✅
```

**What I Learned:**
```
1. Threat detection uses scoring algorithms - multiple rules contribute points to calculate suspicion level
2. Time-based analysis is crucial - using timestamps (time.time()) to detect rapid access and unusual hours
3. List comprehensions filter data efficiently - [e for e in events if condition] creates filtered lists in one line
4. Dictionaries store event data - {'type': 'created', 'path': 'file.txt', 'time': timestamp} keeps related info together
5. Instance variables (self.variable) make data available to all methods in a class
6. Threshold-based decision making - different score ranges (0-30, 31-50, 51-70, 71-100) trigger different threat levels
7. The min() function caps values - min(score, 100) ensures score never exceeds 100 
```

---

## 📅 Day 11-12: System Integration (FileMonitor + ThreatDetector) ✅ COMPLETED

**Date Completed:** February 17, 2026

**Tasks:**
- [x] Integrate ThreatDetector with FileMonitor
- [x] Add threat detection to all event handlers (on_created, on_modified, on_deleted)
- [x] Log warnings when threat score >= 31
- [x] Test integrated system with real file operations
- [x] Fix pyproject.toml configuration issues
- [x] Install dependencies and run system successfully

**Code Changes:**
```python
# src/monitor/file_monitor.py
- Added import: from .threat_detector import ThreatDetector ✅
- Created instance: self.threat_detector = ThreatDetector() ✅
- Updated on_created() to send events and check threat level ✅
- Updated on_modified() to send events and check threat level ✅
- Updated on_deleted() to send events and check threat level ✅
```

**What I Learned:**
```
1. System integration connects multiple components - FileMonitor now uses ThreatDetector in real-time
2. Instance variables (self.threat_detector) make objects available across all class methods
3. Real-time threat detection works by: detect event → add to detector → calculate score → log if suspicious
4. pyproject.toml must have valid TOML syntax - corrupted config files prevent dependency installation
5. Testing integrated systems requires running the actual program, not just unit tests
6. The -e flag in pip install makes code changes take effect immediately without reinstalling
7. Step-by-step implementation helps understand how components connect and work together
```

---

## 📅 Day 13-14: Week 2 Review

**Date:** _________

**Tasks:**
- [ ] Review all code
- [ ] Fix bugs
- [ ] Update documentation
- [ ] Test entire system
- [ ] Prepare for Week 3

**What I Learned:**
```
1. 

2. 

3. 
```

---

## 📅 Day 15-16: Decoy File Generator

**Date:** _________

**Tasks:**
- [ ] Create DecoyGenerator class in `src/decoy/generator.py`
- [ ] Use Faker library to create realistic files
- [ ] Generate fake credentials (passwords.txt)
- [ ] Generate fake documents (report.pdf)
- [ ] Test decoy creation

**Code to Write:**
```python
# src/decoy/generator.py
- DecoyGenerator class
- generate_credential_file() method
- generate_document_file() method
```

**What I Learned:**
```
1. 

2. 

3. 
```

---

## 📅 Day 17-18: Decoy Deployment

**Date:** _________

**Tasks:**
- [ ] Create DecoyManager class in `src/decoy/manager.py`
- [ ] Deploy decoys when threat score > 50
- [ ] Place decoys in strategic locations
- [ ] Track deployed decoys
- [ ] Test deployment logic

**What I Learned:**
```
1. 

2. 

3. 
```

---

## 📅 Day 19-20: Decoy Tracking

**Date:** _________

**Tasks:**
- [ ] Monitor decoy file access
- [ ] Log when attacker touches decoy
- [ ] Capture attacker information
- [ ] Test tracking system
- [ ] Document tracking logic

**What I Learned:**
```
1. 

2. 

3. 
```

---

## 📅 Day 21-22: Alert System

**Date:** _________

**Tasks:**
- [ ] Create AlertManager class in `src/alert/manager.py`
- [ ] Send alerts when decoy accessed
- [ ] Log alerts to file
- [ ] Add alert levels (Low, Medium, High, Critical)
- [ ] Test alert system

**What I Learned:**
```
1. 

2. 

3. 
```

---

## 📅 Day 23-24: Email/Log Alerts

**Date:** _________

**Tasks:**
- [ ] Add email alert option (optional)
- [ ] Improve log formatting
- [ ] Add alert details (time, file, threat score)
- [ ] Test alert delivery
- [ ] Document alert system

**What I Learned:**
```
1. 

2. 

3. 
```

---

## 📅 Day 25-26: Integration Testing

**Date:** _________

**Tasks:**
- [ ] Test entire system together
- [ ] Simulate attacker behavior
- [ ] Verify decoys deploy correctly
- [ ] Verify alerts work
- [ ] Fix integration bugs

**What I Learned:**
```
1. 

2. 

3. 
```

---

## 📅 Day 27-28: Week 4 Review

**Date:** _________

**Tasks:**
- [ ] Review all code
- [ ] Fix bugs
- [ ] Update documentation
- [ ] Test system thoroughly
- [ ] Prepare for Week 5

**What I Learned:**
```
1. 

2. 

3. 
```

---

## 📅 Day 29-56: Remaining Days

**Continue adding your daily tasks here as you progress!**

Each day, add:
- Date
- Tasks to complete
- What you learned

---

## 🔄 END OF DAY ROUTINE

**Every day, do these 3 things:**

1. ✅ Check off completed tasks above
2. 📝 Write what you learned
3. 💾 Git commit (see file: `2_PROGRESS_TRACKER.md`)

---

**Keep going! You're doing great!** 🚀
