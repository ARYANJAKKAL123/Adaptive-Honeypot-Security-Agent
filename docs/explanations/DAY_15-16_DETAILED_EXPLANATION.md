# Day 15-16: Decoy File Generator - Detailed Explanation

**Authors:** Aryan Jakkal & Dhirayshil Sarwade  
**Date Completed:** February 20, 2026  
**Topic:** Clean Architecture Implementation for Decoy System

---

## 🎯 What We Built

Today we implemented a complete **Decoy File Generator** using **Clean Architecture** principles. This system generates realistic fake files (credentials, documents, configs) to trap attackers when suspicious activity is detected.

---

## 🏗️ Clean Architecture Overview

### Why Clean Architecture?

**Problem:** If we build the decoy system without clean architecture, adding a UI later would require massive refactoring.

**Solution:** Separate business logic (Domain) from technical implementation (Infrastructure) so the UI can plug in easily.

### The Three Layers

```
┌─────────────────────────────────────┐
│   UI Layer (Future - Week 5-6)     │
│   Web Dashboard, CLI, API           │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│   Application Layer                 │
│   DecoyService - Business Logic     │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│   Domain Layer                      │
│   Entities + Interfaces             │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│   Infrastructure Layer              │
│   FileDecoyGenerator - Faker, Files │
└─────────────────────────────────────┘
```

---

## 📁 File 1: Domain Entity - `src/domain/entities/decoy.py`

### Purpose
Defines WHAT a decoy IS - the core business object with no external dependencies.

### Code Explanation

```python
from dataclasses import dataclass
from datetime import datetime
```
**Why dataclass?** Automatically generates `__init__`, `__repr__`, `__eq__` methods - less boilerplate code.

```python
@dataclass
class Decoy:
    """
    Represents a decoy file in the honeypot system
    This is a pure business entity with no external dependencies
    """
    decoy_type: str      # Type: "credential", "document", "config", etc.
    file_path: str       # Where the decoy is placed
    content: str         # The fake content inside the decoy
    created_at: datetime # When the decoy was created
```

**Properties Explained:**
- `decoy_type`: Categorizes the decoy (credential, document, config)
- `file_path`: Full path where the decoy file is located
- `content`: The actual fake content (passwords, documents, etc.)
- `created_at`: Timestamp for tracking when decoy was deployed

**Key Principle:** NO external dependencies! Only uses Python standard library (`dataclasses`, `datetime`).

**Real-World Analogy:** This is like a blueprint for a house. It describes what a house should have (rooms, doors, windows) but doesn't explain how to build it or what materials to use.

---

## 📁 File 2: Domain Interface - `src/domain/interfaces/decoy_generator.py`

### Purpose
Defines HOW decoys SHOULD be generated - the contract that any implementation must follow.

### Code Explanation

```python
from abc import ABC, abstractmethod
from ..entities.decoy import Decoy
```
**Why ABC?** Abstract Base Class - ensures any subclass MUST implement the abstract methods.

```python
class IDecoyGenerator(ABC):
    """
    Interface that defines how decoys should be generated
    Any class that generates decoys must implement these methods
    """
```

**Naming Convention:** `I` prefix = Interface (common in clean architecture)

```python
    @abstractmethod
    def create_credential_decoy(self, file_path: str) -> Decoy:
        """
        Generate a fake credential file (passwords, keys, etc.)
        
        Args:
            file_path: Where to place the decoy file
            
        Returns:
            Decoy object with fake credential content
        """
        pass
```

**@abstractmethod:** Forces any class that inherits from `IDecoyGenerator` to implement this method.

**Why 3 methods?**
1. `create_credential_decoy()` - Passwords, API keys, tokens
2. `create_document_decoy()` - Reports, notes, financial data
3. `create_config_decoy()` - Database configs, server settings

**Key Principle:** Defines the contract but doesn't implement anything. Just says "you MUST have these methods."

**Real-World Analogy:** This is like a job description. It says "any decoy generator must be able to create credentials, documents, and configs" but doesn't say HOW to do it.

---

## 📁 File 3: Application Service - `src/domain/application/decoy_service.py`

### Purpose
Orchestrates decoy operations - contains the business logic for WHEN and WHAT decoys to deploy.

### Code Explanation

```python
from ..interfaces.decoy_generator import IDecoyGenerator
from ..entities.decoy import Decoy
from typing import List
```

**Relative imports:** `..` means go up one directory level (from `application/` to `domain/`)

