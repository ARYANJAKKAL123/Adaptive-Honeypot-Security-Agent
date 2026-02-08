# 📖 Day 5-6 Complete Breakdown: Event Logging System

**Date:** February 8, 2026  
**What You Built:** Event logging system with timestamps and log levels  
**Files Created:** `src/monitor/logger.py`, updated `src/monitor/file_monitor.py`

---

## 🎯 Quick Overview

**What you built:** A professional logging system that saves file events to a file with timestamps and severity levels.

**Why it matters:** 
- Console output disappears when you close the program
- Logs provide permanent records for later analysis
- Timestamps tell you exactly when events happened
- Log levels help categorize events by importance
- Essential for security monitoring and threat detection

**Real-world use:** Every professional application uses logging - web servers, databases, security systems, operating systems all maintain detailed logs.

---

## 📚 PART 1: Understanding Logging

### What is Logging?

**Simple definition:**
Logging is the practice of recording events, errors, and information about what your program is doing to a file or other storage.

**Real-world analogies:**
- **Security camera footage** - Visual log of what happened
- **Ship's logbook** - Written record of voyage events
- **Medical records** - Log of patient history and treatments
- **Black box recorder** - Aircraft event log for investigation

**Why not just use print()?**

| Feature | print() | Logging |
|---------|---------|---------|
| Permanent | ❌ Disappears | ✅ Saved to file |
| Timestamps | ❌ No | ✅ Automatic |
| Levels | ❌ No | ✅ INFO, WARNING, ERROR |
| Searchable | ❌ No | ✅ Yes |
| Professional | ❌ No | ✅ Yes |
| Thread-safe | ❌ No | ✅ Yes |

---

## 📚 PART 2: Understanding Log Levels

### The 5 Standard Log Levels

**1. DEBUG (Level 10) - Most Detailed**
- For developers during development
- Very detailed diagnostic information
- Usually disabled in production
- Example: "Variable x = 5", "Entering function calculate()"

**2. INFO (Level 20) - Informational**
- Confirms things are working as expected
- General informational messages
- Normal operations
- Example: "Server started", "File created: test.txt"

**3. WARNING (Level 30) - Potential Issues**
- Something unexpected but not critical
- Program continues normally
- Should be investigated
- Example: "Disk space low", "Deprecated function used"

**4. ERROR (Level 40) - Serious Problems**
- Something failed
- Functionality affected
- Needs attention
- Example: "Failed to save file", "Database connection lost"

**5. CRITICAL (Level 50) - System Failure**
- Very serious error
- Program might crash
- Immediate action required
- Example: "Out of memory", "System failure imminent"

### For Our Honeypot

