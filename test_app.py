from greenkode import green_audit, CodeInspector
import time
import os

# 1. Test the Decorator
@green_audit
def bad_function():
    print("Doing heavy work...")
    # Simulate work
    x = [i**2 for i in range(1000000)]
    time.sleep(0.5)

# 2. Test the Static Analyzer
def test_analyzer():
    print("\n--- Testing Static Analyzer ---")
    # Create a dummy file with inefficient code
    dummy_code = """
import pandas as pd
def inefficient():
    for i in range(10):
        for j in range(10):
            print(i, j)
"""
    with open("dummy_inefficient.py", "w") as f:
        f.write(dummy_code)
    
    inspector = CodeInspector("dummy_inefficient.py")
    suggestions = inspector.analyze()
    
    for tip in suggestions:
        print(f"[Analyzer] {tip}")
    
    # Clean up
    if os.path.exists("dummy_inefficient.py"):
        os.remove("dummy_inefficient.py")

if __name__ == "__main__":
    print("--- Testing GreenKode Engine ---")
    bad_function()
    test_analyzer()