```python
class DecoyService:
    """
    Orchestrates decoy operations based on threat levels
    Contains business logic for when and what decoys to deploy
    """
    
    def __init__(self, decoy_generator: IDecoyGenerator):
        """
        Initialize the decoy service
        
        Args:
            decoy_generator: Implementation of IDecoyGenerator interface
        """
        self.generator = decoy_generator
        self.deployed_decoys: List[Decoy] = []
```

**Dependency Injection:** `DecoyService` receives an `IDecoyGenerator` interface, not a concrete implementation. This makes testing easy - you can pass a mock generator.

**State Management:**
- `self.generator`: The decoy generator to use
- `self.deployed_decoys`: List tracking all deployed decoys

```python
    def generate_decoys_for_threat_level(self, threat_level: str, base_path: str) -> List[Decoy]:
        """
        Generate appropriate decoys based on threat level
        
        Args:
            threat_level: "Normal", "Elevated", "Suspicious", or "Critical"
            base_path: Base directory where decoys should be placed
            
        Returns:
            List of generated Decoy objects
        """
        decoys = []
        
        if threat_level == "Suspicious":
            # Deploy 2 decoys for suspicious activity
            decoys.append(self.generator.create_credential_decoy(f"{base_path}/passwords.txt"))
            decoys.append(self.generator.create_document_decoy(f"{base_path}/confidential_report.txt"))
```

**Business Logic:**
- **Suspicious (51-70):** Deploy 2 decoys (credential + document)
- **Critical (71-100):** Deploy 4 decoys (2 credentials + config + document)

**Why this logic?**
- More severe threats = more decoys
- Mix of types to catch different attacker behaviors
- Strategic file names (passwords.txt, admin_passwords.txt) attract attackers

```python
        elif threat_level == "Critical":
            # Deploy 4 decoys for critical threats
            decoys.append(self.generator.create_credential_decoy(f"{base_path}/admin_passwords.txt"))
            decoys.append(self.generator.create_credential_decoy(f"{base_path}/api_keys.txt"))
            decoys.append(self.generator.create_config_decoy(f"{base_path}/database_config.yaml"))
            decoys.append(self.generator.create_document_decoy(f"{base_path}/financial_data.txt"))
        
        # Track deployed decoys
        self.deployed_decoys.extend(decoys)
        
        return decoys
```

**Tracking:** All deployed decoys are stored in `self.deployed_decoys` for later detection.

```python
    def is_decoy_file(self, file_path: str) -> bool:
        """
        Check if a file path is a deployed decoy
        
        Args:
            file_path: Path to check
            
        Returns:
            True if file is a decoy, False otherwise
        """
        return any(decoy.file_path == file_path for decoy in self.deployed_decoys)
```

**Decoy Detection:** When FileMonitor detects file access, we can check if it's a decoy. If yes = attacker caught!

**Key Principle:** Business logic only. Doesn't know HOW decoys are created (that's Infrastructure's job).

**Real-World Analogy:** This is like a security manager who decides "We have a suspicious threat, deploy 2 decoys!" but doesn't personally create them - delegates to the generator.

---

## 📁 File 4: Infrastructure Implementation - `src/domain/infrastructure/file_decoy_generator.py`

### Purpose
Actually creates the decoy files using Faker library and writes them to the file system.

### Code Explanation

```python
from faker import Faker
from datetime import datetime
import os
from ..interfaces.decoy_generator import IDecoyGenerator
from ..entities.decoy import Decoy
```

**External Dependencies:** This is the ONLY layer that uses external libraries (Faker, os).

```python
class FileDecoyGenerator(IDecoyGenerator):
    """
    Implements IDecoyGenerator using Faker library
    Creates realistic fake files and writes them to the file system
    """
    
    def __init__(self):
        """Initialize the file decoy generator with Faker"""
        self.faker = Faker()
```

**Implements IDecoyGenerator:** Must have all 3 methods (create_credential_decoy, create_document_decoy, create_config_decoy).

**Faker Instance:** `self.faker` generates realistic fake data.

### Method 1: Credential Decoy

```python
    def create_credential_decoy(self, file_path: str) -> Decoy:
        """
        Generate a fake credential file with realistic passwords and usernames
        """
        # Generate fake credentials using Faker
        content = f"""# Credentials File
# DO NOT SHARE - CONFIDENTIAL

Username: {self.faker.user_name()}
Password: {self.faker.password(length=12, special_chars=True)}

Admin Username: {self.faker.user_name()}
Admin Password: {self.faker.password(length=16, special_chars=True)}

Database User: {self.faker.user_name()}
Database Password: {self.faker.password(length=20, special_chars=True)}

API Key: {self.faker.uuid4()}
Secret Token: {self.faker.sha256()}
"""
```

