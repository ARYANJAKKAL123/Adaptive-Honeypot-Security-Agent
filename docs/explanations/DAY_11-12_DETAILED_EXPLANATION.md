# 📘 Day 11-12: System Integration - Detailed Explanation

**Authors:** Aryan Jakkal & Dhirayshil Sarwade  
**Date:** February 17, 2026  
**Topic:** Integrating FileMonitor with ThreatDetector for Real-Time Threat Detection

---

## 🎯 What We Built

We integrated the `ThreatDetector` class (from Day 9-10) with the `FileMonitor` class (from Day 3-4) so that:
- Every file event is automatically analyzed for threats
- Threat scores are calculated in real-time
- Warnings are logged when suspicious activity is detected
- The system monitors AND protects simultaneously

---

## 🧠 The Big Picture: How Integration Works

Think of it like a security system in a building:

**Before Integration (Day 1-10):**
- FileMonitor = Security cameras (just watching and recording)
- ThreatDetector = Security analyst (can analyze, but not connected to cameras)
- They existed separately, not working together

**After Integration (Day 11-12):**
- Security cameras (FileMonitor) are now connected to the analyst (ThreatDetector)
- Every time a camera sees something, the analyst immediately checks if it's suspicious
- If suspicious, an alarm (warning log) is triggered
- Everything happens automatically in real-time!

---

## 📝 Step-by-Step: What We Did

### Step 1: Import ThreatDetector

```python
from .threat_detector import ThreatDetector
```

**What this means:**
- `.threat_detector` = Look in the same package (monitor folder) for threat_detector.py
- `ThreatDetector` = Import the ThreatDetector class from that file
- Now FileMonitor can use ThreatDetector's capabilities

**Real-world analogy:** Like hiring a security analyst to work with your security cameras

---

### Step 2: Create ThreatDetector Instance

```python
def __init__(self):
    super().__init__()
    self.logger = EventLogger()
    self.threat_detector = ThreatDetector()  # ← NEW LINE
    self.logger.log_info("FileMonitor initialized with threat detection")
```

**What this means:**
- `self.threat_detector = ThreatDetector()` creates a new ThreatDetector object
- `self.` makes it available to ALL methods in the FileMonitor class
- Every FileMonitor instance now has its own personal ThreatDetector

**Real-world analogy:** Each security camera system gets its own dedicated analyst

**Why `self.`?**
- Without `self.`: Variable only exists in `__init__()` method
- With `self.`: Variable exists for the entire lifetime of the object
- All methods (on_created, on_modified, on_deleted) can access it

---

### Step 3: Update on_created() Method

```python
def on_created(self, event):
    """Called when a file is created"""
    if not event.is_directory:
        self.logger.log_info(f"File Created: {event.src_path}")

        # Add event to threat detector
        self.threat_detector.add_event("created", event.src_path)

        # Check threat level
        threat_level = self.threat_detector.get_threat_level()
        threat_score = self.threat_detector.threat_score

        # Log if threat is elevated or higher
        if threat_score >= 31:
            self.logger.log_warning(
                f"Threat Level: {threat_level} (Score: {threat_score}) - "
                f"File: {event.src_path}"
            )
```

**Line-by-line breakdown:**

1. `self.logger.log_info(f"File Created: {event.src_path}")`
   - Log the file creation event (same as before)

2. `self.threat_detector.add_event("created", event.src_path)`
   - Send the event to ThreatDetector for analysis
   - "created" = event type
   - event.src_path = which file was created
   - ThreatDetector stores this and updates its internal threat score

3. `threat_level = self.threat_detector.get_threat_level()`
   - Ask ThreatDetector: "What's the current threat level?"
   - Returns: "Normal", "Elevated", "Suspicious", or "Critical"

4. `threat_score = self.threat_detector.threat_score`
   - Get the numerical score (0-100)
   - This is the raw number behind the threat level

5. `if threat_score >= 31:`
   - Only log warnings if score is 31 or higher
   - 31 = "Elevated" threat level (see Day 9-10 explanation)

6. `self.logger.log_warning(...)`
   - Log a WARNING (not just INFO) to highlight suspicious activity
   - Includes: threat level, score, and which file triggered it

**Real-world analogy:**
- Camera sees person enter building (file created)
- Camera sends footage to analyst (add_event)
- Analyst checks if person is suspicious (get_threat_level)
- If suspicious, analyst triggers alarm (log_warning)

