# 📖 Day 9-10 Complete Breakdown: Threat Detection Algorithm

**Date:** February 17, 2026  
**What You Built:** Threat detection system with scoring algorithm  
**Files Created:** `src/monitor/threat_detector.py`

---

## 🎯 Quick Overview

**What you built:** An intelligent threat detection system that analyzes file system events, calculates threat scores, and categorizes threat levels.

**Why it matters:** This is the "brain" of your honeypot. It transforms raw file events into actionable intelligence, determining when behavior is suspicious enough to deploy decoys or send alerts.

**Real-world use:** Intrusion Detection Systems (IDS), Security Information and Event Management (SIEM) systems, and antivirus software all use similar scoring algorithms to detect threats.

---

## 🧠 Understanding Threat Detection

### What is Threat Detection?

**Simple definition:**
An algorithm that analyzes patterns in file system activity and assigns a "suspiciousness score" to determine if an attacker might be present.

**Real-world analogy:**
- Like a security guard watching surveillance cameras
- Normal behavior = low score (employee entering with badge)
- Suspicious behavior = high score (someone trying multiple locked doors at 3 AM)
- When score exceeds threshold → take action (deploy decoys, send alert)

### How the Scoring System Works

```
File Events → Threat Detector → Score (0-100) → Threat Level → Action
                                                      ↓
                                    0-30: Normal (monitor)
                                    31-50: Elevated (watch closely)
                                    51-70: Suspicious (deploy decoys)
                                    71-100: Critical (deploy + alert)
```

---

## 📊 The Scoring Rules Explained

### Rule 1: Rapid File Access (+20 points)

**What it detects:**
- Too many files accessed in a short time
- 5+ events in 10 seconds = suspicious

**Why it's suspicious:**
- Normal users: Open 1-2 files per minute
- Attackers: Scan 10-20 files per minute (automated tools)
- Indicates reconnaissance or data exfiltration

**Example:**
```
Normal behavior:
0s: open document.txt
30s: open report.pdf
60s: open data.xlsx
→ 3 files in 60 seconds (NORMAL)

Suspicious behavior:
0s: open file1.txt
2s: open file2.txt
4s: open file3.txt
6s: open file4.txt
8s: open file5.txt
10s: open file6.txt
→ 6 files in 10 seconds (SUSPICIOUS +20 points)
```

---

### Rule 2: Unusual Time Access (+15 points)

**What it detects:**
- File activity during odd hours (midnight - 5 AM)

**Why it's suspicious:**
- Most legitimate work: 9 AM - 6 PM
- Some late work: 6 PM - midnight
- Very rare legitimate work: midnight - 5 AM
- Attackers often work at night (less likely to be noticed)

**Example:**
```
Normal:
2:00 PM - User edits document → Score: 0

Suspicious:
2:00 AM - User edits document → Score: +15
```

**Note:** This may cause false positives for:
- Night shift workers
- International teams
- Automated backups
- We accept some false positives for better security

---

### Rule 3: Sensitive File Access (+25 points)

**What it detects:**
- Files with suspicious keywords in their names
- Keywords: password, secret, key, token, config, credential, auth, private, id_rsa, ssh, api_key, database, backup

**Why it's suspicious:**
- These files often contain valuable information
- Attackers specifically search for these
- Accessing them indicates reconnaissance

**Example:**
```
Normal files:
- document.txt → Score: 0
- report.pdf → Score: 0
- notes.md → Score: 0

Sensitive files:
- passwords.txt → Score: +25
- config.yaml → Score: +25
- id_rsa (SSH key) → Score: +25
- api_keys.env → Score: +25
```

**Multiple sensitive files:**
```
Accessing 3 sensitive files:
- passwords.txt (+25)
- secret_key.txt (+25)
- database_backup.sql (+25)
→ Total: +75 points (CRITICAL!)
```

---

### Rule 4: Multiple Deletions (+30 points)

**What it detects:**
- 3+ files deleted in 30 seconds

**Why it's suspicious:**
- Attackers delete logs to hide tracks
- Ransomware deletes original files
- Data theft might involve deleting evidence
- Normal users rarely delete many files at once