**Faker Methods Used:**
- `user_name()`: Generates realistic usernames (e.g., "john_smith42")
- `password()`: Generates random passwords with special characters
- `uuid4()`: Generates UUID for API keys
- `sha256()`: Generates SHA-256 hash for tokens

**Why this content?** Looks like a real credentials file that attackers would want to steal.

```python
        # Write to file system
        self._write_to_file(file_path, content)
        
        # Return Decoy object
        return Decoy(
            decoy_type="credential",
            file_path=file_path,
            content=content,
            created_at=datetime.now()
        )
```

**Two-step process:**
1. Write content to actual file system
2. Return Decoy object for tracking

### Method 2: Document Decoy

```python
    def create_document_decoy(self, file_path: str) -> Decoy:
        """
        Generate a fake document file with realistic text
        """
        # Generate fake document using Faker
        content = f"""CONFIDENTIAL REPORT
Date: {self.faker.date()}
Author: {self.faker.name()}
Department: {self.faker.job()}

SUMMARY:
{self.faker.paragraph(nb_sentences=5)}

DETAILS:
{self.faker.text(max_nb_chars=500)}

FINANCIAL DATA:
Revenue: ${self.faker.random_number(digits=7)}
Expenses: ${self.faker.random_number(digits=6)}
Profit Margin: {self.faker.random_int(min=10, max=40)}%

CONTACT INFORMATION:
Email: {self.faker.email()}
Phone: {self.faker.phone_number()}
Address: {self.faker.address()}
"""
```

**Faker Methods Used:**
- `date()`: Random date
- `name()`: Full name (e.g., "John Smith")
- `job()`: Job title (e.g., "Software Engineer")
- `paragraph()`: Realistic paragraph text
- `text()`: Longer text content
- `random_number()`: Random numbers for financial data
- `email()`: Fake email address
- `phone_number()`: Fake phone number
- `address()`: Fake address

**Why this content?** Looks like a confidential business report with financial data - very attractive to attackers.

### Method 3: Config Decoy

```python
    def create_config_decoy(self, file_path: str) -> Decoy:
        """
        Generate a fake configuration file with database/API settings
        """
        # Generate fake config using Faker
        content = f"""# Database Configuration
# PRODUCTION SETTINGS - DO NOT MODIFY

database:
  host: {self.faker.ipv4()}
  port: {self.faker.random_int(min=3000, max=9999)}
  username: {self.faker.user_name()}
  password: {self.faker.password(length=16)}
  database_name: {self.faker.word()}_production

api:
  endpoint: https://{self.faker.domain_name()}/api/v1
  api_key: {self.faker.uuid4()}
  secret_key: {self.faker.sha256()}
  
security:
  encryption_key: {self.faker.sha256()}
  jwt_secret: {self.faker.uuid4()}
  
admin:
  email: {self.faker.email()}
  backup_email: {self.faker.email()}
"""
```

**Faker Methods Used:**
- `ipv4()`: IP address (e.g., "192.168.1.100")
- `random_int()`: Random port number
- `domain_name()`: Domain (e.g., "example.com")
- `word()`: Random word for database name

**Why this content?** Looks like a production database configuration - extremely valuable to attackers.

### Helper Method: File Writing

```python
    def _write_to_file(self, file_path: str, content: str):
        """
        Write content to file system
        
        Args:
            file_path: Path to write to
            content: Content to write
        """
        # Create directory if it doesn't exist
        directory = os.path.dirname(file_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        
        # Write content to file
        with open(file_path, 'w') as f:
            f.write(content)
```

**Safety:** Creates parent directories if they don't exist (prevents errors).

**Key Principle:** This is the ONLY layer that touches external systems (Faker, file system).

**Real-World Analogy:** This is like a factory worker who actually builds the house using specific tools and materials.

---

## 🔄 How Everything Works Together

### Complete Flow

```
1. ThreatDetector detects suspicious activity (score >= 51)
   ↓
2. DecoyService.generate_decoys_for_threat_level("Suspicious", "test_decoys")
   ↓
3. DecoyService decides: "Suspicious = 2 decoys"
   ↓
4. DecoyService calls: generator.create_credential_decoy("test_decoys/passwords.txt")
   ↓
5. FileDecoyGenerator uses Faker to generate fake credentials
   ↓
6. FileDecoyGenerator writes content to file system
   ↓
7. FileDecoyGenerator returns Decoy object
   ↓
8. DecoyService tracks deployed decoy in self.deployed_decoys
   ↓
9. Repeat for document decoy
   ↓
10. Return list of 2 Decoy objects
```