---

### Step 4: Update on_modified() Method

```python
def on_modified(self, event):
    """Called when a file is modified"""
    if not event.is_directory:
        self.logger.log_info(f"File Modified: {event.src_path}")

        # Add event to threat detector
        self.threat_detector.add_event("modified", event.src_path)
    
        # Check threat level
        threat_level = self.threat_detector.get_threat_level()
        threat_score = self.threat_detector.threat_score
    
        # Log if threat is elevated or higher
        if threat_score >= 31:
            self.logger.log_warning(
                f"Threat Level: {threat_level} (Score: {threat_score}) - "
                f"File: {event.src_path}"
            )
```

**What's different from on_created()?**
- Only the event type: `"modified"` instead of `"created"`
- Everything else is identical
- This pattern (detect → analyze → warn) is consistent across all event types

**Why this matters:**
- File modifications can be suspicious (e.g., ransomware encrypting files)
- ThreatDetector tracks modification patterns
- Rapid modifications = higher threat score

---

### Step 5: Update on_deleted() Method

```python
def on_deleted(self, event):
    """Called when a file is deleted"""
    if not event.is_directory:
        self.logger.log_info(f"File Deleted: {event.src_path}")

        # Add event to threat detector
        self.threat_detector.add_event("deleted", event.src_path)

        # Check threat level
        threat_level = self.threat_detector.get_threat_level()
        threat_score = self.threat_detector.threat_score

        # Log if threat is elevated or higher
        if threat_score >= 31:
            self.logger.log_warning(
                f"Threat Level: {threat_level} (Score: {threat_score}) - "
                f"File: {event.src_path}"
            )
```

**Why deletions are important:**
- Deletions are often the most suspicious activity
- Attackers delete logs to cover their tracks
- Ransomware deletes original files after encryption
- ThreatDetector gives deletions +30 points (highest penalty)

---

## 🔄 How It All Works Together

**The Flow:**

```
1. User creates file "passwords.txt"
   ↓
2. Watchdog detects file creation
   ↓
3. Calls FileMonitor.on_created()
   ↓
4. FileMonitor logs: "File Created: passwords.txt"
   ↓
5. FileMonitor sends event to ThreatDetector
   ↓
6. ThreatDetector checks:
   - Is filename sensitive? YES (+25 points)
   - Rapid access? Maybe (+0 to +20 points)
   - Unusual time? Maybe (+0 to +15 points)
   ↓
7. ThreatDetector calculates total score: 25-60 points
   ↓
8. FileMonitor checks: Is score >= 31? YES
   ↓
9. FileMonitor logs WARNING with threat level
   ↓
10. User sees warning in console and log file
```

---

## 🎓 Key Concepts Learned

### 1. System Integration
**What it is:** Connecting multiple components to work together

**Why it matters:**
- Individual components are useful, but limited
- Integration creates a complete, functional system
- The whole is greater than the sum of its parts

**Example:**
- FileMonitor alone = just watching
- ThreatDetector alone = can analyze, but has no data
- Together = real-time threat detection system

---

### 2. Instance Variables (self.variable)
**What it is:** Variables that belong to an object and persist across method calls

**Why it matters:**
- Without `self.`: Variables disappear after method ends
- With `self.`: Variables live as long as the object lives
- Allows methods to share data and objects

**Example:**
```python
# BAD - won't work
def __init__(self):
    threat_detector = ThreatDetector()  # No self.

def on_created(self, event):
    threat_detector.add_event(...)  # ERROR! threat_detector doesn't exist here

# GOOD - works perfectly
def __init__(self):
    self.threat_detector = ThreatDetector()  # With self.

def on_created(self, event):
    self.threat_detector.add_event(...)  # Works! self.threat_detector exists
```

---

### 3. Real-Time Processing
**What it is:** Processing data immediately as it arrives, not in batches

**Why it matters:**
- Faster response to threats
- Immediate warnings when suspicious activity occurs
- Better security posture

**Example:**
- Batch processing: Analyze files every hour → Attacker has 1 hour to act
- Real-time: Analyze files instantly → Attacker detected in seconds

---

### 4. Event-Driven Architecture
**What it is:** System responds to events (file created, modified, deleted) as they happen

**Why it matters:**
- Efficient - only processes when something happens
- Scalable - can handle many events
- Responsive - immediate reaction to changes

