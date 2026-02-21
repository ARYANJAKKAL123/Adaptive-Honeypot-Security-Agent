# Day 17-18: Decoy Deployment - Detailed Explanation

**Authors:** Aryan Jakkal & Dhirayshil Sarwade  
**Date Completed:** February 20, 2026  
**Topic:** Automatic Decoy Deployment Integration

---

## 🎯 What We Built

Today we integrated the decoy system with the file monitoring system. Now when suspicious activity is detected (threat score >= 51), the system **automatically deploys decoys** to trap attackers!

---

## 📁 File Created: `src/monitor/decoy_manager.py`

### Purpose
Bridges the monitoring system (FileMonitor + ThreatDetector) with the clean architecture decoy system (DecoyService + FileDecoyGenerator).

### Why We Need DecoyManager

**Problem:** FileMonitor and ThreatDetector are in `src/monitor/`, but DecoyService is in `src/domain/application/`. We need a bridge.

**Solution:** DecoyManager sits in `src/monitor/` and uses DecoyService internally.

```
FileMonitor (Monitor Layer)
    ↓
DecoyManager (Bridge)
    ↓
DecoyService (Application Layer)
    ↓
FileDecoyGenerator (Infrastructure Layer)
```

---

## 🔍 Code Explanation

### Imports

```python
from domain.application.decoy_service import DecoyService
from domain.infrastructure.file_decoy_generator import FileDecoyGenerator
from .logger import EventLogger
import os
```

**Why these imports?**
- `DecoyService`: Business logic for decoy generation
- `FileDecoyGenerator`: Creates actual decoy files
- `EventLogger`: Logs decoy deployment events
- `os`: File system operations

---

### Class Initialization

```python
class DecoyManager:
    """
    Manages decoy deployment and tracking for the monitoring system
    Bridges FileMonitor with DecoyService (clean architecture)
    """
    
    def __init__(self, decoy_base_path="decoys"):
        """
        Initialize the decoy manager
        
        Args:
            decoy_base_path: Base directory for deploying decoys
        """
        # Create decoy generator (Infrastructure layer)
        generator = FileDecoyGenerator()
        
        # Create decoy service (Application layer)
        self.decoy_service = DecoyService(generator)
```

**What's happening:**
1. Creates `FileDecoyGenerator` (uses Faker to generate content)
2. Creates `DecoyService` and passes it the generator
3. This is **dependency injection** - DecoyService receives the generator it needs

```python
        # Set up decoy deployment path
        self.decoy_base_path = decoy_base_path
        
        # Create decoy directory if it doesn't exist
        if not os.path.exists(decoy_base_path):
            os.makedirs(decoy_base_path)
```

**Safety check:** Creates the `decoys/` directory if it doesn't exist yet.

```python
        # Initialize logger
        self.logger = EventLogger()
        self.logger.log_info(f"DecoyManager initialized - decoys will be deployed to: {decoy_base_path}")
        
        # Track if decoys have been deployed (prevent duplicate deployments)
        self.decoys_deployed = False
```

**State tracking:**
- `self.decoys_deployed`: Boolean flag to prevent deploying decoys multiple times
- Once decoys are deployed, this becomes `True`

---

### Method 1: deploy_for_threat()

```python
    def deploy_for_threat(self, threat_score, threat_level, trigger_path):
        """
        Deploy decoys based on threat level
        
        Args:
            threat_score: Current threat score (0-100)
            threat_level: Threat level category
            trigger_path: File path that triggered the threat
            
        Returns:
            List of deployed Decoy objects, or None if no deployment
        """
```

**Purpose:** Decides whether to deploy decoys and executes deployment.

```python
        # Only deploy for Suspicious (51-70) or Critical (71-100)
        if threat_score < 51:
            return None
```

**Business Rule:** Only deploy decoys when threat is serious enough (score >= 51).

**Why 51?**
- 0-30: Normal - no action needed
- 31-50: Elevated - just watch
- 51-70: Suspicious - deploy decoys!
- 71-100: Critical - deploy more decoys!

```python
        # Prevent duplicate deployments
        if self.decoys_deployed:
            return None
```

**Duplicate prevention:** If decoys already deployed, don't deploy again.

**Why?** Deploying multiple times would:
- Create duplicate files
- Waste resources
- Confuse the tracking system

```python
        # Deploy decoys using DecoyService
        self.logger.log_warning(
            f"Deploying decoys for {threat_level} threat (Score: {threat_score}) "
            f"triggered by: {trigger_path}"
        )
        
        decoys = self.decoy_service.generate_decoys_for_threat_level(
            threat_level, 
            self.decoy_base_path
        )
```

