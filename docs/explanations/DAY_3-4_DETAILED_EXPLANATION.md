# 📖 Day 3-4 Complete Breakdown: File Monitoring System

**Date:** February 8, 2026  
**What You Built:** File monitoring system using watchdog library  
**Files Created:** `src/monitor/file_monitor.py`

---

## 🎯 Quick Overview

**What you built:** A file monitoring system that watches folders and detects when files are created, modified, or deleted in real-time.

**Why it matters:** This is the foundation of your honeypot. Without knowing what's happening to files, you can't detect attackers or deploy decoys. This is like installing security cameras before you can catch intruders.

**Real-world use:** Security systems, backup software, cloud sync tools (like Dropbox), and antivirus programs all use file monitoring.

---

## 🧩 Part 1: The Imports (Lines 1-3)

### What you wrote:
```python
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
```

### Line 1: `from watchdog.observers import Observer`

**What it is:**
- `Observer` is a class from the watchdog library
- It's the "watcher" that monitors folders for changes

**Why we need it:**
- Without Observer, we'd have to manually check files every second (inefficient!)
- Observer runs in the background and automatically detects changes
- It's optimized and uses operating system features for efficiency

**How it works internally:**
- Uses OS-level file system notifications (Windows: ReadDirectoryChangesW, Linux: inotify)
- Runs in a separate thread so it doesn't block your program
- Continuously watches without consuming much CPU

**Real-world analogy:**
- Like a security guard who watches a building 24/7
- The guard doesn't sleep - always alert
- When something happens, the guard immediately notifies you

---

### Line 2: `from watchdog.events import FileSystemEventHandler`

**What it is:**
- `FileSystemEventHandler` is a base class that handles events
- It provides methods that run when specific events occur
- You inherit from it to customize behavior

**Why we need it:**
- Gives us pre-defined methods: `on_created`, `on_modified`, `on_deleted`, `on_moved`
- We just override the ones we care about
- Handles the complex event processing for us

**How it works:**
- When Observer detects a change, it creates an "event object"
- The event object contains info: what happened, which file, when
- Observer then calls the appropriate method on your handler

**Real-world analogy:**
- Like an alarm system with different sensors
- Door sensor → triggers door alarm
- Window sensor → triggers window alarm
- Each sensor has its own response

---

### Line 3: `import time`

**What it is:**
- Python's built-in module for time-related functions
- Provides `sleep()`, `time()`, and other time utilities

**Why we need it:**
- `time.sleep(1)` pauses execution for 1 second
- Keeps our program running without consuming CPU
- Prevents the program from ending immediately

**How it works:**
- `sleep()` tells the operating system "pause this thread"
- OS scheduler removes it from active threads
- After the time expires, OS wakes it up again

---

## 🧩 Part 2: The FileMonitor Class (Lines 5-26)

### What you wrote:
```python
class FileMonitor(FileSystemEventHandler):
    """Monitors file system for changes"""
```

### Understanding Classes

**What is a class?**
- A blueprint for creating objects
- Defines what data an object holds (attributes)
- Defines what an object can do (methods)

**Real-world analogy:**
- Class = Cookie cutter (the template)
- Object = Cookie (the actual thing)
- You can make many cookies from one cutter

### Understanding Inheritance

**What is `(FileSystemEventHandler)`?**
- FileMonitor inherits from FileSystemEventHandler
- Gets all features of FileSystemEventHandler
- Plus any new features you add

**Why inherit?**
- Don't reinvent the wheel
- FileSystemEventHandler already has the structure
- We just customize what we need

---

## 🧩 Part 3: The `__init__` Method (Lines 8-10)

### What you wrote:
```python
def __init__(self):
    super().__init__()
    print("FileMonitor initialized")
```

### Understanding `__init__`

**What is it?**
- Special method called a "constructor"
- Automatically runs when you create an object
- Sets up the object before it's used

**When does it run?**
```python
monitor = FileMonitor()  # ← __init__ runs here
```

### Understanding `super().__init__()`

**What is `super()`?**
- Gives you access to the parent class
- Lets you call methods from the parent
- Calls FileSystemEventHandler's `__init__`

**Why call it?**
- Parent class needs to set itself up
- Has its own initialization code
- Must run before adding our features

---

## 🧩 Part 4: The `on_created` Method (Lines 12-15)

### What you wrote:
```python
def on_created(self, event):
    """Called when a file is created"""
    if not event.is_directory:
        print(f"File Created: {event.src_path}")
```

### Understanding Event Methods

**What is `on_created`?**
- Runs automatically when a file is created
- Part of FileSystemEventHandler interface
- Watchdog calls it for you

**When does it run?**
- Every time a new file appears
- When you create a file manually
- When a program creates a file
- When a file is copied into the folder

### Understanding the `event` Parameter

**What's inside event?**
```python
event.src_path       # File path
event.is_directory   # True if folder, False if file
event.event_type     # "created", "modified", etc.
```

### Understanding `if not event.is_directory`

**What does this do?**
- Checks if it's a FILE (not a folder)
- `not event.is_directory` = "if it's NOT a directory"