**Example:**
```
Normal:
Delete 1 file occasionally → Score: 0

Suspicious:
0s: delete log1.txt
10s: delete log2.txt
20s: delete log3.txt
30s: delete log4.txt
→ 4 deletions in 30 seconds (+30 points)
```

---

## 🎯 Threat Levels Explained

### The Four Threat Levels

| Score | Level | Meaning | Action |
|-------|-------|---------|--------|
| 0-30 | Normal | Regular activity | Monitor only |
| 31-50 | Elevated | Slightly unusual | Watch closely |
| 51-70 | Suspicious | Likely threat | Deploy decoys |
| 71-100 | Critical | Active attack | Deploy decoys + Alert |

### Example Scenarios

**Scenario 1: Normal User**
```
10:00 AM - Create document.txt
Score: 0 (normal time, normal file)
Level: Normal
Action: None
```

**Scenario 2: Elevated Threat**
```
2:00 AM - Create report.pdf
Score: 15 (unusual time)
Level: Elevated
Action: Monitor closely
```

**Scenario 3: Suspicious Threat**
```
2:00 PM - Access passwords.txt
Score: 25 (sensitive file)

Then rapidly access 5 more files
Score: 25 + 20 = 45

Then access config.yaml
Score: 45 + 25 = 70
Level: Suspicious
Action: Deploy decoys!
```

**Scenario 4: Critical Threat**
```
3:00 AM - Access secret_key.txt
Score: 15 (time) + 25 (sensitive) = 40

Rapidly scan 6 files
Score: 40 + 20 = 60

Access database_backup.sql
Score: 60 + 25 = 85

Delete 4 log files
Score: 85 + 30 = 115 → capped at 100
Level: Critical
Action: Deploy decoys + Send alert!
```

---

## 💻 Code Structure Breakdown

### The Complete Class Structure

```python
class ThreatDetector:
    __init__()              # Initialize detector
    add_event()             # Record new event
    calculate_threat_score() # Main scoring algorithm
    check_rapid_access()    # Rule 1: Rapid access
    check_unusual_time()    # Rule 2: Unusual time
    check_sensitive_files() # Rule 3: Sensitive files
    check_deletions()       # Rule 4: Deletions
    get_threat_level()      # Convert score to level
    get_threat_info()       # Get detailed info
```

---

## 🔍 Key Concepts You Learned

### 1. Scoring Algorithms

**What:**
- Multiple rules contribute points
- Total score determines action
- Each rule checks for specific pattern

**Why:**
- Single indicator might be false positive
- Multiple indicators = higher confidence
- Flexible - can add/remove rules easily

**Example:**
```python
score = 0
score += check_rapid_access()    # +0 or +20
score += check_unusual_time()    # +0 or +15
score += check_sensitive_files() # +0 or +25
score += check_deletions()       # +0 or +30
return min(score, 100)           # Cap at 100
```

---

### 2. Time-Based Analysis

**What:**
- Using timestamps to detect patterns
- `time.time()` returns seconds since 1970
- Subtract timestamps to get duration

**Why:**
- Rapid access = short time between events
- Unusual hours = specific time ranges
- Time windows = only recent events matter

**Example:**
```python
# Record event time
timestamp = time.time()  # 1707868800.123

# Later, check how long ago
current_time = time.time()  # 1707868805.456
time_ago = current_time - timestamp  # 5.333 seconds

# Is it recent?
if time_ago < 10:  # Less than 10 seconds
    # This is recent!
```

---

### 3. List Comprehensions

**What:**
- Create filtered lists in one line
- Cleaner than for loops
- Very Pythonic

**Syntax:**
```python
new_list = [item for item in old_list if condition]
```

**Examples:**
```python
# Get recent events (last 10 seconds)
recent = [e for e in self.events 
          if current_time - e['time'] < 10]

# Get only deletions
deletes = [e for e in self.events 
           if e['type'] == 'deleted']

# Get recent deletions
recent_deletes = [e for e in self.events 
                  if e['type'] == 'deleted' 
                  and current_time - e['time'] < 30]
```

---

### 4. Dictionaries for Data Storage

**What:**
- Store related data together
- Access with keys
- Like a real dictionary: word → definition

**Structure:**
```python
event = {
    'type': 'created',      # What happened
    'path': 'file.txt',     # Which file
    'time': 1707868800.123  # When it happened
}
```

