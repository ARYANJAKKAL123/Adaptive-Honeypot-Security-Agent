import time
from datetime import datetime
from .logger import EventLogger


class ThreatDetector:
    """
    Analyzes file system events and calculates threat scores
    Detects suspicious patterns and assigns threat levels
    """
    
    def __init__(self):
        """
        Initialize the threat detector
        Sets up event tracking and scoring system
        """
        # Event history - stores recent file events
        self.events = []
        
        # Current threat score (0-100)
        self.threat_score = 0
        
        # Time window for event analysis (5 minutes = 300 seconds)
        self.time_window = 300
        
        # Rapid access threshold (events in 10 seconds)
        self.rapid_access_window = 10
        self.rapid_access_threshold = 5
        
        # Deletion threshold (deletions in 30 seconds)
        self.deletion_window = 30
        self.deletion_threshold = 3
        
        # Sensitive file keywords
        self.sensitive_keywords = [
            'password', 'passwd', 'pwd',
            'secret', 'key', 'token',
            'config', 'credential', 'auth',
            'private', 'id_rsa', 'ssh',
            'api_key', 'database', 'backup'
        ]
        
        # Initialize logger
        self.logger = EventLogger()
        self.logger.log_info("ThreatDetector initialized")
    
    def add_event(self, event_type, file_path):
        """
        Add a new file system event and update threat score
        
        Args:
            event_type: Type of event ('created', 'modified', 'deleted')
            file_path: Path to the file involved
        """
        # Get current timestamp
        timestamp = time.time()
        
        # Create event dictionary
        event = {
            'type': event_type,
            'path': file_path,
            'time': timestamp
        }
        
        # Add to event history
        self.events.append(event)
        
        # Clean up old events (older than time_window)
        current_time = time.time()
        self.events = [e for e in self.events 
                       if current_time - e['time'] < self.time_window]
        
        # Calculate new threat score
        old_score = self.threat_score
        self.threat_score = self.calculate_threat_score()
        
        # Log if threat level changed significantly
        if self.threat_score > old_score and self.threat_score >= 50:
            threat_level = self.get_threat_level()
            self.logger.log_warning(
                f"Threat detected! Level: {threat_level}, "
                f"Score: {self.threat_score}, File: {file_path}"
            )
    
    def calculate_threat_score(self):
        """
        Calculate total threat score based on all detection rules
        
        Returns:
            int: Threat score (0-100)
        """
        score = 0
        
        # Check for rapid file access
        score += self.check_rapid_access()
        
        # Check for unusual time access
        score += self.check_unusual_time()
        
        # Check for multiple deletions
        score += self.check_deletions()
        
        # Check each event for sensitive files
        for event in self.events:
            score += self.check_sensitive_files(event['path'])
        
        # Cap score at 100
        return min(score, 100)
    
    def check_rapid_access(self):
        """
        Check for rapid file access pattern
        
        Returns:
            int: Points to add (0 or 20)
        """
        current_time = time.time()
        
        # Count events in the rapid access window
        recent_events = [e for e in self.events 
                        if current_time - e['time'] < self.rapid_access_window]
        
        # If too many events in short time, it's suspicious
        if len(recent_events) > self.rapid_access_threshold:
            return 20
        
        return 0
    
    def check_unusual_time(self):
        """
        Check if activity is happening at unusual hours
        
        Returns:
            int: Points to add (0 or 15)
        """
        current_hour = datetime.now().hour
        
        # Activity between midnight and 5 AM is suspicious
        if 0 <= current_hour < 5:
            return 15
        
        return 0
    
    def check_sensitive_files(self, file_path):
        """
        Check if file path contains sensitive keywords
        
        Args:
            file_path: Path to check
            
        Returns:
            int: Points to add (0 or 25)
        """
        # Convert to lowercase for case-insensitive matching
        file_path_lower = file_path.lower()
        
        # Check if any sensitive keyword is in the path
        for keyword in self.sensitive_keywords:
            if keyword in file_path_lower:
                return 25
        
        return 0
    
    def check_deletions(self):
        """
        Check for multiple file deletions in short time
        
        Returns:
            int: Points to add (0 or 30)
        """
        current_time = time.time()
        
        # Count deletion events in the deletion window
        recent_deletes = [e for e in self.events 
                         if e['type'] == 'deleted' 
                         and current_time - e['time'] < self.deletion_window]
        
        # If too many deletions, it's very suspicious
        if len(recent_deletes) > self.deletion_threshold:
            return 30
        
        return 0
    
    def get_threat_level(self):
        """
        Convert numeric score to threat level category
        
        Returns:
            str: Threat level ('Normal', 'Elevated', 'Suspicious', 'Critical')
        """
        if self.threat_score >= 71:
            return "Critical"
        elif self.threat_score >= 51:
            return "Suspicious"
        elif self.threat_score >= 31:
            return "Elevated"
        else:
            return "Normal"
    
    def get_threat_info(self):
        """
        Get detailed information about current threat status
        
        Returns:
            dict: Threat information including score, level, and event count
        """
        return {
            'score': self.threat_score,
            'level': self.get_threat_level(),
            'event_count': len(self.events),
            'recent_events': self.events[-5:] if self.events else []
        }


# Testing code
if __name__ == "__main__":
    """Test the threat detector with sample scenarios"""
    
    print("\n" + "="*60)
    print("TESTING THREAT DETECTOR")
    print("="*60)
    
    # Create detector
    detector = ThreatDetector()
    print("\n✅ ThreatDetector created")
    print(f"   Initial score: {detector.threat_score}")
    print(f"   Initial level: {detector.get_threat_level()}")
    
    # Test 1: Normal file access
    print("\n" + "-"*60)
    print("TEST 1: Normal file access")
    print("-"*60)
    detector.add_event("created", "document.txt")
    print(f"Score: {detector.threat_score} - Level: {detector.get_threat_level()}")
    
    # Test 2: Sensitive file
    print("\n" + "-"*60)
    print("TEST 2: Accessing sensitive file")
    print("-"*60)
    detector.add_event("modified", "passwords.txt")
    print(f"Score: {detector.threat_score} - Level: {detector.get_threat_level()}")
    
    # Test 3: Rapid access
    print("\n" + "-"*60)
    print("TEST 3: Rapid file access (6 files quickly)")
    print("-"*60)
    for i in range(6):
        detector.add_event("created", f"file{i}.txt")
    print(f"Score: {detector.threat_score} - Level: {detector.get_threat_level()}")
    
    # Test 4: Multiple deletions
    print("\n" + "-"*60)
    print("TEST 4: Multiple deletions")
    print("-"*60)
    for i in range(4):
        detector.add_event("deleted", f"old_file{i}.txt")
    print(f"Score: {detector.threat_score} - Level: {detector.get_threat_level()}")
    
    # Show final info
    print("\n" + "="*60)
    print("FINAL THREAT INFO")
    print("="*60)
    info = detector.get_threat_info()
    print(f"Score: {info['score']}")
    print(f"Level: {info['level']}")
    print(f"Total events tracked: {info['event_count']}")
    print("\n✅ All tests completed!")
