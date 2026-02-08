# 🎓 Learning Guide: Building an AI-Driven Cybersecurity Deception Platform

## Welcome, Future Security Engineer!

This guide will teach you how to build a production-grade cybersecurity SaaS platform from scratch. Think of me as your mentor walking you through each concept, explaining the "why" behind every decision, and showing you how professional security engineers think about problems.

## 📚 Table of Contents

1. [Understanding the Big Picture](#understanding-the-big-picture)
2. [Core Concepts You Need to Know](#core-concepts-you-need-to-know)
3. [The Architecture: How Everything Fits Together](#the-architecture-how-everything-fits-together)
4. [Building Block by Block](#building-block-by-block)
5. [Security Principles We Follow](#security-principles-we-follow)
6. [Testing Like a Pro](#testing-like-a-pro)
7. [Deployment and Operations](#deployment-and-operations)
8. [Learning Resources](#learning-resources)

---

## Understanding the Big Picture

### What Are We Building?

Imagine you're a security guard protecting a museum. Traditional security just watches for break-ins. But what if you could:
- **Predict** who might be a thief before they steal anything
- **Mislead** thieves by showing them fake treasures
- **Learn** from each attempted theft to get better at catching future thieves
- **Alert** the right people instantly when something suspicious happens

That's exactly what our platform does, but for computer systems!

### The Three Core Ideas

**1. Hybrid Suspicious Scoring (The Detective)**
- Combines rule-based detection (if X happens, it's suspicious) with AI/ML (this pattern looks unusual)
- Gives every user a "trust score" from 0-100
- Like a credit score, but for security

**2. Autonomous Deception (The Trap)**
- Automatically creates fake files that look real
- When attackers touch them, we know they're up to no good
- Like leaving fake diamonds around to catch thieves

**3. Real-Time Visibility (The Control Room)**
- Modern dashboard showing everything happening right now
- Beautiful visualizations that make complex data easy to understand
- Different views for different team members

---

## Core Concepts You Need to Know

### 1. What is a Honeypot?

**Simple Explanation:**
A honeypot is a decoy system designed to attract attackers. It looks like a real target but is actually a trap.

**Real-World Analogy:**
Think of a police sting operation where they set up a fake storefront to catch criminals. The store looks real, but it's actually monitored by police.

**Why It Matters:**
- Attackers reveal their tactics when they interact with honeypots
- We can study attack methods without risking real systems
- It gives us early warning of attacks

### 2. Suspicious Scoring: Rule-Based vs. AI/ML

**Rule-Based Detection (The Checklist)**
```
IF user logs in from 5 different countries in 1 hour THEN suspicious = TRUE
IF user tries to access admin panel without permission THEN suspicious = TRUE
IF user downloads 1000 files in 5 minutes THEN suspicious = TRUE
```

**Pros:** Fast, predictable, easy to explain
**Cons:** Can't catch new attack patterns, attackers can learn the rules

**AI/ML Detection (The Pattern Learner)**
```
This user normally logs in at 9am from New York
Today they logged in at 3am from Russia
Their typing speed is different
Their mouse movements are unusual
→ AI calculates: 85% chance this is an attacker
```

**Pros:** Catches new patterns, adapts over time
**Cons:** Slower, needs training data, harder to explain

**Hybrid Approach (Best of Both Worlds)**
We use BOTH! Rules catch obvious attacks fast, AI catches subtle anomalies.


### 3. Decoy Files: Making Fake Look Real

**The Challenge:**
Attackers are smart. If your fake files look fake, they'll ignore them.

**How We Make Them Realistic:**

1. **Metadata Matching**
   - Real file: `financial_report_Q4_2024.xlsx` created on Dec 31, 2024
   - Decoy file: `financial_report_Q1_2025.xlsx` created on Mar 31, 2025
   - Same naming pattern, realistic dates

2. **Content Generation**
   - Don't just create empty files
   - Generate realistic-looking data (fake names, addresses, numbers)
   - Use templates that match your organization

3. **Context Awareness**
   - Finance server? Create fake financial documents
   - HR server? Create fake employee records
   - Engineering server? Create fake source code

**Example: Creating a Fake Credential File**
```python
# Bad decoy (obvious fake)
password = "password123"

# Good decoy (looks real)
password = "Tr0ub4dor&3"  # Follows password policy
username = "john.smith@company.com"  # Real email format
last_rotated = "2025-01-15"  # Recent date
```

### 4. Autonomous Agents: The AI Brain

**What is an Autonomous Agent?**
An agent is software that can make decisions and take actions without human intervention.

**Our Agent's Job:**
1. **Monitor** - Watch all suspicious scores continuously
2. **Decide** - Determine if action is needed
3. **Act** - Deploy decoys, send alerts, block access
4. **Learn** - Improve detection based on results

**Decision Flow:**
```
User suspicious score = 45 → Keep monitoring
User suspicious score = 65 → Deploy decoys near their location
User touches decoy → Score jumps to 95 → Alert security team
User touches 3 decoys → Score = 100 → Auto-block + escalate
```

**Why Autonomous?**
- Attacks happen in seconds, humans take minutes
- Can monitor thousands of users simultaneously
- Never gets tired or distracted
- Learns and improves 24/7

---

## The Architecture: How Everything Fits Together

### The 10,000 Foot View

```
┌─────────────────────────────────────────────────────────────┐
│                     REACT DASHBOARD (Frontend)               │
│  Real-time charts, alerts, heatmaps, role-based views       │
└─────────────────────────────────────────────────────────────┘
                              ↕ WebSocket + REST API
┌─────────────────────────────────────────────────────────────┐
│                     API SERVER (Gateway)                     │
│  Authentication, rate limiting, request routing              │
└─────────────────────────────────────────────────────────────┘
                              ↕
┌─────────────────────────────────────────────────────────────┐
│                     CORE AGENT (Orchestrator)                │
│  Coordinates all components, manages lifecycle               │
└─────────────────────────────────────────────────────────────┘
         ↓              ↓              ↓              ↓
┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│  Scoring     │ │  Autonomous  │ │  Decoy       │ │  Activity    │
│  Engine      │ │  Agent       │ │  Manager     │ │  Logger      │
└──────────────┘ └──────────────┘ └──────────────┘ └──────────────┘
         ↓              ↓              ↓              ↓
┌─────────────────────────────────────────────────────────────┐
│                     DATABASE LAYER                           │
│  Events, Rules, Decoys, Users, Scores, Threat Intel         │
└─────────────────────────────────────────────────────────────┘
```

### Component Breakdown

**1. Frontend (React Dashboard)**
- **What:** The user interface security analysts see
- **Tech:** React, TypeScript, WebSocket, Chart.js
- **Responsibilities:** Display data, handle user interactions, real-time updates

**2. API Server**
- **What:** The gateway between frontend and backend
- **Tech:** FastAPI (Python), JWT authentication, rate limiting
- **Responsibilities:** Authenticate users, validate requests, route to services

**3. Core Agent**
- **What:** The orchestrator that manages everything
- **Tech:** Python, async/await for concurrency
- **Responsibilities:** Start/stop components, health checks, configuration

**4. Scoring Engine**
- **What:** Calculates suspicious scores
- **Tech:** Python, scikit-learn for ML, rule engine
- **Responsibilities:** Analyze behavior, calculate risk scores, classify severity

**5. Autonomous Agent**
- **What:** The AI brain that makes decisions
- **Tech:** Python, reinforcement learning, decision trees
- **Responsibilities:** Monitor scores, trigger workflows, learn from outcomes

**6. Decoy Manager**
- **What:** Creates and manages fake files
- **Tech:** Python, template engines, file generators
- **Responsibilities:** Generate decoys, track interactions, maintain realism

**7. Activity Logger**
- **What:** Records everything that happens
- **Tech:** Python, SQLAlchemy, PostgreSQL
- **Responsibilities:** Log events, query data, export reports

**8. Database Layer**
- **What:** Persistent storage for all data
- **Tech:** PostgreSQL (production), SQLite (development)
- **Responsibilities:** Store events, users, scores, configurations


---

## Building Block by Block

### Phase 1: Foundation (Weeks 1-2)

**What We're Building:**
The basic structure and data models

**Key Concepts to Learn:**
- Object-oriented programming (classes, inheritance)
- Data modeling (how to represent real-world concepts in code)
- Configuration management (YAML/JSON parsing)

**Step-by-Step:**

**Step 1.1: Set Up Your Development Environment**
```bash
# Create a virtual environment (isolated Python installation)
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install fastapi sqlalchemy hypothesis pytest pyyaml
```

**Why virtual environments?**
- Keeps project dependencies separate
- Prevents version conflicts
- Makes deployment easier

**Step 1.2: Create the Project Structure**
```
adaptive-honeypot-agent/
├── src/
│   └── honeypot/
│       ├── __init__.py
│       ├── core/          # Core agent logic
│       ├── scoring/       # Suspicious scoring engine
│       ├── agent/         # Autonomous agent
│       ├── decoy/         # Decoy management
│       ├── logging/       # Activity logging
│       ├── api/           # REST API
│       └── models/        # Data models
├── tests/
│   ├── unit/
│   ├── property/
│   └── integration/
├── frontend/
│   └── dashboard/         # React app
├── config/
│   └── config.yaml
└── pyproject.toml
```

**Why this structure?**
- Separation of concerns (each folder has one job)
- Easy to find code
- Scales as project grows

**Step 1.3: Create Your First Data Model**

Let's create a `SecurityEvent` class that represents something suspicious happening:

```python
# src/honeypot/models/event.py

from datetime import datetime
from typing import Optional
from dataclasses import dataclass

@dataclass
class SecurityEvent:
    """
    Represents a single security event (login, file access, etc.)
    
    Think of this as a "security incident report" that captures
    everything we need to know about what happened.
    """
    
    # Who did it?
    user_id: str
    source_ip: str
    
    # What happened?
    event_type: str  # "login", "file_access", "privilege_escalation"
    action: str      # "read", "write", "delete"
    target: str      # What they accessed
    
    # When?
    timestamp: datetime
    
    # How suspicious?
    suspicious_score: float  # 0-100
    
    # Extra details
    metadata: dict
    
    # Was this a decoy interaction?
    is_decoy_interaction: bool = False
    decoy_id: Optional[str] = None
    
    def __post_init__(self):
        """
        Validation that runs after object creation.
        This is defensive programming - catch errors early!
        """
        if not 0 <= self.suspicious_score <= 100:
            raise ValueError(f"Score must be 0-100, got {self.suspicious_score}")
        
        if self.is_decoy_interaction and not self.decoy_id:
            raise ValueError("Decoy interactions must have a decoy_id")
```

**Learning Points:**
- `@dataclass` - Python decorator that auto-generates `__init__`, `__repr__`, etc.
- Type hints (`str`, `float`, `Optional`) - Help catch bugs and document code
- Validation - Always validate input data!
- Comments - Explain WHY, not just WHAT

**Step 1.4: Create the Configuration System**

```python
# src/honeypot/core/config.py

from typing import List, Dict, Any
import yaml
from pathlib import Path

class Config:
    """
    Manages all configuration for the honeypot agent.
    
    Why we need this:
    - Different settings for dev/staging/production
    - Change behavior without changing code
    - Easy to test with different configurations
    """
    
    def __init__(self, config_path: str):
        self.config_path = Path(config_path)
        self.data = self._load_config()
        self._validate()
    
    def _load_config(self) -> dict:
        """Load YAML configuration file"""
        try:
            with open(self.config_path, 'r') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            raise ConfigError(f"Config file not found: {self.config_path}")
        except yaml.YAMLError as e:
            raise ConfigError(f"Invalid YAML: {e}")
    
    def _validate(self):
        """
        Validate configuration has required fields.
        
        Fail fast principle: If config is wrong, fail immediately
        rather than failing mysteriously later.
        """
        required_sections = ['agent', 'scoring', 'decoy', 'database']
        
        for section in required_sections:
            if section not in self.data:
                raise ConfigError(f"Missing required section: {section}")
        
        # Validate scoring thresholds
        scoring = self.data['scoring']
        if not 0 <= scoring.get('threshold', 0) <= 100:
            raise ConfigError("Scoring threshold must be 0-100")
    
    def get(self, key: str, default=None):
        """Get configuration value with dot notation"""
        # Support nested keys like "scoring.threshold"
        keys = key.split('.')
        value = self.data
        
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
            else:
                return default
        
        return value if value is not None else default
    
    def reload(self):
        """Reload configuration from disk (hot reload)"""
        old_data = self.data
        try:
            self.data = self._load_config()
            self._validate()
        except Exception as e:
            # If reload fails, keep old config
            self.data = old_data
            raise ConfigError(f"Failed to reload config: {e}")


class ConfigError(Exception):
    """Custom exception for configuration errors"""
    pass
```

**Example config.yaml:**
```yaml
agent:
  name: "honeypot-agent-01"
  listen_address: "0.0.0.0"
  api_port: 8080
  log_level: "INFO"

scoring:
  threshold: 60  # Trigger deception at this score
  ml_enabled: true
  rule_weight: 0.4  # 40% rule-based, 60% ML
  ml_weight: 0.6

decoy:
  enabled: true
  types:
    - documents
    - credentials
    - configs
  placement_strategy: "context_aware"
  
database:
  type: "postgresql"
  host: "localhost"
  port: 5432
  name: "honeypot_db"
  user: "honeypot_user"
  password: "${DB_PASSWORD}"  # From environment variable
```

**Learning Points:**
- YAML is human-readable configuration format
- Validation prevents runtime errors
- Hot reload allows changes without restart
- Environment variables for secrets (never hardcode passwords!)


### Phase 2: The Scoring Engine (Weeks 3-4)

**What We're Building:**
The hybrid system that calculates suspicious scores

**Key Concepts to Learn:**
- Rule engines (pattern matching)
- Machine learning basics (anomaly detection)
- Statistical analysis (baselines, standard deviations)

**Step 2.1: Understanding the Scoring Algorithm**

**The Formula:**
```
Final Score = (Rule Score × Rule Weight) + (ML Score × ML Weight)

Where:
- Rule Score: 0-100 based on rule violations
- ML Score: 0-100 based on behavioral anomaly
- Weights: Configurable (default 40% rules, 60% ML)
```

**Step 2.2: Build the Rule-Based Scorer**

```python
# src/honeypot/scoring/rule_scorer.py

from typing import List, Dict
from datetime import datetime, timedelta
from ..models.event import SecurityEvent

class RuleScorer:
    """
    Calculates suspicious score based on predefined rules.
    
    Think of this as a checklist of "red flags" that indicate
    suspicious behavior.
    """
    
    def __init__(self):
        # Define our rules with their severity weights
        self.rules = {
            'abnormal_access_frequency': 25,
            'privilege_escalation': 40,
            'unusual_file_traversal': 30,
            'ip_anomaly': 20,
            'device_anomaly': 15,
            'off_hours_access': 10,
            'multiple_failed_logins': 35,
        }
    
    def calculate_score(self, 
                       user_id: str, 
                       recent_events: List[SecurityEvent],
                       user_baseline: Dict) -> float:
        """
        Calculate rule-based score for a user.
        
        Args:
            user_id: The user being scored
            recent_events: Events from last 24 hours
            user_baseline: Normal behavior profile
            
        Returns:
            Score from 0-100
        """
        violations = []
        
        # Check each rule
        if self._check_abnormal_frequency(recent_events, user_baseline):
            violations.append('abnormal_access_frequency')
        
        if self._check_privilege_escalation(recent_events):
            violations.append('privilege_escalation')
        
        if self._check_unusual_traversal(recent_events, user_baseline):
            violations.append('unusual_file_traversal')
        
        if self._check_ip_anomaly(recent_events, user_baseline):
            violations.append('ip_anomaly')
        
        # Calculate total score (max 100)
        total_score = sum(self.rules[v] for v in violations)
        return min(total_score, 100)
    
    def _check_abnormal_frequency(self, 
                                  events: List[SecurityEvent],
                                  baseline: Dict) -> bool:
        """
        Check if user is accessing resources more than normal.
        
        Example:
        - Normal: 50 file accesses per hour
        - Current: 500 file accesses per hour
        - Result: SUSPICIOUS (10x normal)
        """
        if not events:
            return False
        
        # Count events in last hour
        one_hour_ago = datetime.now() - timedelta(hours=1)
        recent = [e for e in events if e.timestamp > one_hour_ago]
        current_frequency = len(recent)
        
        # Compare to baseline
        normal_frequency = baseline.get('avg_hourly_events', 50)
        threshold = normal_frequency * 3  # 3x normal is suspicious
        
        return current_frequency > threshold
    
    def _check_privilege_escalation(self, events: List[SecurityEvent]) -> bool:
        """
        Check if user is trying to gain higher privileges.
        
        Red flags:
        - Accessing admin endpoints without permission
        - Attempting to modify user roles
        - Trying to access restricted files
        """
        escalation_keywords = [
            'admin', 'root', 'sudo', 'privilege',
            'role_change', 'permission_modify'
        ]
        
        for event in events:
            # Check if event involves privilege escalation
            if any(keyword in event.action.lower() for keyword in escalation_keywords):
                return True
            
            # Check metadata for escalation attempts
            if event.metadata.get('permission_denied') and \
               event.metadata.get('required_role') == 'admin':
                return True
        
        return False
    
    def _check_unusual_traversal(self, 
                                 events: List[SecurityEvent],
                                 baseline: Dict) -> bool:
        """
        Check if user is accessing unusual file paths.
        
        Example suspicious patterns:
        - Accessing system directories (/etc, /var, C:\Windows)
        - Directory traversal attacks (../../etc/passwd)
        - Accessing many different directories rapidly
        """
        suspicious_patterns = [
            '../',           # Directory traversal
            '/etc/',         # Linux system files
            '/var/',         # Linux system files
            'C:\\Windows',   # Windows system files
            '/root/',        # Root user files
        ]
        
        for event in events:
            target = event.target
            
            # Check for suspicious patterns
            if any(pattern in target for pattern in suspicious_patterns):
                return True
            
            # Check if accessing way more directories than normal
            accessed_dirs = set(self._extract_directory(e.target) for e in events)
            normal_dirs = baseline.get('avg_directories_accessed', 5)
            
            if len(accessed_dirs) > normal_dirs * 5:
                return True
        
        return False
    
    def _check_ip_anomaly(self, 
                         events: List[SecurityEvent],
                         baseline: Dict) -> bool:
        """
        Check if user is connecting from unusual IP addresses.
        
        Red flags:
        - IP from different country than usual
        - Multiple IPs in short time (impossible travel)
        - IP on known bad actor list
        """
        if not events:
            return False
        
        # Get unique IPs from recent events
        recent_ips = set(e.source_ip for e in events)
        
        # Get user's normal IPs
        normal_ips = set(baseline.get('common_ips', []))
        
        # Check for new IPs
        new_ips = recent_ips - normal_ips
        
        # Multiple new IPs is suspicious
        if len(new_ips) > 2:
            return True
        
        # Check for impossible travel (multiple countries in short time)
        if self._detect_impossible_travel(events):
            return True
        
        return False
    
    def _detect_impossible_travel(self, events: List[SecurityEvent]) -> bool:
        """
        Detect if user appears to be in multiple locations impossibly fast.
        
        Example:
        - Login from New York at 10:00 AM
        - Login from Tokyo at 10:05 AM
        - Impossible to travel that fast!
        """
        # Sort events by time
        sorted_events = sorted(events, key=lambda e: e.timestamp)
        
        for i in range(len(sorted_events) - 1):
            event1 = sorted_events[i]
            event2 = sorted_events[i + 1]
            
            # Get time difference
            time_diff = (event2.timestamp - event1.timestamp).total_seconds() / 3600
            
            # Get geographic distance (simplified - would use real geolocation)
            distance_km = self._get_distance(event1.source_ip, event2.source_ip)
            
            # Check if travel speed is impossible (>1000 km/h)
            if time_diff > 0 and (distance_km / time_diff) > 1000:
                return True
        
        return False
    
    @staticmethod
    def _extract_directory(path: str) -> str:
        """Extract directory from file path"""
        return path.rsplit('/', 1)[0] if '/' in path else ''
    
    @staticmethod
    def _get_distance(ip1: str, ip2: str) -> float:
        """
        Get geographic distance between two IPs.
        
        In production, you'd use a geolocation service like MaxMind.
        For now, simplified version.
        """
        # Placeholder - would integrate with geolocation API
        return 0.0
```

**Learning Points:**
- Each rule is independent and testable
- Rules are weighted by severity
- Baselines are crucial for anomaly detection
- Real-world security requires domain knowledge


**Step 2.3: Build the ML-Based Scorer**

```python
# src/honeypot/scoring/ml_scorer.py

import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from typing import List, Dict
from ..models.event import SecurityEvent

class MLScorer:
    """
    Uses machine learning to detect behavioral anomalies.
    
    Key Concept: Anomaly Detection
    - We learn what "normal" behavior looks like
    - Anything that deviates significantly is suspicious
    - No need to know what attacks look like in advance!
    """
    
    def __init__(self):
        # Isolation Forest is great for anomaly detection
        self.model = IsolationForest(
            contamination=0.1,  # Expect 10% of data to be anomalies
            random_state=42
        )
        self.scaler = StandardScaler()
        self.is_trained = False
    
    def train(self, historical_events: List[SecurityEvent]):
        """
        Train the model on historical "normal" behavior.
        
        This is called during initial setup and periodically updated.
        """
        if len(historical_events) < 100:
            raise ValueError("Need at least 100 events to train")
        
        # Extract features from events
        features = self._extract_features(historical_events)
        
        # Normalize features (important for ML!)
        features_scaled = self.scaler.fit_transform(features)
        
        # Train the model
        self.model.fit(features_scaled)
        self.is_trained = True
    
    def calculate_score(self, recent_events: List[SecurityEvent]) -> float:
        """
        Calculate ML-based anomaly score.
        
        Returns:
            Score from 0-100 (higher = more suspicious)
        """
        if not self.is_trained:
            raise RuntimeError("Model not trained yet!")
        
        if not recent_events:
            return 0.0
        
        # Extract features
        features = self._extract_features(recent_events)
        features_scaled = self.scaler.transform(features)
        
        # Get anomaly scores
        # Isolation Forest returns -1 for anomalies, 1 for normal
        anomaly_scores = self.model.score_samples(features_scaled)
        
        # Convert to 0-100 scale
        # More negative = more anomalous = higher score
        avg_score = np.mean(anomaly_scores)
        normalized_score = self._normalize_score(avg_score)
        
        return normalized_score
    
    def _extract_features(self, events: List[SecurityEvent]) -> np.ndarray:
        """
        Convert events into numerical features for ML.
        
        Feature Engineering is crucial! We need to capture
        the essence of behavior in numbers.
        """
        features = []
        
        for event in events:
            feature_vector = [
                # Temporal features
                event.timestamp.hour,  # Hour of day (0-23)
                event.timestamp.weekday(),  # Day of week (0-6)
                
                # Behavioral features
                len(event.target),  # Length of accessed path
                event.metadata.get('duration_seconds', 0),
                event.metadata.get('bytes_transferred', 0),
                
                # Categorical features (encoded as numbers)
                self._encode_event_type(event.event_type),
                self._encode_action(event.action),
                
                # Derived features
                1 if event.is_decoy_interaction else 0,
                event.suspicious_score,  # Previous score
            ]
            
            features.append(feature_vector)
        
        return np.array(features)
    
    @staticmethod
    def _encode_event_type(event_type: str) -> int:
        """Convert event type to number"""
        encoding = {
            'login': 1,
            'file_access': 2,
            'file_modify': 3,
            'privilege_escalation': 4,
            'network_access': 5,
        }
        return encoding.get(event_type, 0)
    
    @staticmethod
    def _encode_action(action: str) -> int:
        """Convert action to number"""
        encoding = {
            'read': 1,
            'write': 2,
            'delete': 3,
            'execute': 4,
        }
        return encoding.get(action, 0)
    
    @staticmethod
    def _normalize_score(anomaly_score: float) -> float:
        """
        Convert Isolation Forest score to 0-100 scale.
        
        Isolation Forest scores typically range from -0.5 to 0.5
        - Negative = anomaly
        - Positive = normal
        """
        # Map [-0.5, 0.5] to [100, 0]
        # More negative = higher suspicious score
        normalized = (0.5 - anomaly_score) * 100
        return max(0, min(100, normalized))
```

**Step 2.4: Combine Rule and ML Scores**

```python
# src/honeypot/scoring/hybrid_scorer.py

from typing import List, Dict
from ..models.event import SecurityEvent
from .rule_scorer import RuleScorer
from .ml_scorer import MLScorer

class HybridScorer:
    """
    Combines rule-based and ML-based scoring.
    
    Best of both worlds:
    - Rules catch known attack patterns quickly
    - ML catches novel/unknown patterns
    """
    
    def __init__(self, rule_weight: float = 0.4, ml_weight: float = 0.6):
        """
        Args:
            rule_weight: Weight for rule-based score (0-1)
            ml_weight: Weight for ML-based score (0-1)
        """
        if abs(rule_weight + ml_weight - 1.0) > 0.01:
            raise ValueError("Weights must sum to 1.0")
        
        self.rule_weight = rule_weight
        self.ml_weight = ml_weight
        
        self.rule_scorer = RuleScorer()
        self.ml_scorer = MLScorer()
    
    def calculate_score(self,
                       user_id: str,
                       recent_events: List[SecurityEvent],
                       user_baseline: Dict) -> Dict:
        """
        Calculate hybrid suspicious score.
        
        Returns:
            {
                'total_score': 0-100,
                'rule_score': 0-100,
                'ml_score': 0-100,
                'severity': 'low'|'medium'|'high'|'critical',
                'triggered_rules': [...],
            }
        """
        # Calculate individual scores
        rule_score = self.rule_scorer.calculate_score(
            user_id, recent_events, user_baseline
        )
        
        ml_score = self.ml_scorer.calculate_score(recent_events)
        
        # Combine with weights
        total_score = (rule_score * self.rule_weight) + (ml_score * self.ml_weight)
        
        # Classify severity
        severity = self._classify_severity(total_score)
        
        return {
            'total_score': round(total_score, 2),
            'rule_score': round(rule_score, 2),
            'ml_score': round(ml_score, 2),
            'severity': severity,
            'timestamp': datetime.now(),
            'user_id': user_id,
        }
    
    @staticmethod
    def _classify_severity(score: float) -> str:
        """Classify score into severity levels"""
        if score >= 76:
            return 'critical'
        elif score >= 51:
            return 'high'
        elif score >= 26:
            return 'medium'
        else:
            return 'low'
```

**Learning Points:**
- ML requires feature engineering (converting data to numbers)
- Isolation Forest is perfect for anomaly detection
- Normalization is crucial for ML
- Hybrid approaches leverage strengths of both methods
- Always validate and test ML models!


### Phase 3: The Autonomous Agent (Weeks 5-6)

**What We're Building:**
The AI brain that makes decisions and takes actions

**Key Concepts to Learn:**
- State machines (tracking agent state)
- Decision trees (if-then-else logic)
- Feedback loops (learning from outcomes)
- Asynchronous programming (doing multiple things at once)

**Step 3.1: Understanding Agent Architecture**

```python
# src/honeypot/agent/autonomous_agent.py

import asyncio
from typing import Dict, List
from datetime import datetime, timedelta
from enum import Enum

class AgentState(Enum):
    """
    The agent's current operational state.
    
    Think of this like a traffic light:
    - MONITORING: Green light, watching but not acting
    - INVESTIGATING: Yellow light, suspicious activity detected
    - RESPONDING: Red light, taking defensive action
    - LEARNING: Processing outcomes to improve
    """
    MONITORING = "monitoring"
    INVESTIGATING = "investigating"
    RESPONDING = "responding"
    LEARNING = "learning"

class AutonomousAgent:
    """
    The AI brain that continuously monitors, decides, and acts.
    
    Core Loop:
    1. Monitor all suspicious scores
    2. Detect when thresholds are exceeded
    3. Trigger appropriate deception workflows
    4. Learn from outcomes
    5. Repeat
    """
    
    def __init__(self, 
                 scoring_engine,
                 decoy_manager,
                 alert_system,
                 response_handler):
        self.scoring_engine = scoring_engine
        self.decoy_manager = decoy_manager
        self.alert_system = alert_system
        self.response_handler = response_handler
        
        # Agent state
        self.state = AgentState.MONITORING
        self.monitored_users: Dict[str, UserContext] = {}
        
        # Decision thresholds
        self.investigation_threshold = 60
        self.response_threshold = 80
        self.critical_threshold = 95
        
        # Learning parameters
        self.feedback_history = []
        self.model_update_interval = timedelta(hours=1)
        self.last_model_update = datetime.now()
    
    async def run(self):
        """
        Main agent loop - runs continuously.
        
        This is the heart of the autonomous agent!
        """
        print("🤖 Autonomous Agent starting...")
        
        while True:
            try:
                # Phase 1: Monitor
                await self._monitor_phase()
                
                # Phase 2: Investigate suspicious users
                await self._investigate_phase()
                
                # Phase 3: Respond to threats
                await self._respond_phase()
                
                # Phase 4: Learn from outcomes
                await self._learn_phase()
                
                # Sleep briefly before next iteration
                await asyncio.sleep(2)  # Check every 2 seconds
                
            except Exception as e:
                print(f"❌ Agent error: {e}")
                await asyncio.sleep(5)  # Back off on error
    
    async def _monitor_phase(self):
        """
        Continuously monitor all users' suspicious scores.
        
        This runs constantly in the background.
        """
        self.state = AgentState.MONITORING
        
        # Get all active users
        active_users = await self._get_active_users()
        
        for user_id in active_users:
            # Calculate current score
            score_data = await self._calculate_user_score(user_id)
            
            # Update user context
            if user_id not in self.monitored_users:
                self.monitored_users[user_id] = UserContext(user_id)
            
            context = self.monitored_users[user_id]
            context.update_score(score_data)
            
            # Check if we need to escalate
            if score_data['total_score'] >= self.investigation_threshold:
                context.mark_for_investigation()
    
    async def _investigate_phase(self):
        """
        Investigate users flagged as suspicious.
        
        Deploy decoys near their activity to gather more intel.
        """
        self.state = AgentState.INVESTIGATING
        
        # Get users marked for investigation
        investigating = [
            ctx for ctx in self.monitored_users.values()
            if ctx.needs_investigation
        ]
        
        for context in investigating:
            print(f"🔍 Investigating user {context.user_id} (score: {context.current_score})")
            
            # Deploy decoys in user's area of activity
            decoys = await self._deploy_contextual_decoys(context)
            context.add_decoys(decoys)
            
            # Mark as investigated
            context.investigation_started()
    
    async def _respond_phase(self):
        """
        Respond to confirmed threats.
        
        Take defensive actions based on severity.
        """
        self.state = AgentState.RESPONDING
        
        # Get users above response threshold
        responding = [
            ctx for ctx in self.monitored_users.values()
            if ctx.current_score >= self.response_threshold
        ]
        
        for context in responding:
            severity = context.get_severity()
            
            if severity == 'critical':
                # Immediate block + alert
                await self._execute_critical_response(context)
            elif severity == 'high':
                # Rate limit + alert
                await self._execute_high_response(context)
            else:
                # Monitor closely + alert
                await self._execute_medium_response(context)
    
    async def _learn_phase(self):
        """
        Learn from outcomes to improve detection.
        
        This is where the agent gets smarter over time!
        """
        self.state = AgentState.LEARNING
        
        # Check if it's time to update the model
        if datetime.now() - self.last_model_update < self.model_update_interval:
            return
        
        print("🧠 Learning from recent outcomes...")
        
        # Collect feedback from recent interactions
        feedback = await self._collect_feedback()
        
        # Update scoring model
        if len(feedback) >= 10:  # Need minimum data
            await self._update_scoring_model(feedback)
        
        # Update decision thresholds
        await self._optimize_thresholds(feedback)
        
        self.last_model_update = datetime.now()
    
    async def _deploy_contextual_decoys(self, context: UserContext) -> List[str]:
        """
        Deploy decoys that match the user's context.
        
        If they're accessing financial files, deploy fake financial docs.
        If they're accessing configs, deploy fake credentials.
        """
        # Analyze user's recent activity
        activity_pattern = context.get_activity_pattern()
        
        # Determine appropriate decoy types
        decoy_types = self._select_decoy_types(activity_pattern)
        
        # Generate and deploy decoys
        decoy_ids = []
        for decoy_type in decoy_types:
            decoy_id = await self.decoy_manager.create_decoy(
                decoy_type=decoy_type,
                context=activity_pattern,
                target_user=context.user_id
            )
            decoy_ids.append(decoy_id)
        
        print(f"🎭 Deployed {len(decoy_ids)} decoys for user {context.user_id}")
        return decoy_ids
    
    def _select_decoy_types(self, activity_pattern: Dict) -> List[str]:
        """
        Choose appropriate decoy types based on user activity.
        
        This is context-aware deception!
        """
        decoy_types = []
        
        # Check what they've been accessing
        accessed_files = activity_pattern.get('accessed_files', [])
        
        if any('.xlsx' in f or '.csv' in f for f in accessed_files):
            decoy_types.append('financial_spreadsheet')
        
        if any('config' in f or '.env' in f for f in accessed_files):
            decoy_types.append('credentials_file')
        
        if any('.sql' in f or 'database' in f for f in accessed_files):
            decoy_types.append('database_dump')
        
        # Default to generic documents if no pattern
        if not decoy_types:
            decoy_types.append('generic_document')
        
        return decoy_types
    
    async def _execute_critical_response(self, context: UserContext):
        """
        Critical threat response: Immediate action required!
        """
        print(f"🚨 CRITICAL THREAT: User {context.user_id}")
        
        # 1. Block the user immediately
        await self.response_handler.block_user(
            user_id=context.user_id,
            reason="Critical suspicious score",
            duration=timedelta(hours=24)
        )
        
        # 2. Send high-priority alert
        await self.alert_system.send_alert(
            severity='critical',
            title=f"Critical Threat Detected: {context.user_id}",
            description=f"User score: {context.current_score}. Immediate action taken.",
            user_id=context.user_id
        )
        
        # 3. Log for forensics
        await self._log_response(context, 'critical_block')
    
    async def _collect_feedback(self) -> List[Dict]:
        """
        Collect feedback on agent decisions.
        
        Feedback includes:
        - Did decoys work? (were they accessed?)
        - Were alerts accurate? (confirmed threats vs false positives)
        - Did responses stop attacks?
        """
        feedback = []
        
        for context in self.monitored_users.values():
            # Check decoy effectiveness
            decoy_interactions = context.get_decoy_interactions()
            
            if decoy_interactions:
                # Decoys were accessed = good detection!
                feedback.append({
                    'user_id': context.user_id,
                    'score': context.current_score,
                    'outcome': 'true_positive',
                    'confidence': 0.9
                })
            elif context.current_score > self.response_threshold:
                # High score but no decoy interaction = possible false positive
                feedback.append({
                    'user_id': context.user_id,
                    'score': context.current_score,
                    'outcome': 'possible_false_positive',
                    'confidence': 0.5
                })
        
        return feedback
    
    async def _update_scoring_model(self, feedback: List[Dict]):
        """
        Update the ML model based on feedback.
        
        This is reinforcement learning in action!
        """
        # Extract training data from feedback
        true_positives = [f for f in feedback if f['outcome'] == 'true_positive']
        false_positives = [f for f in feedback if 'false_positive' in f['outcome']]
        
        print(f"📊 Feedback: {len(true_positives)} confirmed threats, "
              f"{len(false_positives)} possible false positives")
        
        # Retrain ML scorer with new data
        # (Implementation would fetch events and retrain)
        await self.scoring_engine.ml_scorer.retrain(feedback)


class UserContext:
    """
    Tracks everything we know about a user's current session.
    
    This is like a case file for each user.
    """
    
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.current_score = 0.0
        self.score_history = []
        self.needs_investigation = False
        self.investigation_start = None
        self.deployed_decoys = []
        self.decoy_interactions = []
        self.recent_events = []
    
    def update_score(self, score_data: Dict):
        """Update user's suspicious score"""
        self.current_score = score_data['total_score']
        self.score_history.append({
            'score': self.current_score,
            'timestamp': datetime.now()
        })
    
    def mark_for_investigation(self):
        """Flag user for investigation"""
        if not self.needs_investigation:
            self.needs_investigation = True
            print(f"⚠️  User {self.user_id} marked for investigation")
    
    def get_severity(self) -> str:
        """Get current threat severity"""
        if self.current_score >= 95:
            return 'critical'
        elif self.current_score >= 80:
            return 'high'
        elif self.current_score >= 60:
            return 'medium'
        else:
            return 'low'
```

**Learning Points:**
- State machines help manage complex behavior
- Async/await enables concurrent monitoring of many users
- Context-aware decisions are more effective
- Feedback loops enable continuous improvement
- Autonomous doesn't mean uncontrolled - we have thresholds and safeguards


### Phase 4: Decoy File Generation (Weeks 7-8)

**What We're Building:**
Realistic fake files that fool attackers

**Key Concepts to Learn:**
- File generation and manipulation
- Template engines
- Metadata spoofing
- Context-aware content generation

**Step 4.1: The Decoy Manager**

```python
# src/honeypot/decoy/decoy_manager.py

import os
import random
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List
from .generators import (
    DocumentGenerator,
    CredentialGenerator,
    ConfigGenerator,
    DatabaseGenerator
)

class DecoyManager:
    """
    Creates and manages decoy files.
    
    Goal: Make fake files indistinguishable from real ones.
    """
    
    def __init__(self, decoy_root: str):
        self.decoy_root = Path(decoy_root)
        self.decoy_root.mkdir(exist_ok=True)
        
        # Initialize generators
        self.generators = {
            'document': DocumentGenerator(),
            'credential': CredentialGenerator(),
            'config': ConfigGenerator(),
            'database': DatabaseGenerator(),
        }
        
        # Track all decoys
        self.active_decoys: Dict[str, DecoyFile] = {}
    
    async def create_decoy(self,
                          decoy_type: str,
                          context: Dict,
                          target_user: str = None) -> str:
        """
        Create a context-aware decoy file.
        
        Args:
            decoy_type: Type of decoy to create
            context: User activity context for realism
            target_user: Optional user to target
            
        Returns:
            Decoy ID for tracking
        """
        # Generate decoy content
        generator = self.generators.get(decoy_type)
        if not generator:
            raise ValueError(f"Unknown decoy type: {decoy_type}")
        
        decoy_content = generator.generate(context)
        
        # Create realistic file path
        file_path = self._generate_realistic_path(decoy_type, context)
        
        # Write file with realistic metadata
        full_path = self.decoy_root / file_path
        full_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(full_path, 'wb') as f:
            f.write(decoy_content)
        
        # Set realistic timestamps
        self._set_realistic_timestamps(full_path, context)
        
        # Set realistic permissions
        self._set_realistic_permissions(full_path, decoy_type)
        
        # Create decoy record
        decoy = DecoyFile(
            decoy_id=self._generate_decoy_id(),
            file_path=str(file_path),
            decoy_type=decoy_type,
            created_at=datetime.now(),
            target_user=target_user,
            context=context
        )
        
        self.active_decoys[decoy.decoy_id] = decoy
        
        print(f"🎭 Created decoy: {file_path}")
        return decoy.decoy_id
    
    def _generate_realistic_path(self, decoy_type: str, context: Dict) -> str:
        """
        Generate a file path that looks realistic.
        
        Bad: /decoys/fake_file_123.txt
        Good: /home/user/Documents/Financial_Report_Q4_2024.xlsx
        """
        # Get user's common directories from context
        common_dirs = context.get('common_directories', ['/home/user/Documents'])
        base_dir = random.choice(common_dirs)
        
        # Generate realistic filename
        if decoy_type == 'document':
            filename = self._generate_document_name(context)
        elif decoy_type == 'credential':
            filename = self._generate_credential_name(context)
        elif decoy_type == 'config':
            filename = self._generate_config_name(context)
        else:
            filename = f"data_{random.randint(1000, 9999)}.txt"
        
        return f"{base_dir}/{filename}"
    
    def _generate_document_name(self, context: Dict) -> str:
        """Generate realistic document filename"""
        # Analyze context to determine document type
        industry = context.get('industry', 'general')
        
        templates = {
            'finance': [
                'Financial_Report_Q{quarter}_{year}.xlsx',
                'Budget_Analysis_{year}.xlsx',
                'Revenue_Forecast_{month}_{year}.csv',
            ],
            'hr': [
                'Employee_Records_{year}.xlsx',
                'Salary_Information_{department}.xlsx',
                'Performance_Reviews_{quarter}_{year}.docx',
            ],
            'engineering': [
                'API_Keys_{environment}.txt',
                'Database_Credentials_{env}.env',
                'Server_Config_{region}.yaml',
            ],
        }
        
        # Get templates for industry
        industry_templates = templates.get(industry, templates['finance'])
        template = random.choice(industry_templates)
        
        # Fill in template
        now = datetime.now()
        return template.format(
            quarter=f"Q{(now.month-1)//3 + 1}",
            year=now.year,
            month=now.strftime('%B'),
            department='Engineering',
            environment='production',
            env='prod',
            region='us-east-1'
        )
    
    def _set_realistic_timestamps(self, file_path: Path, context: Dict):
        """
        Set file timestamps to look realistic.
        
        Attackers check timestamps! Make them believable.
        """
        # Get typical file age from context
        typical_age_days = context.get('typical_file_age_days', 30)
        
        # Create timestamp within realistic range
        age = timedelta(days=random.randint(1, typical_age_days))
        timestamp = datetime.now() - age
        
        # Set access and modification times
        timestamp_epoch = timestamp.timestamp()
        os.utime(file_path, (timestamp_epoch, timestamp_epoch))
    
    def _set_realistic_permissions(self, file_path: Path, decoy_type: str):
        """
        Set file permissions appropriately.
        
        Credentials should be readable only by owner.
        Documents can be more permissive.
        """
        if decoy_type == 'credential':
            # 600 = owner read/write only
            os.chmod(file_path, 0o600)
        elif decoy_type == 'config':
            # 644 = owner read/write, others read
            os.chmod(file_path, 0o644)
        else:
            # 664 = owner/group read/write, others read
            os.chmod(file_path, 0o664)
```

**Step 4.2: Document Generator**

```python
# src/honeypot/decoy/generators/document_generator.py

from typing import Dict
import random
from faker import Faker  # Library for generating fake data

class DocumentGenerator:
    """
    Generates realistic fake documents.
    
    Uses templates and fake data to create convincing files.
    """
    
    def __init__(self):
        self.faker = Faker()
    
    def generate(self, context: Dict) -> bytes:
        """Generate document content based on context"""
        doc_type = context.get('document_type', 'spreadsheet')
        
        if doc_type == 'spreadsheet':
            return self._generate_spreadsheet(context)
        elif doc_type == 'pdf':
            return self._generate_pdf(context)
        elif doc_type == 'text':
            return self._generate_text(context)
        else:
            return self._generate_generic(context)
    
    def _generate_spreadsheet(self, context: Dict) -> bytes:
        """
        Generate a fake Excel/CSV file.
        
        Example: Financial report with fake numbers
        """
        import csv
        from io import StringIO
        
        # Determine content type from context
        content_type = context.get('content_type', 'financial')
        
        if content_type == 'financial':
            headers = ['Date', 'Department', 'Revenue', 'Expenses', 'Profit']
            rows = []
            
            for i in range(50):  # 50 rows of fake data
                date = self.faker.date_between(start_date='-1y', end_date='today')
                department = random.choice(['Sales', 'Marketing', 'Engineering', 'HR'])
                revenue = random.randint(10000, 100000)
                expenses = random.randint(5000, 80000)
                profit = revenue - expenses
                
                rows.append([date, department, revenue, expenses, profit])
        
        elif content_type == 'employee':
            headers = ['Employee ID', 'Name', 'Email', 'Department', 'Salary']
            rows = []
            
            for i in range(30):
                emp_id = f"EMP{random.randint(1000, 9999)}"
                name = self.faker.name()
                email = self.faker.email()
                department = random.choice(['Engineering', 'Sales', 'HR', 'Finance'])
                salary = random.randint(50000, 150000)
                
                rows.append([emp_id, name, email, department, salary])
        
        # Convert to CSV
        output = StringIO()
        writer = csv.writer(output)
        writer.writerow(headers)
        writer.writerows(rows)
        
        return output.getvalue().encode('utf-8')
    
    def _generate_pdf(self, context: Dict) -> bytes:
        """
        Generate a fake PDF document.
        
        Would use a library like ReportLab in production.
        For now, simplified version.
        """
        # Placeholder - would generate actual PDF
        content = f"""
        CONFIDENTIAL DOCUMENT
        
        Company: {self.faker.company()}
        Date: {self.faker.date()}
        
        This document contains sensitive information...
        
        {self.faker.text(max_nb_chars=500)}
        """
        return content.encode('utf-8')
```

**Step 4.3: Credential Generator**

```python
# src/honeypot/decoy/generators/credential_generator.py

import random
import string
from typing import Dict

class CredentialGenerator:
    """
    Generates fake but realistic-looking credentials.
    
    These are honeytokens - credentials that alert us when used.
    """
    
    def generate(self, context: Dict) -> bytes:
        """Generate fake credentials"""
        cred_type = context.get('credential_type', 'api_key')
        
        if cred_type == 'api_key':
            return self._generate_api_key()
        elif cred_type == 'database':
            return self._generate_database_creds()
        elif cred_type == 'aws':
            return self._generate_aws_creds()
        else:
            return self._generate_generic_creds()
    
    def _generate_api_key(self) -> bytes:
        """
        Generate fake API key.
        
        Format matches real API keys to fool attackers.
        """
        # Generate realistic-looking API key
        prefix = random.choice(['sk_live_', 'pk_test_', 'api_key_'])
        key = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
        
        content = f"""
# API Configuration
# DO NOT COMMIT TO VERSION CONTROL

API_KEY={prefix}{key}
API_SECRET={''.join(random.choices(string.ascii_letters + string.digits, k=64))}
API_ENDPOINT=https://api.example.com/v1

# Last rotated: {datetime.now().strftime('%Y-%m-%d')}
"""
        return content.encode('utf-8')
    
    def _generate_database_creds(self) -> bytes:
        """Generate fake database credentials"""
        content = f"""
# Database Configuration

DB_HOST=prod-db-01.internal.company.com
DB_PORT=5432
DB_NAME=production_db
DB_USER=app_user
DB_PASSWORD={self._generate_realistic_password()}

# Connection string
DATABASE_URL=postgresql://app_user:{self._generate_realistic_password()}@prod-db-01.internal.company.com:5432/production_db
"""
        return content.encode('utf-8')
    
    @staticmethod
    def _generate_realistic_password() -> str:
        """
        Generate password that looks real.
        
        Follows common password patterns:
        - Mix of upper/lower/numbers/symbols
        - 12-16 characters
        - Looks like something a human would create
        """
        words = ['Secure', 'Password', 'Admin', 'Prod', 'System']
        word = random.choice(words)
        number = random.randint(100, 999)
        symbol = random.choice(['!', '@', '#', '$', '&'])
        
        return f"{word}{number}{symbol}{random.randint(10, 99)}"
```

**Learning Points:**
- Realism is crucial - attackers will spot obvious fakes
- Use real data generation libraries (Faker)
- Match file metadata to environment
- Context-awareness makes decoys more effective
- Honeytokens (fake credentials) are powerful detection tools


### Phase 5: Modern React Dashboard (Weeks 9-11)

**What We're Building:**
A beautiful, real-time security operations center

**Key Concepts to Learn:**
- React components and hooks
- WebSocket for real-time updates
- State management (Redux/Context)
- Data visualization (Chart.js, D3.js)
- Modern UI/UX patterns

**Step 5.1: Dashboard Architecture**

```
frontend/dashboard/
├── src/
│   ├── components/
│   │   ├── Dashboard/
│   │   │   ├── Dashboard.tsx
│   │   │   ├── Dashboard.css
│   │   │   └── index.ts
│   │   ├── ScoreChart/
│   │   ├── AttackTimeline/
│   │   ├── DecoyHeatmap/
│   │   ├── AlertCard/
│   │   └── RoleView/
│   ├── hooks/
│   │   ├── useWebSocket.ts
│   │   ├── useRealTimeData.ts
│   │   └── useAuth.ts
│   ├── services/
│   │   ├── api.ts
│   │   └── websocket.ts
│   ├── store/
│   │   ├── slices/
│   │   └── store.ts
│   ├── types/
│   │   └── index.ts
│   └── App.tsx
└── package.json
```

**Step 5.2: Real-Time Score Chart Component**

```typescript
// frontend/dashboard/src/components/ScoreChart/ScoreChart.tsx

import React, { useEffect, useRef } from 'react';
import { Line } from 'react-chartjs-2';
import { useRealTimeData } from '../../hooks/useRealTimeData';
import './ScoreChart.css';

interface ScoreData {
  timestamp: string;
  score: number;
  userId: string;
  severity: 'low' | 'medium' | 'high' | 'critical';
}

export const ScoreChart: React.FC = () => {
  /**
   * Real-time suspicious score chart.
   * 
   * Shows live updates of user suspicious scores.
   * Color-coded by severity for quick visual assessment.
   */
  
  // Custom hook for WebSocket data
  const { scores, isConnected } = useRealTimeData<ScoreData>('scores');
  
  // Prepare chart data
  const chartData = {
    labels: scores.map(s => new Date(s.timestamp).toLocaleTimeString()),
    datasets: [
      {
        label: 'Suspicious Score',
        data: scores.map(s => s.score),
        borderColor: scores.map(s => getSeverityColor(s.severity)),
        backgroundColor: scores.map(s => getSeverityColor(s.severity, 0.1)),
        tension: 0.4, // Smooth curves
        fill: true,
      }
    ]
  };
  
  const chartOptions = {
    responsive: true,
    maintainAspectRatio: false,
    animation: {
      duration: 750, // Smooth animations
      easing: 'easeInOutQuart'
    },
    scales: {
      y: {
        beginAtZero: true,
        max: 100,
        ticks: {
          callback: (value: number) => `${value}%`
        }
      }
    },
    plugins: {
      legend: {
        display: true,
        position: 'top' as const,
      },
      tooltip: {
        callbacks: {
          label: (context: any) => {
            const score = context.parsed.y;
            const severity = scores[context.dataIndex]?.severity;
            return `Score: ${score} (${severity})`;
          }
        }
      }
    }
  };
  
  return (
    <div className="score-chart-container">
      <div className="chart-header">
        <h2>Real-Time Suspicious Scores</h2>
        <div className={`connection-status ${isConnected ? 'connected' : 'disconnected'}`}>
          {isConnected ? '🟢 Live' : '🔴 Disconnected'}
        </div>
      </div>
      
      <div className="chart-wrapper">
        <Line data={chartData} options={chartOptions} />
      </div>
      
      <div className="severity-legend">
        <span className="legend-item low">Low (0-25)</span>
        <span className="legend-item medium">Medium (26-50)</span>
        <span className="legend-item high">High (51-75)</span>
        <span className="legend-item critical">Critical (76-100)</span>
      </div>
    </div>
  );
};

function getSeverityColor(severity: string, alpha: number = 1): string {
  const colors = {
    low: `rgba(52, 211, 153, ${alpha})`,      // Green
    medium: `rgba(251, 191, 36, ${alpha})`,   // Yellow
    high: `rgba(251, 146, 60, ${alpha})`,     // Orange
    critical: `rgba(239, 68, 68, ${alpha})`   // Red
  };
  return colors[severity as keyof typeof colors] || colors.low;
}
```

**Step 5.3: Custom WebSocket Hook**

```typescript
// frontend/dashboard/src/hooks/useRealTimeData.ts

import { useState, useEffect, useCallback } from 'react';
import { websocketService } from '../services/websocket';

/**
 * Custom hook for real-time data via WebSocket.
 * 
 * This abstracts away WebSocket complexity and provides
 * a simple interface for components.
 * 
 * Usage:
 *   const { data, isConnected } = useRealTimeData<ScoreData>('scores');
 */
export function useRealTimeData<T>(channel: string) {
  const [data, setData] = useState<T[]>([]);
  const [isConnected, setIsConnected] = useState(false);
  const [error, setError] = useState<string | null>(null);
  
  useEffect(() => {
    // Connect to WebSocket
    websocketService.connect();
    
    // Subscribe to channel
    const unsubscribe = websocketService.subscribe(channel, (newData: T) => {
      setData(prevData => {
        // Keep last 50 data points for performance
        const updated = [...prevData, newData];
        return updated.slice(-50);
      });
    });
    
    // Listen for connection status
    websocketService.onConnectionChange((connected) => {
      setIsConnected(connected);
    });
    
    // Listen for errors
    websocketService.onError((err) => {
      setError(err.message);
    });
    
    // Cleanup on unmount
    return () => {
      unsubscribe();
      websocketService.disconnect();
    };
  }, [channel]);
  
  const clearData = useCallback(() => {
    setData([]);
  }, []);
  
  return {
    data,
    isConnected,
    error,
    clearData
  };
}
```

**Step 5.4: WebSocket Service**

```typescript
// frontend/dashboard/src/services/websocket.ts

type MessageHandler<T> = (data: T) => void;
type ConnectionHandler = (connected: boolean) => void;
type ErrorHandler = (error: Error) => void;

class WebSocketService {
  /**
   * Manages WebSocket connection for real-time updates.
   * 
   * Features:
   * - Automatic reconnection
   * - Message routing by channel
   * - Connection status tracking
   * - Error handling
   */
  
  private ws: WebSocket | null = null;
  private url: string;
  private reconnectAttempts = 0;
  private maxReconnectAttempts = 5;
  private reconnectDelay = 1000; // Start with 1 second
  
  private subscribers: Map<string, Set<MessageHandler<any>>> = new Map();
  private connectionHandlers: Set<ConnectionHandler> = new Set();
  private errorHandlers: Set<ErrorHandler> = new Set();
  
  constructor() {
    // Get WebSocket URL from environment
    this.url = process.env.REACT_APP_WS_URL || 'ws://localhost:8080/ws';
  }
  
  connect(): void {
    if (this.ws?.readyState === WebSocket.OPEN) {
      return; // Already connected
    }
    
    console.log('🔌 Connecting to WebSocket...');
    
    try {
      this.ws = new WebSocket(this.url);
      
      this.ws.onopen = () => {
        console.log('✅ WebSocket connected');
        this.reconnectAttempts = 0;
        this.reconnectDelay = 1000;
        this.notifyConnectionChange(true);
      };
      
      this.ws.onmessage = (event) => {
        this.handleMessage(event.data);
      };
      
      this.ws.onerror = (error) => {
        console.error('❌ WebSocket error:', error);
        this.notifyError(new Error('WebSocket connection error'));
      };
      
      this.ws.onclose = () => {
        console.log('🔌 WebSocket disconnected');
        this.notifyConnectionChange(false);
        this.attemptReconnect();
      };
      
    } catch (error) {
      console.error('Failed to create WebSocket:', error);
      this.notifyError(error as Error);
    }
  }
  
  disconnect(): void {
    if (this.ws) {
      this.ws.close();
      this.ws = null;
    }
  }
  
  subscribe<T>(channel: string, handler: MessageHandler<T>): () => void {
    /**
     * Subscribe to a specific data channel.
     * 
     * Returns an unsubscribe function for cleanup.
     */
    if (!this.subscribers.has(channel)) {
      this.subscribers.set(channel, new Set());
    }
    
    this.subscribers.get(channel)!.add(handler);
    
    // Send subscription message to server
    this.send({
      type: 'subscribe',
      channel: channel
    });
    
    // Return unsubscribe function
    return () => {
      const handlers = this.subscribers.get(channel);
      if (handlers) {
        handlers.delete(handler);
        if (handlers.size === 0) {
          this.subscribers.delete(channel);
          // Unsubscribe from server
          this.send({
            type: 'unsubscribe',
            channel: channel
          });
        }
      }
    };
  }
  
  private handleMessage(data: string): void {
    try {
      const message = JSON.parse(data);
      const { channel, payload } = message;
      
      // Route message to subscribers
      const handlers = this.subscribers.get(channel);
      if (handlers) {
        handlers.forEach(handler => handler(payload));
      }
    } catch (error) {
      console.error('Failed to parse WebSocket message:', error);
    }
  }
  
  private send(data: any): void {
    if (this.ws?.readyState === WebSocket.OPEN) {
      this.ws.send(JSON.stringify(data));
    }
  }
  
  private attemptReconnect(): void {
    if (this.reconnectAttempts >= this.maxReconnectAttempts) {
      console.error('Max reconnection attempts reached');
      return;
    }
    
    this.reconnectAttempts++;
    
    console.log(`Reconnecting in ${this.reconnectDelay}ms (attempt ${this.reconnectAttempts})`);
    
    setTimeout(() => {
      this.connect();
    }, this.reconnectDelay);
    
    // Exponential backoff
    this.reconnectDelay *= 2;
  }
  
  onConnectionChange(handler: ConnectionHandler): void {
    this.connectionHandlers.add(handler);
  }
  
  onError(handler: ErrorHandler): void {
    this.errorHandlers.add(handler);
  }
  
  private notifyConnectionChange(connected: boolean): void {
    this.connectionHandlers.forEach(handler => handler(connected));
  }
  
  private notifyError(error: Error): void {
    this.errorHandlers.forEach(handler => handler(error));
  }
}

export const websocketService = new WebSocketService();
```

**Step 5.5: Alert Card Component**

```typescript
// frontend/dashboard/src/components/AlertCard/AlertCard.tsx

import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import './AlertCard.css';

interface Alert {
  id: string;
  severity: 'low' | 'medium' | 'high' | 'critical';
  title: string;
  description: string;
  timestamp: string;
  userId: string;
  score: number;
}

interface AlertCardProps {
  alert: Alert;
  onDismiss: (id: string) => void;
  onInvestigate: (id: string) => void;
}

export const AlertCard: React.FC<AlertCardProps> = ({ 
  alert, 
  onDismiss, 
  onInvestigate 
}) => {
  /**
   * Animated alert card with smooth transitions.
   * 
   * Uses Framer Motion for professional animations.
   */
  
  const [isExpanded, setIsExpanded] = useState(false);
  
  const severityConfig = {
    low: { icon: 'ℹ️', color: '#10b981' },
    medium: { icon: '⚠️', color: '#f59e0b' },
    high: { icon: '🔥', color: '#f97316' },
    critical: { icon: '🚨', color: '#ef4444' }
  };
  
  const config = severityConfig[alert.severity];
  
  return (
    <motion.div
      className={`alert-card severity-${alert.severity}`}
      initial={{ opacity: 0, y: -20, scale: 0.95 }}
      animate={{ opacity: 1, y: 0, scale: 1 }}
      exit={{ opacity: 0, x: 100, scale: 0.95 }}
      transition={{ duration: 0.3, ease: 'easeOut' }}
      layout
    >
      <div className="alert-header" onClick={() => setIsExpanded(!isExpanded)}>
        <div className="alert-icon" style={{ color: config.color }}>
          {config.icon}
        </div>
        
        <div className="alert-title-section">
          <h3>{alert.title}</h3>
          <span className="alert-timestamp">
            {new Date(alert.timestamp).toLocaleString()}
          </span>
        </div>
        
        <div className="alert-score">
          <span className="score-value">{alert.score}</span>
          <span className="score-label">Risk Score</span>
        </div>
        
        <motion.div
          className="expand-icon"
          animate={{ rotate: isExpanded ? 180 : 0 }}
          transition={{ duration: 0.2 }}
        >
          ▼
        </motion.div>
      </div>
      
      <AnimatePresence>
        {isExpanded && (
          <motion.div
            className="alert-details"
            initial={{ height: 0, opacity: 0 }}
            animate={{ height: 'auto', opacity: 1 }}
            exit={{ height: 0, opacity: 0 }}
            transition={{ duration: 0.2 }}
          >
            <p className="alert-description">{alert.description}</p>
            
            <div className="alert-metadata">
              <div className="metadata-item">
                <span className="label">User ID:</span>
                <span className="value">{alert.userId}</span>
              </div>
              <div className="metadata-item">
                <span className="label">Severity:</span>
                <span className="value">{alert.severity.toUpperCase()}</span>
              </div>
            </div>
            
            <div className="alert-actions">
              <button 
                className="btn btn-primary"
                onClick={() => onInvestigate(alert.id)}
              >
                🔍 Investigate
              </button>
              <button 
                className="btn btn-secondary"
                onClick={() => onDismiss(alert.id)}
              >
                ✓ Dismiss
              </button>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </motion.div>
  );
};
```

**Learning Points:**
- React hooks manage component state and side effects
- WebSocket enables real-time updates without polling
- Framer Motion provides smooth, professional animations
- Component composition keeps code organized
- Custom hooks abstract complex logic
- TypeScript provides type safety


---

## Security Principles We Follow

### 1. Defense in Depth

**Concept:** Multiple layers of security, so if one fails, others protect you.

**Our Implementation:**
```
Layer 1: Authentication (API keys, OAuth)
Layer 2: Authorization (role-based access control)
Layer 3: Input validation (reject bad data)
Layer 4: Rate limiting (prevent abuse)
Layer 5: Audit logging (track everything)
Layer 6: Encryption (protect data at rest and in transit)
```

**Example:**
```python
@require_authentication  # Layer 1
@require_role('admin')   # Layer 2
@validate_input          # Layer 3
@rate_limit(100)         # Layer 4
def delete_user(user_id: str):
    audit_log.record('delete_user', user_id)  # Layer 5
    # ... actual deletion
```

### 2. Principle of Least Privilege

**Concept:** Give users/processes only the minimum permissions they need.

**Bad Example:**
```python
# Running as root - can do ANYTHING
os.system('rm -rf /important/data')  # Oops!
```

**Good Example:**
```python
# Running as dedicated user with limited permissions
# Can only access /var/honeypot directory
# Cannot delete system files
```

### 3. Fail Securely

**Concept:** When something goes wrong, fail in a way that maintains security.

**Bad Example:**
```python
try:
    check_authentication(token)
except Exception:
    # Error occurred, let them in anyway
    return True  # DANGEROUS!
```

**Good Example:**
```python
try:
    check_authentication(token)
except Exception as e:
    audit_log.error(f"Auth failed: {e}")
    return False  # Deny access on error
```

### 4. Never Trust User Input

**Concept:** All input is potentially malicious until proven otherwise.

**Example:**
```python
def search_files(user_query: str):
    # BAD: SQL injection vulnerability
    query = f"SELECT * FROM files WHERE name = '{user_query}'"
    
    # GOOD: Parameterized query
    query = "SELECT * FROM files WHERE name = ?"
    cursor.execute(query, (user_query,))
```

### 5. Security Through Obscurity is Not Security

**Concept:** Don't rely on keeping your methods secret.

**Bad Approach:**
```python
# "Security" through obscurity
SECRET_ADMIN_URL = "/x7k2p9q/admin"  # Attackers will find this
```

**Good Approach:**
```python
# Real security through authentication
@require_authentication
@require_role('admin')
def admin_panel():
    # Properly secured, URL doesn't matter
```

---

## Testing Like a Pro

### Unit Testing

**What:** Test individual functions in isolation

**Example:**
```python
# tests/unit/test_rule_scorer.py

import pytest
from honeypot.scoring.rule_scorer import RuleScorer

def test_abnormal_frequency_detection():
    """
    Test that abnormal access frequency is detected.
    
    Given: User normally accesses 50 files/hour
    When: User accesses 200 files/hour
    Then: Abnormal frequency should be flagged
    """
    scorer = RuleScorer()
    
    # Create test data
    events = create_test_events(count=200, timespan_hours=1)
    baseline = {'avg_hourly_events': 50}
    
    # Test
    result = scorer._check_abnormal_frequency(events, baseline)
    
    # Assert
    assert result == True, "Should detect abnormal frequency"

def test_privilege_escalation_detection():
    """Test that privilege escalation attempts are detected"""
    scorer = RuleScorer()
    
    # Create event with admin access attempt
    events = [
        SecurityEvent(
            user_id='user123',
            source_ip='192.168.1.100',
            event_type='file_access',
            action='admin_panel_access',
            target='/admin/users',
            timestamp=datetime.now(),
            suspicious_score=0,
            metadata={'permission_denied': True, 'required_role': 'admin'}
        )
    ]
    
    result = scorer._check_privilege_escalation(events)
    assert result == True
```

### Property-Based Testing

**What:** Test properties that should always be true, with random inputs

**Example:**
```python
# tests/property/test_scoring_properties.py

from hypothesis import given, strategies as st
from honeypot.scoring.hybrid_scorer import HybridScorer

@given(
    rule_score=st.floats(min_value=0, max_value=100),
    ml_score=st.floats(min_value=0, max_value=100)
)
def test_score_always_in_range(rule_score, ml_score):
    """
    Property: Final score should always be between 0 and 100.
    
    This tests with random inputs to ensure the property holds.
    """
    scorer = HybridScorer(rule_weight=0.4, ml_weight=0.6)
    
    # Calculate score
    final_score = (rule_score * 0.4) + (ml_score * 0.6)
    
    # Property: Score must be in valid range
    assert 0 <= final_score <= 100

@given(
    events=st.lists(
        st.builds(SecurityEvent, ...),
        min_size=1,
        max_size=100
    )
)
def test_logging_never_loses_data(events):
    """
    Property: Logging should never lose events.
    
    For any list of events, all should be retrievable.
    """
    logger = ActivityLogger()
    
    # Log all events
    for event in events:
        logger.log_event(event)
    
    # Retrieve all events
    retrieved = logger.query_events(filter={})
    
    # Property: All events should be present
    assert len(retrieved) == len(events)
```

### Integration Testing

**What:** Test how components work together

**Example:**
```python
# tests/integration/test_attack_flow.py

async def test_full_attack_detection_flow():
    """
    Test complete flow: Attack → Detection → Decoy → Alert
    
    This simulates a real attack scenario.
    """
    # Setup
    agent = CoreAgent(config)
    await agent.start()
    
    # Simulate attacker behavior
    attacker_id = 'attacker_001'
    
    # Step 1: Normal activity (establish baseline)
    for i in range(50):
        await simulate_normal_activity(attacker_id)
    
    # Step 2: Suspicious activity
    for i in range(10):
        await simulate_privilege_escalation(attacker_id)
    
    # Step 3: Verify score increased
    score = await agent.scoring_engine.get_score(attacker_id)
    assert score > 60, "Score should increase with suspicious activity"
    
    # Step 4: Verify decoys were deployed
    decoys = await agent.decoy_manager.get_decoys_for_user(attacker_id)
    assert len(decoys) > 0, "Decoys should be deployed"
    
    # Step 5: Simulate decoy interaction
    await simulate_decoy_access(attacker_id, decoys[0])
    
    # Step 6: Verify alert was sent
    alerts = await agent.alert_system.get_recent_alerts()
    assert any(a.user_id == attacker_id for a in alerts), "Alert should be sent"
    
    # Cleanup
    await agent.stop()
```

---

## Deployment and Operations

### Development Environment

```bash
# 1. Clone repository
git clone https://github.com/company/honeypot-agent.git
cd honeypot-agent

# 2. Set up Python environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

# 3. Set up database
python scripts/init_db.py

# 4. Configure
cp config/config.example.yaml config/config.yaml
# Edit config.yaml with your settings

# 5. Run tests
pytest

# 6. Start development server
python -m honeypot.main --config config/config.yaml
```

### Production Deployment (Docker)

```dockerfile
# Dockerfile

FROM python:3.11-slim

# Security: Run as non-root user
RUN useradd -m -u 1000 honeypot

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY src/ ./src/
COPY config/ ./config/

# Set ownership
RUN chown -R honeypot:honeypot /app

# Switch to non-root user
USER honeypot

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD python -c "import requests; requests.get('http://localhost:8080/health')"

# Run application
CMD ["python", "-m", "honeypot.main", "--config", "config/config.yaml"]
```

```yaml
# docker-compose.yml

version: '3.8'

services:
  honeypot-agent:
    build: .
    ports:
      - "8080:8080"
    environment:
      - DB_PASSWORD=${DB_PASSWORD}
      - API_KEY=${API_KEY}
    volumes:
      - ./config:/app/config
      - ./data:/app/data
    depends_on:
      - postgres
    restart: unless-stopped
  
  postgres:
    image: postgres:15
    environment:
      - POSTGRES_DB=honeypot_db
      - POSTGRES_USER=honeypot_user
      - POSTGRES_PASSWORD=${DB_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    restart: unless-stopped
  
  dashboard:
    build: ./frontend/dashboard
    ports:
      - "3000:3000"
    environment:
      - REACT_APP_API_URL=http://localhost:8080
      - REACT_APP_WS_URL=ws://localhost:8080/ws
    depends_on:
      - honeypot-agent
    restart: unless-stopped

volumes:
  postgres_data:
```

### Monitoring and Observability

```python
# src/honeypot/observability/metrics.py

from prometheus_client import Counter, Histogram, Gauge

# Define metrics
suspicious_score_gauge = Gauge(
    'honeypot_suspicious_score',
    'Current suspicious score for users',
    ['user_id']
)

decoy_interactions_counter = Counter(
    'honeypot_decoy_interactions_total',
    'Total number of decoy interactions',
    ['decoy_type']
)

alert_latency_histogram = Histogram(
    'honeypot_alert_latency_seconds',
    'Time from detection to alert',
    buckets=[0.1, 0.5, 1.0, 2.0, 5.0]
)

# Use in code
def send_alert(alert):
    start_time = time.time()
    # ... send alert
    latency = time.time() - start_time
    alert_latency_histogram.observe(latency)
```

---

## Learning Resources

### Books
1. **"The Web Application Hacker's Handbook"** - Understand attacker mindset
2. **"Designing Data-Intensive Applications"** - System architecture
3. **"Python Machine Learning"** - ML fundamentals
4. **"React Up & Running"** - Modern frontend development

### Online Courses
1. **Coursera: Machine Learning** (Andrew Ng) - ML basics
2. **Udemy: Complete React Developer** - React mastery
3. **SANS SEC504** - Hacker techniques and incident handling

### Practice Platforms
1. **HackTheBox** - Practice security skills
2. **TryHackMe** - Guided security challenges
3. **LeetCode** - Algorithm practice

### Communities
1. **r/netsec** - Security news and discussions
2. **OWASP** - Web security community
3. **React Discord** - React help and tips

---

## Next Steps

Congratulations! You now understand the architecture and concepts behind building an AI-driven cybersecurity deception platform.

**Your Learning Path:**

1. **Week 1-2:** Build the foundation (data models, configuration)
2. **Week 3-4:** Implement scoring engine (rules + ML)
3. **Week 5-6:** Build autonomous agent
4. **Week 7-8:** Create decoy generation system
5. **Week 9-11:** Develop React dashboard
6. **Week 12:** Integration, testing, deployment

**Remember:**
- Start simple, add complexity gradually
- Test everything thoroughly
- Security is not optional
- Learn from failures
- Ask questions when stuck

**You've got this! 🚀**