**Deployment:**
1. Log the deployment event
2. Call `DecoyService.generate_decoys_for_threat_level()`
3. DecoyService decides how many decoys (2 for Suspicious, 4 for Critical)
4. Returns list of Decoy objects

```python
        # Mark as deployed
        self.decoys_deployed = True
        
        # Log deployment details
        self.logger.log_warning(
            f"✅ Deployed {len(decoys)} decoy(s): " +
            ", ".join([os.path.basename(d.file_path) for d in decoys])
        )
        
        return decoys
```

**After deployment:**
1. Set flag to `True` (prevents future deployments)
2. Log which decoys were created
3. Return the list of decoys

---

### Method 2: track_decoy_access()

```python
    def track_decoy_access(self, file_path, event_type, threat_level, threat_score):
        """
        Check if accessed file is a decoy and log if attacker caught
        
        Args:
            file_path: Path of accessed file
            event_type: Type of access (created, modified, deleted)
            threat_level: Current threat level
            threat_score: Current threat score
        """
```

**Purpose:** Detect when an attacker accesses a decoy file.

```python
        # Check if this file is a deployed decoy
        if self.decoy_service.is_decoy_file(file_path):
            self.logger.log_error(
                f"🚨 ATTACKER CAUGHT! Decoy accessed: {file_path} | "
                f"Event: {event_type} | Threat: {threat_level} ({threat_score})"
            )
            return True
        
        return False
```

**How it works:**
1. Ask DecoyService: "Is this file path a decoy?"
2. If YES → Log critical alert "ATTACKER CAUGHT!"
3. If NO → Return False (normal file)

**Why this is important:**
- Confirms attacker is actively searching for sensitive files
- Provides evidence of malicious activity
- Triggers alert system (coming in Day 21-22)

---

### Method 3: get_deployment_status()

```python
    def get_deployment_status(self):
        """
        Get current decoy deployment status
        
        Returns:
            Dictionary with deployment information
        """
        deployed_decoys = self.decoy_service.get_deployed_decoys()
        
        return {
            'deployed': self.decoys_deployed,
            'count': len(deployed_decoys),
            'decoys': deployed_decoys,
            'base_path': self.decoy_base_path
        }
```

**Purpose:** Get information about deployed decoys.

**Returns:**
- `deployed`: Boolean - are decoys deployed?
- `count`: Number of deployed decoys
- `decoys`: List of Decoy objects
- `base_path`: Where decoys are stored

**Use cases:**
- Testing
- Dashboard display (future)
- Debugging

---

## 🔗 Integration with FileMonitor

### Updated FileMonitor

```python
class FileMonitor(FileSystemEventHandler):
    def __init__(self):
        super().__init__()
        self.logger = EventLogger()
        self.threat_detector = ThreatDetector()
        self.decoy_manager = DecoyManager()  # ← NEW!
```

**What changed:** Added `DecoyManager` instance.

### Event Handling Flow

```python
    def _handle_file_event(self, event_type, file_path, event_label):
        """Analyze file events and trigger decoy deployment when needed."""
        self.logger.log_info(f"{event_label}: {file_path}")

        # Step 1: Add event to threat detector
        self.threat_detector.add_event(event_type, file_path)
        threat_level = self.threat_detector.get_threat_level()
        threat_score = self.threat_detector.threat_score

        # Step 2: Log if threat detected
        if threat_score >= 31:
            self.logger.log_warning(
                f"Threat Level: {threat_level} (Score: {threat_score}) - File: {file_path}"
            )

        # Step 3: Deploy decoys if needed
        deployed = self.decoy_manager.deploy_for_threat(
            threat_score=threat_score,
            threat_level=threat_level,
            trigger_path=file_path,
        )
        if deployed:
            self.logger.log_warning(
                f"Decoy deployment triggered by {file_path}: {len(deployed)} decoy(s) created"
            )

        # Step 4: Check if accessed file is a decoy
        self.decoy_manager.track_decoy_access(
            file_path=file_path,
            event_type=event_type,
            threat_level=threat_level,
            threat_score=threat_score,
        )
```

**Complete Flow:**
1. File event occurs (created/modified/deleted)
2. ThreatDetector analyzes and calculates score
3. If score >= 31, log warning
4. If score >= 51, deploy decoys
5. Check if accessed file is a decoy
6. If decoy accessed, log "ATTACKER CAUGHT!"

---

## 🧪 Testing

### Test File: `test_integrated_system.py`

**What it tests:**

**Step 1: Initialize System**
```python
file_monitor = FileMonitor()
# Creates: FileMonitor → ThreatDetector → DecoyManager → DecoyService → FileDecoyGenerator
```

