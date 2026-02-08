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

## 📅 Day 7-8: Testing & Bug Fixes

**Date:** _________

**Tasks:**
- [ ] Write unit tests in `tests/test_monitor.py`
- [ ] Test edge cases (empty files, large files)
- [ ] Fix any bugs found
- [ ] Document your code with comments
- [ ] Review Week 1 progress

**What I Learned:**
```
1. 

2. 

3. 
```

---

## 📅 Day 9-10: Threat Detection Algorithm

**Date:** _________

**Tasks:**
- [ ] Create ThreatDetector class in `src/monitor/threat_detector.py`
- [ ] Design scoring system (0-100 scale)
- [ ] Implement basic rules:
  - Rapid file access = +20 points
  - Unusual time access = +15 points
  - Multiple failed attempts = +25 points
- [ ] Test with sample data

**Code to Write:**
```python
# src/monitor/threat_detector.py
- ThreatDetector class
- calculate_threat_score() method
- Rules for suspicious behavior
```

**What I Learned:**
```
1. 

2. 

3. 
```

---

## 📅 Day 11-12: Scoring System Refinement

**Date:** _________

**Tasks:**
- [ ] Add more threat indicators
- [ ] Adjust score thresholds
- [ ] Test scoring accuracy
- [ ] Create threat level categories (Low, Medium, High)
- [ ] Document scoring logic

**What I Learned:**
```
1. 

2. 

3. 
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
