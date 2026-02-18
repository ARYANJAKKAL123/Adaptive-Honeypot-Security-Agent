#!/usr/bin/env python3
"""
Week 2 Review - System Test
Tests all components to ensure they work correctly
"""

print("\n" + "="*60)
print("WEEK 2 SYSTEM REVIEW - TESTING ALL COMPONENTS")
print("="*60)

# Test 1: Import all modules
print("\n[1/5] Testing imports...")
try:
    from src.monitor.logger import EventLogger
    from src.monitor.threat_detector import ThreatDetector
    from src.monitor.file_monitor import FileMonitor
    print("✅ All imports successful!")
except Exception as e:
    print(f"❌ Import failed: {e}")
    exit(1)

# Test 2: Create EventLogger
print("\n[2/5] Testing EventLogger...")
try:
    logger = EventLogger()
    logger.log_info("Test info message")
    logger.log_warning("Test warning message")
    logger.log_error("Test error message")
    print("✅ EventLogger working!")
except Exception as e:
    print(f"❌ EventLogger failed: {e}")
    exit(1)

# Test 3: Create ThreatDetector
print("\n[3/5] Testing ThreatDetector...")
try:
    detector = ThreatDetector()
    
    # Test normal file
    detector.add_event("created", "normal.txt")
    score1 = detector.threat_score
    level1 = detector.get_threat_level()
    print(f"   Normal file: Score={score1}, Level={level1}")
    
    # Test sensitive file
    detector.add_event("created", "passwords.txt")
    score2 = detector.threat_score
    level2 = detector.get_threat_level()
    print(f"   Sensitive file: Score={score2}, Level={level2}")
    
    print("✅ ThreatDetector working!")
except Exception as e:
    print(f"❌ ThreatDetector failed: {e}")
    exit(1)

# Test 4: Create FileMonitor
print("\n[4/5] Testing FileMonitor...")
try:
    monitor = FileMonitor()
    print("✅ FileMonitor created with integrated ThreatDetector!")
except Exception as e:
    print(f"❌ FileMonitor failed: {e}")
    exit(1)

# Test 5: Check integration
print("\n[5/5] Testing integration...")
try:
    # Verify FileMonitor has ThreatDetector
    assert hasattr(monitor, 'threat_detector'), "FileMonitor missing threat_detector"
    assert hasattr(monitor, 'logger'), "FileMonitor missing logger"
    
    # Verify ThreatDetector has logger
    assert hasattr(detector, 'logger'), "ThreatDetector missing logger"
    
    print("✅ All components properly integrated!")
except Exception as e:
    print(f"❌ Integration check failed: {e}")
    exit(1)

# Summary
print("\n" + "="*60)
print("SYSTEM REVIEW COMPLETE")
print("="*60)
print("\n✅ All tests passed!")
print("✅ EventLogger: Working")
print("✅ ThreatDetector: Working")
print("✅ FileMonitor: Working")
print("✅ Integration: Working")
print("\n🎉 Your Week 1-2 system is fully functional!")
print("\nNext: Day 15-16 - Decoy File Generator")
print("="*60 + "\n")