**Step 2: Normal Activity (Score < 51)**
```python
# Create 2 normal files
for i in range(2):
    event = MockEvent(f"{test_dir}/normal_file_{i}.txt")
    file_monitor.on_created(event)

# Result: No decoys deployed (score too low)
```

**Step 3: Suspicious Activity (Score >= 51)**
```python
# Access sensitive files rapidly
sensitive_files = [
    "passwords.txt",
    "api_keys.txt",
    "secret_token.txt",
    "database_config.yaml",
    "admin_credentials.txt"
]

for file_path in sensitive_files:
    file_monitor.on_created(MockEvent(file_path))

# Result: Threat score increases, decoys deployed!
```

**Step 4: Check Deployment**
```python
status = file_monitor.decoy_manager.get_deployment_status()
print(f"Decoys Deployed: {status['deployed']}")
print(f"Number of Decoys: {status['count']}")

# Result: Shows deployed decoys
```

**Step 5: Simulate Attacker**
```python
# Access a deployed decoy
decoy_path = status['decoys'][0].file_path
file_monitor.on_modified(MockEvent(decoy_path))

# Result: Logs "🚨 ATTACKER CAUGHT!"
```

**Step 6: Verify Files**
```python
files = os.listdir("decoys")
# Result: Shows actual decoy files created on disk
```

---

## 🎯 Key Concepts Learned

### 1. System Integration
Connecting multiple components to work together:
- FileMonitor (monitoring)
- ThreatDetector (analysis)
- DecoyManager (bridge)
- DecoyService (business logic)
- FileDecoyGenerator (implementation)

### 2. Bridge Pattern
DecoyManager acts as a bridge between:
- Monitoring layer (`src/monitor/`)
- Domain layer (`src/domain/`)

### 3. Automatic Response
System responds automatically to threats:
- No human intervention needed
- Real-time deployment
- Immediate detection

### 4. State Management
Tracking deployment state:
- `self.decoys_deployed` flag
- Prevents duplicate deployments
- Maintains system consistency

### 5. Defensive Programming
Safety checks:
- Check if directory exists before creating
- Prevent duplicate deployments
- Validate threat score threshold

---

## 🔄 Complete System Flow

```
1. Attacker creates/modifies files rapidly
   ↓
2. FileMonitor detects events
   ↓
3. ThreatDetector calculates score
   ↓
4. Score reaches 51+ (Suspicious)
   ↓
5. DecoyManager.deploy_for_threat() called
   ↓
6. DecoyService decides: 2 decoys for Suspicious
   ↓
7. FileDecoyGenerator creates fake files using Faker
   ↓
8. Decoys written to decoys/ directory
   ↓
9. DecoyManager tracks deployed decoys
   ↓
10. Attacker accesses decoy file
   ↓
11. FileMonitor detects access
   ↓
12. DecoyManager.track_decoy_access() called
   ↓
13. Identifies file as decoy
   ↓
14. Logs "🚨 ATTACKER CAUGHT!"
   ↓
15. Alert system triggered (Day 21-22)
```

---

## 💡 Real-World Analogy

**Think of it like a security system:**

1. **FileMonitor** = Security cameras watching your house
2. **ThreatDetector** = AI analyzing camera footage for suspicious behavior
3. **DecoyManager** = Security guard who decides when to set traps
4. **DecoyService** = Trap designer who plans what traps to use
5. **FileDecoyGenerator** = Worker who actually builds the traps
6. **Decoys** = Fake valuables (bait) to catch burglars

When the AI detects suspicious behavior (score >= 51), the security guard automatically deploys traps. When the burglar touches a trap, the system knows they're caught!

---

## 🚀 What's Next (Day 19-20)

Now that decoys are deployed, we need to:
1. **Track decoy access more thoroughly**
2. **Capture attacker information** (IP, timestamp, actions)
3. **Log detailed attack patterns**
4. **Prepare for alert system** (Day 21-22)

---

## 📊 Project Status

**Completed:**
- ✅ File monitoring (Day 3-4)
- ✅ Event logging (Day 5-6)
- ✅ Threat detection (Day 9-10)
- ✅ System integration (Day 11-12)
- ✅ Decoy generation (Day 15-16)
- ✅ Decoy deployment (Day 17-18)

**Next:**
- ⏳ Decoy tracking (Day 19-20)
- ⏳ Alert system (Day 21-22)

**Progress:** 32% complete (18/56 days)

---

## 🎉 Congratulations!

You've built an **adaptive security system** that:
- ✅ Monitors files in real-time
- ✅ Detects suspicious behavior
- ✅ Automatically deploys decoys
- ✅ Catches attackers red-handed

**This is professional-grade security software!** 🛡️

---

**Next:** Day 19-20 - Decoy Tracking (detailed attack logging)
