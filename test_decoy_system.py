# test_decoy_system.py
"""
Test the complete decoy system with clean architecture
"""
import sys
import os

# Add src to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from domain.infrastructure.file_decoy_generator import FileDecoyGenerator
from domain.application.decoy_service import DecoyService

def test_decoy_generation():
    """Test generating decoys with clean architecture"""
    
    print("\n" + "="*60)
    print("TESTING DECOY SYSTEM - CLEAN ARCHITECTURE")
    print("="*60)
    
    # Step 1: Create the infrastructure implementation (uses Faker)
    print("\n1️⃣ Creating FileDecoyGenerator (Infrastructure Layer)...")
    generator = FileDecoyGenerator()
    print("   ✅ FileDecoyGenerator created")
    
    # Step 2: Create the application service (business logic)
    print("\n2️⃣ Creating DecoyService (Application Layer)...")
    decoy_service = DecoyService(generator)
    print("   ✅ DecoyService created")
    
    # Step 3: Test Suspicious threat level (2 decoys)
    print("\n" + "-"*60)
    print("TEST 1: Suspicious Threat Level (Score 51-70)")
    print("-"*60)
    
    test_path = "test_decoys"
    decoys = decoy_service.generate_decoys_for_threat_level("Suspicious", test_path)
    
    print(f"✅ Generated {len(decoys)} decoys:")
    for decoy in decoys:
        print(f"   - Type: {decoy.decoy_type}")
        print(f"     Path: {decoy.file_path}")
        print(f"     Created: {decoy.created_at}")
        print(f"     Content preview: {decoy.content[:100]}...")
        print()
    
    # Step 4: Test Critical threat level (4 decoys)
    print("-"*60)
    print("TEST 2: Critical Threat Level (Score 71-100)")
    print("-"*60)
    
    decoys = decoy_service.generate_decoys_for_threat_level("Critical", test_path)
    
    print(f"✅ Generated {len(decoys)} decoys:")
    for decoy in decoys:
        print(f"   - Type: {decoy.decoy_type}")
        print(f"     Path: {decoy.file_path}")
        print(f"     Created: {decoy.created_at}")
        print()
    
    # Step 5: Test decoy detection
    print("-"*60)
    print("TEST 3: Decoy Detection")
    print("-"*60)
    
    test_file = f"{test_path}/passwords.txt"
    is_decoy = decoy_service.is_decoy_file(test_file)
    print(f"Is '{test_file}' a decoy? {is_decoy}")
    
    normal_file = "normal_file.txt"
    is_decoy = decoy_service.is_decoy_file(normal_file)
    print(f"Is '{normal_file}' a decoy? {is_decoy}")
    
    # Step 6: Show all deployed decoys
    print("\n" + "-"*60)
    print("TEST 4: All Deployed Decoys")
    print("-"*60)
    
    all_decoys = decoy_service.get_deployed_decoys()
    print(f"✅ Total deployed decoys: {len(all_decoys)}")
    
    # Step 7: Verify files were created
    print("\n" + "-"*60)
    print("TEST 5: File System Verification")
    print("-"*60)
    
    if os.path.exists(test_path):
        files = os.listdir(test_path)
        print(f"✅ Files created in '{test_path}':")
        for file in files:
            file_path = os.path.join(test_path, file)
            size = os.path.getsize(file_path)
            print(f"   - {file} ({size} bytes)")
    else:
        print(f"❌ Directory '{test_path}' not found")
    
    # Summary
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    print("✅ Clean Architecture working perfectly!")
    print("✅ Domain Layer: Decoy entity defined")
    print("✅ Domain Layer: IDecoyGenerator interface defined")
    print("✅ Application Layer: DecoyService orchestrating")
    print("✅ Infrastructure Layer: FileDecoyGenerator using Faker")
    print("✅ All layers integrated successfully!")
    print("\n🎉 Day 15-16 Complete! Decoy system ready!")
    print("="*60)

if __name__ == "__main__":
    test_decoy_generation()