**Example:**
- Polling (bad): Check for changes every second → Wastes CPU
- Event-driven (good): Only act when change happens → Efficient

---

### 5. Separation of Concerns
**What it is:** Each component has one clear responsibility

**Why it matters:**
- Easier to understand and maintain
- Can test components independently
- Can reuse components in different contexts

**Example:**
- FileMonitor: Detects file events
- ThreatDetector: Analyzes threat levels
- EventLogger: Records events
- Each does ONE thing well

---

## 🐛 Common Issues & Solutions

### Issue 1: ImportError - No module named 'watchdog'
**Problem:** Dependencies not installed

**Solution:**
```bash
pip install -e ".[dev]"
```

---

### Issue 2: ImportError - Attempted relative import with no known parent package
**Problem:** Running file directly instead of as module

**Solution:**
```bash
# BAD
python src/monitor/file_monitor.py

# GOOD
python -m src.monitor.file_monitor
```

---

### Issue 3: TOML parsing error
**Problem:** pyproject.toml file corrupted or has invalid syntax

**Solution:** Ensure pyproject.toml contains only valid TOML configuration, no extra text

---

## 🧪 Testing the Integrated System

**How to test:**

1. Start the monitor:
```bash
python -m src.monitor.file_monitor
```

2. In another terminal, create test files:
```bash
# Normal file - low threat
echo "hello" > test_monitor/normal.txt

# Sensitive file - higher threat
echo "password=secret" > test_monitor/passwords.txt

# Multiple rapid operations - even higher threat
for i in {1..5}; do echo "test" > test_monitor/file$i.txt; done

# Deletions - highest threat
rm test_monitor/file*.txt
```

3. Watch the output:
- INFO logs for all events
- WARNING logs when threat score >= 31
- Threat levels and scores displayed

---

## 📊 What Success Looks Like

**You know it's working when:**

1. ✅ Monitor starts without errors
2. ✅ Creates test_monitor folder automatically
3. ✅ Logs INFO messages for all file operations
4. ✅ Logs WARNING messages for suspicious activity
5. ✅ Threat scores increase with suspicious patterns
6. ✅ Can stop with Ctrl+C cleanly

**Example output:**
```
Starting to monitor: test_monitor
Created test folder: test_monitor
Monitoring Started! Press Ctrl+C to stop..
[2026-02-17 10:30:15] [INFO] File Created: test_monitor/passwords.txt
[2026-02-17 10:30:15] [WARNING] Threat Level: Elevated (Score: 25) - File: test_monitor/passwords.txt
```

---

## 🚀 What's Next?

**Day 13-14: Week 2 Review**
- Review all code from Week 1-2
- Fix any bugs
- Update documentation
- Test entire system thoroughly
- Prepare for Week 3 (Decoy system)

**Future enhancements:**
- Add more threat detection rules
- Implement automatic responses to threats
- Create decoy files to trap attackers
- Build alert system for critical threats

---

## 💡 Pro Tips

1. **Always use `self.` for objects you need across methods**
   - Makes objects available everywhere in the class

2. **Test integration early and often**
   - Don't wait until everything is built
   - Integrate components as you build them

3. **Keep components loosely coupled**
   - FileMonitor doesn't need to know HOW ThreatDetector works
   - It just calls methods and gets results
   - This makes code flexible and maintainable

4. **Log at appropriate levels**
   - INFO: Normal operations
   - WARNING: Suspicious but not critical
   - ERROR: Something went wrong
   - This helps filter logs later

5. **Use real-world analogies**
   - Helps understand abstract concepts
   - Makes code easier to explain to others
   - Useful for documentation and presentations

---

## 📚 Key Takeaways

1. **Integration is powerful** - Connecting components creates complete systems
2. **Instance variables enable sharing** - `self.variable` makes data available across methods
3. **Real-time processing is efficient** - Process events as they happen, not in batches
4. **Event-driven architecture scales** - Responds to events, doesn't waste resources polling
5. **Separation of concerns matters** - Each component has one clear responsibility
6. **Testing integrated systems requires running the actual program** - Unit tests aren't enough
7. **Configuration files must be valid** - Corrupted configs prevent the entire system from working

---

**Congratulations! You've built a real-time threat detection system!** 🎉

Your FileMonitor and ThreatDetector are now working together to protect the file system. This is a major milestone in your honeypot project!

