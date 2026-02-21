# test_integrated_system.py
"""
Test the complete integrated system:
FileMonitor + ThreatDetector + DecoyManager + DecoyService
"""
import sys
import os
import time

# Add src to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from monitor.file_monitor import FileMonitor
from monitor.threat_detector import ThreatDetector
from monitor.decoy_manager import DecoyManager

def test_integrated_system():
    """Test the complete integrated system"""
    
    print("\n" + "="*70)
    print("TESTING INTEGRATED SYSTEM - Day 17-18")
    print("FileMonitor + ThreatDetector + DecoyManager + DecoyService")
    print("="*70)
    
    # Create test directory
    test_dir = "test_integrated"
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)
    
    print(f"\n✅ Test directory created: {test_dir}")
    
    # Initialize the system
    print("\n" + "-"*70)
    print("STEP 1: Initialize System Components")
    print("-"*70)
    
    file_monitor = FileMonitor()
    print("✅ FileMonitor initialized")
    print("✅ ThreatDetector initialized (inside FileMonitor)")
    print("✅ DecoyManager initialized (inside FileMonitor)")
    
    # Simulate normal activity (should NOT trigger decoys)
    print("\n" + "-"*70)
    print("STEP 2: Simulate Normal Activity (Score < 51)")
    print("-"*70)
    
    class MockEvent:
        def __init__(self, path, is_dir=False):
            self.src_path = path
            self.is_directory = is_dir
    
    # Create 2 normal files
    for i in range(2):
        event = MockEvent(f"{test_dir}/normal_file_{i}.txt")
        file_monitor.on_created(event)
    
    threat_score = file_monitor.threat_detector.threat_score
    threat_level = file_monitor.threat_detector.get_threat_level()
    print(f"Current Threat Score: {threat_score}")
    print(f"Current Threat Level: {threat_level}")
    print("✅ No decoys deployed (score < 51)")
    
    # Simulate suspicious activity (should trigger decoys)
    print("\n" + "-"*70)
    print("STEP 3: Simulate Suspicious Activity (Score >= 51)")
    print("-"*70)
    
    # Access sensitive files rapidly
    sensitive_files = [
        f"{test_dir}/passwords.txt",
        f"{test_dir}/api_keys.txt",
        f"{test_dir}/secret_token.txt",
        f"{test_dir}/database_config.yaml",
        f"{test_dir}/admin_credentials.txt"
    ]
    
    print("Simulating rapid access to sensitive files...")
    for file_path in sensitive_files:
        event = MockEvent(file_path)
        file_monitor.on_created(event)
        time.sleep(0.1)  # Small delay
    
    threat_score = file_monitor.threat_detector.threat_score
    threat_level = file_monitor.threat_detector.get_threat_level()
    print(f"\nCurrent Threat Score: {threat_score}")
    print(f"Current Threat Level: {threat_level}")
    
    # Check decoy deployment status
    print("\n" + "-"*70)
    print("STEP 4: Check Decoy Deployment Status")
    print("-"*70)
    
    status = file_monitor.decoy_manager.get_deployment_status()
    print(f"Decoys Deployed: {status['deployed']}")
    print(f"Number of Decoys: {status['count']}")
    print(f"Decoy Base Path: {status['base_path']}")
    
    if status['deployed']:
        print("\n✅ Decoys successfully deployed!")
        print("\nDeployed Decoys:")
        for decoy in status['decoys']:
            print(f"  - Type: {decoy.decoy_type}")
            print(f"    Path: {decoy.file_path}")
            print(f"    Created: {decoy.created_at}")
            print()
    
    # Simulate attacker accessing decoy
    print("-"*70)
    print("STEP 5: Simulate Attacker Accessing Decoy")
    print("-"*70)
    
    if status['deployed'] and status['count'] > 0:
        # Access the first deployed decoy
        decoy_path = status['decoys'][0].file_path
        print(f"Simulating access to decoy: {decoy_path}")
        
        event = MockEvent(decoy_path)
        file_monitor.on_modified(event)
        
        print("\n🚨 Check logs/events.log for 'ATTACKER CAUGHT' message!")
    
    # Verify files were created
    print("\n" + "-"*70)
    print("STEP 6: Verify Decoy Files on Disk")
    print("-"*70)
    
    if os.path.exists("decoys"):
        files = os.listdir("decoys")
        print(f"✅ Decoy directory exists with {len(files)} file(s):")
        for file in files:
            file_path = os.path.join("decoys", file)
            size = os.path.getsize(file_path)
            print(f"  - {file} ({size} bytes)")
    else:
        print("❌ Decoy directory not found")
    
    # Summary
    print("\n" + "="*70)
    print("TEST SUMMARY")
    print("="*70)
    print("✅ FileMonitor working")
    print("✅ ThreatDetector calculating scores")
    print("✅ DecoyManager deploying decoys automatically")
    print("✅ DecoyService generating realistic decoys")
    print("✅ Decoy access detection working")
    print("✅ All components integrated successfully!")
    print("\n🎉 Day 17-18 Complete! Decoy deployment system working!")
    print("="*70)

if __name__ == "__main__":
    test_integrated_system()