We use three levels:
- **INFO** - Normal file events (created, modified, deleted)
- **WARNING** - Suspicious patterns (will use later for threat detection)
- **ERROR** - System errors (can't write log, file access denied)

---

## 🧩 PART 3: The EventLogger Class - Line by Line

### The Imports (Lines 1-3)

```python
import logging
import os
from datetime import datetime
```

**Line 1: `import logging`**
- Python's built-in logging module
- No installation needed (part of standard library)
- Provides all logging functionality
- Thread-safe and production-ready

**What logging module provides:**
- Automatic timestamp formatting
- Log level filtering
- Multiple output destinations (file, console, network)
- Configurable formatting
- Thread-safe operations

**Line 2: `import os`**
- Operating system interface module
- Provides file and directory operations
- We use it to create the logs directory
- Cross-platform (works on Windows, Mac, Linux)

**Functions we use:**
- `os.path.dirname()` - Extract directory from path
- `os.path.exists()` - Check if path exists
- `os.makedirs()` - Create directories (including nested)

**Line 3: `from datetime import datetime`**
- For working with dates and times
- More flexible than logging's default timestamps
- Can format dates in custom ways
- Useful for future enhancements

---

### The Class Definition (Line 5)

```python
class EventLogger:
    """
    Handles logging of file system events
    Writes events to logs/events.log with timestamps
    """
```

**Why create a class?**
1. **Encapsulation** - Groups related functionality together
2. **Reusability** - Can create multiple loggers if needed
3. **Maintainability** - Easy to modify and extend
4. **Professional** - Standard practice in software development

**What this class does:**
- Configures Python's logging system
- Provides simple methods to log events
- Handles file creation and directory setup
- Formats log messages consistently

---

### The __init__ Method - Part 1: Setup (Lines 9-17)

```python
def __init__(self, log_file='logs/events.log'):
    """
    Initialize the event logger
    
    Args:
        log_file: Path to the log file (default: logs/events.log)
    """
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)
```

**Understanding the parameter:**

**`log_file='logs/events.log'`**
- This is a "default parameter"
- If you don't specify a file, it uses this default
- Allows flexibility for different log files

**Examples:**
```python
# Using default:
logger = EventLogger()  
# Uses: logs/events.log

# Custom file:
logger = EventLogger('logs/security.log')  
# Uses: logs/security.log

# Different directory:
logger = EventLogger('app_logs/events.log')  
# Uses: app_logs/events.log
```

**Line: `log_dir = os.path.dirname(log_file)`**

**What `os.path.dirname()` does:**
- Extracts the directory part of a path
- Removes the filename, keeps the folder

**Examples:**
```python
os.path.dirname('logs/events.log')  # Returns: 'logs'
os.path.dirname('a/b/c/file.txt')   # Returns: 'a/b/c'
os.path.dirname('file.txt')         # Returns: '' (empty)
```

**Line: `if log_dir and not os.path.exists(log_dir):`**

**Breaking it down:**
1. `if log_dir` - Check if directory path is not empty
2. `and` - Both conditions must be true
3. `not os.path.exists(log_dir)` - Check if directory doesn't exist

**Why both checks?**
- If `log_file='events.log'` (no directory), `log_dir` is empty string
- Empty string is "falsy" in Python, so first check fails
- Prevents trying to create an empty directory

**Line: `os.makedirs(log_dir)`**

**What `makedirs()` does:**
- Creates directory and all parent directories
- Like `mkdir -p` in Linux

**Difference from `mkdir()`:**
```python
# mkdir() - Only creates one level
os.mkdir('logs')  # ✅ Works if parent exists
os.mkdir('logs/subfolder/deep')  # ❌ Fails if parents don't exist

# makedirs() - Creates all levels
os.makedirs('logs/subfolder/deep')  # ✅ Creates all three
```

---

### The __init__ Method - Part 2: Configuration (Lines 19-28)

```python
    self.log_file = log_file
    
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    self.logger = logging.getLogger(__name__)
```

**Line: `self.log_file = log_file`**

**What is `self.`?**
- `self` refers to the current object instance
- `self.log_file` is an instance variable
- Stores data that belongs to this specific object
- Can be accessed by any method in the class

**Example:**
```python
logger1 = EventLogger('logs/app1.log')
logger2 = EventLogger('logs/app2.log')

# Each has its own log_file:
logger1.log_file  # 'logs/app1.log'
logger2.log_file  # 'logs/app2.log'
```

**Line: `logging.basicConfig(...)`**

**What is basicConfig()?**
- Configures the root logger
- Should only be called once in your program
- Sets up how all logging will work
- Simple way to configure logging

**Parameter: `filename=log_file`**
- Where to write log messages
- Creates file if it doesn't exist
- Appends to file if it exists (doesn't overwrite)

**Parameter: `level=logging.INFO`**
- Minimum severity level to log
- INFO and above will be logged (INFO, WARNING, ERROR, CRITICAL)
- DEBUG messages will be ignored

**Why INFO level?**
- DEBUG is too verbose for production
- INFO captures normal operations
- Still see warnings and errors
- Good balance for monitoring

**Parameter: `format='%(asctime)s - %(levelname)s - %(message)s'`**

**Understanding format strings:**
- Template for how log messages look
- `%(...)s` are placeholders that get replaced

**Placeholders explained:**
- `%(asctime)s` - Timestamp when event occurred
- `%(levelname)s` - Log level (INFO, WARNING, ERROR)
- `%(message)s` - Your actual message
- `-` - Literal dash separator

**Example output:**
```
2026-02-08 14:30:45 - INFO - File created: test.txt
2026-02-08 14:30:50 - WARNING - Suspicious activity
2026-02-08 14:31:00 - ERROR - Failed to write file
```

**Other available placeholders:**
- `%(filename)s` - Source file name
- `%(lineno)d` - Line number
- `%(funcName)s` - Function name
- `%(process)d` - Process ID
- `%(thread)d` - Thread ID

**Parameter: `datefmt='%Y-%m-%d %H:%M:%S'`**

**Understanding date format codes:**
- `%Y` - 4-digit year (2026)
- `%m` - 2-digit month (01-12)
- `%d` - 2-digit day (01-31)
- `%H` - Hour in 24-hour format (00-23)
- `%M` - Minute (00-59)
- `%S` - Second (00-59)

**Examples:**
```python
'%Y-%m-%d %H:%M:%S'  # 2026-02-08 14:30:45
'%d/%m/%Y %I:%M %p'  # 08/02/2026 02:30 PM
'%B %d, %Y'          # February 08, 2026
```

**Line: `self.logger = logging.getLogger(__name__)`**

**What is `getLogger()`?**
- Gets a logger instance
- Can have multiple loggers in one program
- Each logger can have different settings

**What is `__name__`?**
- Special Python variable
- Contains the module name
- For `logger.py`, `__name__` is `'logger'`
- Helps identify which module logged the message

**Why store in `self.logger`?**
- Makes it available to all methods in the class
- Don't need to call `getLogger()` every time
- More efficient

---

## 🧩 PART 4: The Logging Methods

### The log_info() Method (Lines 30-36)

```python
def log_info(self, message):
    """
    Log an informational message
    
    Args:
        message: The message to log
    """
    self.logger.info(message)
```

**Method breakdown:**

**`def log_info(self, message):`**
- `self` - Reference to the object (always first parameter in methods)
- `message` - The text you want to log

**`self.logger.info(message)`**
- Calls the `info()` method on the logger
- Writes message at INFO level
- Automatically adds timestamp and formatting

**How it works internally:**
1. You call: `logger.log_info("File created")`
2. Method calls: `self.logger.info("File created")`
3. Logging module checks: Is INFO >= configured level? (Yes, INFO >= INFO)
4. Logging module formats: `2026-02-08 14:30:45 - INFO - File created`
5. Logging module writes to file: `logs/events.log`

**Usage examples:**
```python
logger = EventLogger()

# Log normal events
logger.log_info("Application started")
logger.log_info("File created: test.txt")
logger.log_info("User logged in: john")
logger.log_info("Processing complete")
```

**What gets written:**
```
2026-02-08 14:30:00 - INFO - Application started
2026-02-08 14:30:05 - INFO - File created: test.txt
2026-02-08 14:30:10 - INFO - User logged in: john
2026-02-08 14:30:15 - INFO - Processing complete
```

---

### The log_warning() Method (Lines 38-44)

```python
def log_warning(self, message):
    """
    Log a warning message
    
    Args:
        message: The warning message to log
    """
    self.logger.warning(message)
```

**Same structure as log_info(), but:**
- Uses WARNING level instead of INFO
- For suspicious or unusual events
- Indicates potential problems

**When to use:**
- Unusual but not critical situations
- Deprecated features being used
- Resource limits approaching
- Suspicious patterns detected

**Usage examples:**
```python
logger.log_warning("Disk space below 10%")
logger.log_warning("Multiple failed login attempts")
logger.log_warning("Unusual file access pattern detected")
logger.log_warning("API rate limit approaching")
```

**For our honeypot (future use):**
```python
# When threat score is elevated but not critical
logger.log_warning("Suspicious activity: rapid file scanning")
logger.log_warning("Unusual access time: 3 AM")
logger.log_warning("Multiple files accessed in short time")
```

---

### The log_error() Method (Lines 46-52)

```python
def log_error(self, message):
    """
    Log an error message
    
    Args:
        message: The error message to log
    """
    self.logger.error(message)
```

**Same structure, but:**
- Uses ERROR level
- For actual failures and errors
- Indicates something went wrong

**When to use:**
- Operations that failed
- Exceptions caught
- System errors
- Data corruption

**Usage examples:**
```python
logger.log_error("Failed to save file: permission denied")
logger.log_error("Database connection lost")
logger.log_error("Invalid configuration file")
logger.log_error("Out of memory")
```

**For our honeypot:**
```python
# System errors
logger.log_error("Failed to create log directory")
logger.log_error("Cannot write to log file")
logger.log_error("Watchdog observer crashed")
```

---

## 🧩 PART 5: Integration with FileMonitor

### Adding the Import (Line 4 in file_monitor.py)

```python
from .logger import EventLogger
```

**Understanding relative imports:**

**The dot (`.`) means:**
- "From the same package"
- We're in `src/monitor/file_monitor.py`
- Logger is in `src/monitor/logger.py`
- Same directory = same package

**Why use relative import?**
- Cleaner than absolute imports
- Works regardless of how package is installed
- Standard practice for same-package imports

**Absolute vs Relative:**
```python
# Relative (what we use):
from .logger import EventLogger

# Absolute (also works):
from src.monitor.logger import EventLogger
```

**What gets imported:**
- The `EventLogger` class
- Can now create EventLogger objects
- `from X import Y` means "import Y from module X"

---

### Creating Logger Instance (In FileMonitor.__init__)

**Before:**
```python
def __init__(self):
    super().__init__()
    print("FileMonitor initialized")
```

**After:**
```python
def __init__(self):
    super().__init__()
    self.logger = EventLogger()
    self.logger.log_info("FileMonitor initialized")
```

**What changed:**

**Line: `self.logger = EventLogger()`**
- Creates an EventLogger object
- Stores it as instance variable
- Now available to all methods via `self.logger`

**Why `self.logger`?**
- Makes logger available to all methods in FileMonitor
- `on_created()`, `on_modified()`, `on_deleted()` can all use it
- Without `self.`, only `__init__` could access it

**Line: `self.logger.log_info("FileMonitor initialized")`**
- Replaces `print()` statement
- Logs to file instead of console
- Includes timestamp automatically

**What happens:**
1. `EventLogger()` is created
2. EventLogger creates logs directory if needed
3. EventLogger configures logging
4. "FileMonitor initialized" is logged to file
5. Logger is stored in `self.logger` for future use

---

### Updating Event Methods

**Pattern for all three methods:**

**Before (on_created):**
```python
def on_created(self, event):
    if not event.is_directory:
        print(f"File Created: {event.src_path}")
```

**After (on_created):**
```python
def on_created(self, event):
    if not event.is_directory:
        self.logger.log_info(f"File Created: {event.src_path}")
```

**What changed:**
- `print()` → `self.logger.log_info()`
- Same message format
- Different destination (file vs console)

**Why this works:**
1. `self.logger` was created in `__init__`
2. It's an instance variable, so all methods can access it
3. `log_info()` writes to file with timestamp
4. Message format stays the same

**Same pattern for all three:**
- `on_created()` → `self.logger.log_info()`
- `on_modified()` → `self.logger.log_info()`
- `on_deleted()` → `self.logger.log_info()`

---

## 🎯 The Complete Flow

### When You Run file_monitor.py:

**Step 1: Imports are loaded**
```python
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
from .logger import EventLogger  # ← Logger is imported
```

**Step 2: Classes are defined**
- FileMonitor class definition is read
- EventLogger class definition is read (from logger.py)
- No code executes yet, just definitions

**Step 3: Test code runs**
```python
if __name__ == "__main__":
    # Creates test folder
    # Calls start_monitoring()
```

**Step 4: start_monitoring() creates FileMonitor**
```python
event_handler = FileMonitor()  # ← __init__ runs here
```

**Step 5: FileMonitor.__init__() runs**
```python
def __init__(self):
    super().__init__()              # 1. Initialize parent class
    self.logger = EventLogger()     # 2. Create logger
    self.logger.log_info("...")     # 3. Log initialization
```

**Step 6: EventLogger.__init__() runs**
```python
def __init__(self, log_file='logs/events.log'):
    log_dir = os.path.dirname(log_file)     # 1. Get directory
    if log_dir and not os.path.exists(...): # 2. Check if exists
        os.makedirs(log_dir)                # 3. Create if needed
    
    self.log_file = log_file                # 4. Store path
    logging.basicConfig(...)                # 5. Configure logging
    self.logger = logging.getLogger(...)    # 6. Get logger
```

**Step 7: Observer starts watching**
- FileMonitor is ready with logger
- Observer begins monitoring folder
- Waits for file events

**Step 8: File event occurs**
- You create a file: `test.txt`
- Observer detects it
- Observer calls `event_handler.on_created(event)`

**Step 9: on_created() runs**
```python
def on_created(self, event):
    if not event.is_directory:
        self.logger.log_info(f"File Created: {event.src_path}")
```

**Step 10: log_info() writes to file**
```python
def log_info(self, message):
    self.logger.info(message)  # ← Writes to logs/events.log
```

**Step 11: Logging module does its magic**
1. Checks level: INFO >= INFO? Yes
2. Formats message: `2026-02-08 14:30:45 - INFO - File Created: test.txt`
3. Writes to file: `logs/events.log`
4. Returns control to your program

---

## 💡 Key Concepts You Learned

### 1. Logging vs Printing

**Printing:**
- Temporary output
- No timestamps
- No levels
- Disappears when terminal closes

**Logging:**
- Permanent records
- Automatic timestamps
- Severity levels
- Saved to files
- Professional standard

### 2. Log Levels

**Purpose:**
- Categorize events by importance
- Filter what you want to see
- Standard across all languages

**The hierarchy:**
```
DEBUG < INFO < WARNING < ERROR < CRITICAL
```

**When level is set to INFO:**
- DEBUG messages ignored
- INFO and above logged

### 3. Python's Logging Module

**Key components:**
- **Logger** - Main object that logs messages
- **Handler** - Where to send logs (file, console, etc.)
- **Formatter** - How to format messages
- **Level** - Minimum severity to log

**Configuration:**
- `basicConfig()` - Simple setup
- `getLogger()` - Get logger instance
- `info()`, `warning()`, `error()` - Log at different levels

### 4. Instance Variables (self.)

**What they are:**
- Variables that belong to an object
- Prefixed with `self.`
- Available to all methods in the class

**Example:**
```python
class MyClass:
    def __init__(self):
        self.data = "Hello"  # Instance variable
    
    def print_data(self):
        print(self.data)     # Can access it here
```

### 5. Relative Imports

**Syntax:**
- `.module` - Same package
- `..module` - Parent package
- `...module` - Grandparent package

**When to use:**
- Importing from same package
- Cleaner than absolute imports
- Standard practice

### 6. Default Parameters

**Syntax:**
```python
def function(param='default_value'):
    ...
```

**Benefits:**
- Optional parameters
- Flexibility
- Backward compatibility

**Example:**
```python
def greet(name='World'):
    print(f"Hello, {name}!")

greet()          # Hello, World!
greet('Alice')   # Hello, Alice!
```

---

## 🔗 How This Fits in Your Honeypot

### Current State (Day 5-6):
✅ **Logging system built** - All events saved to file

### How It's Used Now:
- File created → Logged with timestamp
- File modified → Logged with timestamp
- File deleted → Logged with timestamp

### How It Will Be Used Later:

**Day 9-12: Threat Detection**
```python
# When suspicious activity detected
logger.log_warning("Threat score elevated: 75")
logger.log_warning("Rapid file scanning detected")
```

**Day 15-18: Decoy Deployment**
```python
# When decoys are deployed
logger.log_info("Decoy deployed: fake_passwords.txt")
logger.log_warning("Decoy accessed by attacker!")
```

**Day 21-24: Alert System**
```python
# When alerts are sent
logger.log_info("Alert sent: Decoy accessed")
logger.log_error("Failed to send alert: SMTP error")
```

### The Big Picture:
```
File Monitoring (Day 3-4) ✅
    ↓
Event Logging (Day 5-6) ✅
    ↓
Threat Detection (Day 9-12)
    ↓ (uses logs to analyze patterns)
Decoy Deployment (Day 15-18)
    ↓ (logs decoy activity)
Alert System (Day 21-24)
    ↓ (logs alerts sent)
Complete Honeypot! 🎉
```

---

## 🎓 What You Should Understand Now

After reading this, you should be able to explain:

1. ✅ What logging is and why it's better than print()
2. ✅ The 5 log levels and when to use each
3. ✅ How Python's logging module works
4. ✅ What basicConfig() does and its parameters
5. ✅ How to create a logger class
6. ✅ What instance variables (self.) are and why we use them
7. ✅ How relative imports work
8. ✅ How to integrate logging with existing code
9. ✅ The complete flow from file event to log entry
10. ✅ How this fits into the bigger honeypot project

---

## 📚 Additional Learning Resources

### Python Logging:
- **Official Docs:** https://docs.python.org/3/library/logging.html
- **Logging HOWTO:** https://docs.python.org/3/howto/logging.html
- **Logging Cookbook:** https://docs.python.org/3/howto/logging-cookbook.html

### Best Practices:
- Use appropriate log levels
- Include context in messages
- Don't log sensitive data (passwords, keys)
- Rotate log files to prevent huge files
- Use structured logging for complex applications

### Advanced Topics (For Later):
- Log rotation (limiting file size)
- Multiple handlers (file + console)
- Custom formatters
- Logging exceptions with traceback
- Structured logging (JSON format)

---

## 🚀 Next Steps

1. **Review this document** - Make sure you understand everything

2. **Experiment** - Try different log levels and formats

3. **Read the logs** - Open `logs/events.log` and see your work

4. **Prepare for Day 7-8** - Testing & Bug Fixes

---

**Congratulations on completing Day 5-6!** 🎉

You now have a professional logging system that will serve as the foundation for all future monitoring and security features!

---

**Last Updated:** February 8, 2026
