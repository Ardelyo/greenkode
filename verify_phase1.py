from src.greenkode.analyzer import CodeInspector
import os

# Create a dummy file for testing if it doesn't exist (though we have tests/test_analyzer_phase1.py)
test_file = "tests/test_analyzer_phase1.py"

if not os.path.exists(test_file):
    print(f"Error: {test_file} not found")
else:
    inspector = CodeInspector(test_file)
    suggestions = inspector.analyze()
    
    print("--- Analysis Results ---")
    for s in suggestions:
        print(s)
    print("------------------------")