### Example Execution

```python
# Infrastructure layer
generator = FileDecoyGenerator()

# Application layer
service = DecoyService(generator)

# Generate decoys for suspicious threat
decoys = service.generate_decoys_for_threat_level("Suspicious", "test_decoys")

# Result: 2 files created
# - test_decoys/passwords.txt (with fake credentials)
# - test_decoys/confidential_report.txt (with fake document)
```

---

## 🧪 Testing

### Test File: `test_decoy_system.py`

**What it tests:**
1. ✅ FileDecoyGenerator creation
2. ✅ DecoyService creation
3. ✅ Suspicious threat level (2 decoys)
4. ✅ Critical threat level (4 decoys)
5. ✅ Decoy detection (is_decoy_file)
6. ✅ Deployed decoys tracking
7. ✅ Files actually created on disk

**Why testing is important:**
- Verifies all layers work together
- Ensures Faker generates content
- Confirms files are written to disk
- Validates business logic (2 vs 4 decoys)

---

## 🎯 Benefits of Clean Architecture

### 1. Easy Testing
```python
# Can test DecoyService with mock generator
mock_generator = MockDecoyGenerator()
service = DecoyService(mock_generator)
# No need for actual file system or Faker
```

### 2. Easy UI Integration (Future)
```python
# Web dashboard just calls Application layer
class WebDashboard:
    def deploy_decoys_button_clicked(self):
        decoys = self.decoy_service.generate_decoys_for_threat_level("Critical", "/monitored")
        self.display_success(f"Deployed {len(decoys)} decoys")
```

### 3. Easy to Swap Implementations
```python
# Want to use a different fake data generator?
# Just create new class that implements IDecoyGenerator
class CloudDecoyGenerator(IDecoyGenerator):
    # Uses cloud API instead of Faker
    pass

# Swap it in - no changes to DecoyService needed!
service = DecoyService(CloudDecoyGenerator())
```

### 4. Clear Separation of Concerns
- **Domain:** Business rules (what is a decoy?)
- **Application:** Business logic (when to deploy?)
- **Infrastructure:** Technical details (how to create?)

---

## 💡 Key Concepts Learned

### 1. Clean Architecture Layers
- **Domain:** Pure business logic, no dependencies
- **Application:** Orchestrates business operations
- **Infrastructure:** Handles external systems

### 2. Dependency Injection
- Pass interfaces, not concrete implementations
- Makes testing easy
- Allows swapping implementations

### 3. Interface Segregation
- `IDecoyGenerator` defines contract
- Any implementation must follow contract
- Enforced by `@abstractmethod`

### 4. Faker Library
- Generates realistic fake data
- Many methods: `user_name()`, `password()`, `email()`, etc.
- Perfect for honeypot decoys

### 5. Dataclasses
- Reduces boilerplate code
- Automatically generates `__init__`, `__repr__`, `__eq__`
- Clean syntax with type hints

---

## 🚀 Next Steps (Day 17-18)

Now that we have decoy generation, next we'll:
1. **Integrate with ThreatDetector** - Deploy decoys automatically when threat score > 50
2. **Create DecoyManager** - Manages decoy lifecycle
3. **Add Decoy Monitoring** - Detect when attackers access decoys
4. **Implement Alerts** - Notify when decoy is accessed

---

## 📊 Project Status

**Completed:**
- ✅ File monitoring (Day 3-4)
- ✅ Event logging (Day 5-6)
- ✅ Threat detection (Day 9-10)
- ✅ System integration (Day 11-12)
- ✅ Decoy generation (Day 15-16)

**Next:**
- ⏳ Decoy deployment (Day 17-18)
- ⏳ Decoy tracking (Day 19-20)
- ⏳ Alert system (Day 21-22)

**Progress:** 29% complete (16/56 days)

---

## 🎉 Congratulations!

You've successfully implemented Clean Architecture! This is a professional software engineering pattern used in production systems. Your decoy system is now:
- ✅ Testable
- ✅ Maintainable
- ✅ Scalable
- ✅ UI-ready

**You're building a real, professional security system!** 🛡️

---

**Next:** Day 17-18 - Decoy Deployment (integrate with ThreatDetector)