**Access:**
```python
event['type']  # 'created'
event['path']  # 'file.txt'
event['time']  # 1707868800.123
```

**Why:**
- Self-documenting (keys explain values)
- Easy to add more fields later
- Can store in lists: `[event1, event2, event3]`

---

### 5. Instance Variables (self.)

**What:**
- Variables that belong to an object
- Prefixed with `self.`
- Available to all methods

**Example:**
```python
class ThreatDetector:
    def __init__(self):
        self.events = []        # Instance variable
        self.threat_score = 0   # Instance variable
    
    def add_event(self, ...):
        self.events.append(...)  # Can access here
    
    def calculate_threat_score(self):
        for event in self.events:  # And here
            ...
```

**Why:**
- Share data between methods
- Each object has its own copy
- Persistent across method calls

---

### 6. Threshold-Based Decision Making

**What:**
- Compare values to thresholds
- Different ranges trigger different actions
- Common in security systems

**Example:**
```python
if score >= 71:
    return "Critical"
elif score >= 51:
    return "Suspicious"
elif score >= 31:
    return "Elevated"
else:
    return "Normal"
```

**Why:**
- Clear decision boundaries
- Easy to adjust thresholds
- Graduated response (not just on/off)

---

## 🔗 How This Fits in Your Honeypot

### Current State (Day 9-10):
✅ **Threat detection built** - Can analyze events and calculate threat scores

### How It Will Be Used:

**Day 11-12: Integration**
```python
# In FileMonitor.on_created():
self.threat_detector.add_event("created", event.src_path)

if self.threat_detector.threat_score >= 50:
    # Deploy decoys!
```

**Day 15-18: Decoy Deployment**
```python
# When threat is suspicious or critical
if threat_level in ["Suspicious", "Critical"]:
    decoy_manager.deploy_decoys()
```

**Day 21-24: Alert System**
```python
# When threat is critical
if threat_level == "Critical":
    alert_manager.send_alert(
        f"Critical threat detected! Score: {score}"
    )
```

### The Big Picture:
```
File Monitoring (Day 3-4) ✅
    ↓
Event Logging (Day 5-6) ✅
    ↓
Threat Detection (Day 9-10) ✅
    ↓ (analyzes events, calculates scores)
Decoy Deployment (Day 15-18)
    ↓ (deploys when score > 50)
Alert System (Day 21-24)
    ↓ (alerts when score > 70)
Complete Honeypot! 🎉
```

---

## 🎓 What You Should Understand Now

After completing Day 9-10, you should be able to explain:

1. ✅ What threat detection is and why it's important
2. ✅ How scoring algorithms work (multiple rules → total score)
3. ✅ The 4 detection rules and why each is suspicious
4. ✅ How time-based analysis works (timestamps, time windows)
5. ✅ What list comprehensions are and how to use them
6. ✅ How dictionaries store event data
7. ✅ What instance variables are and why we use them
8. ✅ How threshold-based decision making works
9. ✅ The 4 threat levels and what actions they trigger
10. ✅ How this integrates with the rest of your honeypot

---

## 📚 Additional Learning Resources

### Security Concepts:
- **Intrusion Detection Systems (IDS):** Similar scoring approaches
- **SIEM Systems:** Security Information and Event Management
- **Anomaly Detection:** Identifying unusual patterns

### Python Concepts:
- **Time module:** https://docs.python.org/3/library/time.html
- **Datetime module:** https://docs.python.org/3/library/datetime.html
- **List comprehensions:** https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

### Security Best Practices:
- Balance between false positives and false negatives
- Adjust thresholds based on environment
- Log all detections for analysis
- Regularly review and update rules

---

## 🚀 Next Steps

1. **Test your code:**
   ```bash
   python src/monitor/threat_detector.py
   ```

2. **Commit your work:**
   ```bash
   git add .
   git commit -m "Day 9-10: Implemented threat detection algorithm with scoring system"
   git push
   ```

3. **Prepare for Day 11-12:** Integration with FileMonitor

---

**Congratulations on completing Day 9-10!** 🎉

You've built the intelligence layer of your honeypot system. This threat detector will make your honeypot adaptive and smart, responding to suspicious behavior automatically!

---

**Last Updated:** February 17, 2026