**Why?**
- Folders also trigger events
- We only care about files
- Reduces noise in logs

---

## 🧩 Part 5: The `on_modified` Method (Lines 17-20)

### What you wrote:
```python
def on_modified(self, event):
    """Called when a file is modified"""
    if not event.is_directory:
        print(f"File Modified: {event.src_path}")
```

### When does this trigger?

**File modification includes:**
1. Content changes - Editing and saving
2. Attribute changes - Permissions, timestamps
3. Metadata changes - Sometimes renaming

**Important note:**
- Can trigger multiple times for one save
- Some programs save files in chunks
- This is normal behavior

**Why important for honeypot?**
- Attackers often modify files
- Or read files (can trigger modified)
- Helps detect suspicious activity

---

## 🧩 Part 6: The `on_deleted` Method (Lines 22-26)

### What you wrote:
```python
def on_deleted(self, event):
    """Called when a file is deleted"""
    if not event.is_directory:
        print(f"File Deleted:{event.src_path}")
```

### When does this trigger?

**File deletion includes:**
- Deleting a file
- Moving to recycle bin
- Program removing a file

**Why important for honeypot?**
- Attackers might delete log files
- Or delete evidence
- Critical security event to track

---

## 🧩 Part 7: The `start_monitoring` Function (Lines 28-48)

### What you wrote:
```python
def start_monitoring(path_to_watch):
    """Start monitoring a directory"""
```

### Why is this outside the class?

**Key difference:**
- Methods INSIDE class = actions the object can do
- Functions OUTSIDE class = helper functions that USE the class

**What does it do?**
1. Creates FileMonitor object
2. Creates Observer object
3. Connects them together
4. Starts watching
5. Keeps program running

---

## 🧩 Part 8: Creating Objects (Lines 30-34)

### What you wrote:
```python
event_handler = FileMonitor()
observer = Observer()
```

### Understanding Object Creation

**Line 1: `event_handler = FileMonitor()`**
- Creates a FileMonitor object
- Runs `__init__` method
- Prints "FileMonitor initialized"
- Stores object in `event_handler` variable

**Line 2: `observer = Observer()`**
- Creates an Observer object
- This is the watcher
- Ready to monitor folders

---

## 🧩 Part 9: Connecting Observer and Handler (Line 36)

### What you wrote:
```python
observer.schedule(event_handler, path_to_watch, recursive=True)
```

### Understanding `schedule()`

**What does it do?**
- Tells Observer what to watch
- Tells Observer who to notify
- Sets up the monitoring

**Parameters:**
1. `event_handler` - Your FileMonitor (who to notify)
2. `path_to_watch` - Folder to monitor (what to watch)
3. `recursive=True` - Watch subfolders too (how deep)

**What happens internally:**
- Observer starts monitoring the path
- When it sees a change, creates event object
- Calls appropriate method on event_handler

---

## 🧩 Part 10: Starting and Running (Lines 38-46)

### What you wrote:
```python
observer.start()
print("Monitoring Started! Press Ctrl+C to stop..")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
    print("Monitoring Stopped")

observer.join()
```

### Understanding `observer.start()`

