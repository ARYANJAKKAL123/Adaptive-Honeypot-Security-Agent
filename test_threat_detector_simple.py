"""Simple test to verify threat_detector works"""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from src.monitor.threat_detector import ThreatDetector

print("Testing ThreatDetector...")
detector = ThreatDetector()
print(f"✅ Created! Initial score: {detector.threat_score}")

detector.add_event("created", "test.txt")
print(f"✅ Added event! Score: {detector.threat_score}")

print("\n✅ All basic tests passed!")