**What does it do?**
- Starts the Observer thread
- Begins monitoring
- Returns immediately (doesn't block)

### Understanding the While Loop

**Why `while True`?**
- Creates infinite loop
- Keeps program running
- Without it, program would end

**Why `time.sleep(1)`?**
- Pauses for 1 second
- Prevents 100% CPU usage
- Gives Observer time to work

### Understanding Try-Except

**What is `try...except`?**
- Error handling structure
- `try` - run this code
- `except KeyboardInterrupt` - if Ctrl+C pressed, run this

**Why catch KeyboardInterrupt?**
- Allows graceful shutdown
- Stops Observer properly
- Prevents errors when stopping

### Understanding `observer.join()`

**What does it do?**
- Waits for Observer thread to finish
- Ensures clean shutdown
- Good practice for thread management

---

## 🧩 Part 11: The Test Code (Lines 50-57)

### What you wrote:
```python
if __name__ == "__main__":
    import os
    
    test_folder = "test_monitor"
    if not os.path.exists(test_folder):
        os.mkdir(test_folder)
        print(f"Created test folder:{test_folder}")
    
    start_monitoring(test_folder)
```

### Understanding `if __name__ == "__main__"`

**What is this?**
- Special Python check
- Only runs if you execute THIS file directly
- Doesn't run if you import this file

**Why useful?**
- Separates testing from reusable code
- Can import FileMonitor elsewhere without running test
- Professional Python practice

### Understanding the Test Logic

**Step 1: Import os**
```python
import os
```
- Imports os module for file operations
- Provides `os.path.exists()`, `os.mkdir()`, etc.

**Step 2: Check if folder exists**
```python
if not os.path.exists(test_folder):
```
- Checks if "test_monitor" folder exists
- `not os.path.exists()` = "if it doesn't exist"

**Step 3: Create folder if needed**
```python
os.mkdir(test_folder)
```
- Creates the folder
- Only runs if folder doesn't exist

**Step 4: Start monitoring**
```python
start_monitoring(test_folder)
```
- Calls our function
- Begins watching the test folder

---

## 🎯 The Big Picture: How Everything Works Together

### The Complete Flow:

1. **You run the file**
   - Python executes from top to bottom
   - Imports are loaded
   - Class is defined
   - Function is defined
   - Test code runs (because `if __name__ == "__main__"`)

2. **Test code creates folder**
   - Checks if "test_monitor" exists
   - Creates it if needed

3. **Test code calls start_monitoring()**
   - Function begins execution

4. **start_monitoring creates objects**
   - `FileMonitor()` object created
   - `Observer()` object created

5. **Objects are connected**
   - `observer.schedule()` links them
   - Observer knows to notify FileMonitor

6. **Monitoring begins**
   - `observer.start()` activates watching
   - Observer thread starts running

7. **Program waits**
   - `while True` loop keeps program alive
   - `time.sleep(1)` prevents CPU overuse

8. **You create/modify/delete files**
   - Observer detects changes
   - Creates event objects
   - Calls appropriate methods on FileMonitor

9. **FileMonitor responds**
   - `on_created()`, `on_modified()`, or `on_deleted()` runs
   - Prints message to console

10. **You press Ctrl+C**
    - KeyboardInterrupt exception raised
    - `except` block catches it
    - `observer.stop()` stops monitoring
    - `observer.join()` waits for clean shutdown
    - Program ends

---

## 💡 Key Concepts You Learned

### 1. Observer Pattern
**What it is:**
- Design pattern where one object watches another
- Subject (Observer) notifies observers (Handler) of changes
- Decouples watching from responding

**Why it's important:**
- Used everywhere in software
- GUI frameworks (button clicks)
- Event systems (game engines)
- Reactive programming

### 2. Event-Driven Programming
**What it is:**
- Code runs in response to events
- Not sequential - reactive
- Waits for things to happen

**Why it's important:**
- Modern applications are event-driven
- User interfaces
- Network servers
- Real-time systems

### 3. Inheritance
**What it is:**
- Class inherits features from parent class
- Extends or customizes parent behavior
- Code reuse

**Why it's important:**
- Don't reinvent the wheel
- Build on existing code
- Maintain consistency

### 4. Threading
**What it is:**
- Running multiple tasks concurrently
- Observer runs in separate thread
- Main program continues independently

**Why it's important:**
- Responsive applications
- Background tasks
- Parallel processing

### 5. Exception Handling
**What it is:**
- Gracefully handling errors
- `try...except` blocks
- Prevents crashes

**Why it's important:**
- Robust applications
- User-friendly error messages
- Clean shutdowns

---

## 🔗 How This Fits in Your Honeypot Project

### Current State (Day 3-4):
✅ **Foundation built** - Can detect file changes

### Next Steps:

**Day 5-6: Event Logging**
- Save events to files (not just print)
- Add timestamps
- Persistent storage

**Day 9-12: Threat Detection**
- Analyze events for suspicious patterns
- Calculate threat scores
- Decide when to respond

**Day 15-18: Decoy Deployment**
- When threat detected, create fake files
- Use file monitoring to track decoy access
- Catch attackers in the act

**Day 21-24: Alert System**
- When decoy accessed, send alerts
- Use event data to identify attacker
- Log security incidents

### The Big Picture:
```
File Monitoring (Day 3-4) ✅
    ↓
Event Logging (Day 5-6)
    ↓
Threat Detection (Day 9-12)
    ↓
Decoy Deployment (Day 15-18)
    ↓
Alert System (Day 21-24)
    ↓
Complete Honeypot! 🎉
```

---

## 📚 Additional Learning Resources

### Python Concepts:
- **Classes and Objects:** https://docs.python.org/3/tutorial/classes.html
- **Inheritance:** https://docs.python.org/3/tutorial/classes.html#inheritance
- **Exception Handling:** https://docs.python.org/3/tutorial/errors.html

### Watchdog Library:
- **Documentation:** https://python-watchdog.readthedocs.io/
- **API Reference:** https://python-watchdog.readthedocs.io/en/stable/api.html

### Design Patterns:
- **Observer Pattern:** Common in event-driven systems
- **Used by:** GUI frameworks, pub-sub systems, reactive programming

---

## 🎓 What You Should Understand Now

After reading this, you should be able to explain:

1. ✅ What the Observer pattern is and why we use it
2. ✅ How watchdog library works internally
3. ✅ What each line of code does and why
4. ✅ How inheritance works in Python
5. ✅ How event-driven programming works
6. ✅ Why we use threading for monitoring
7. ✅ How exception handling provides graceful shutdown
8. ✅ How this fits into the bigger honeypot project

---

## 🚀 Next Steps

1. **Commit your code:**
   ```bash
   git add .
   git commit -m "Day 3-4: Implemented file monitoring system"
   git push
   ```

2. **Review this document** - Make sure you understand everything

3. **Ask questions** - If anything is unclear

4. **Ready for Day 5-6** - Event Logging system!

---

**Congratulations on completing Day 3-4!** 🎉

You've built the foundation of your honeypot system. Everything else builds on this file monitoring capability!
