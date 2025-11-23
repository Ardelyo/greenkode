import random
import time

def find_duplicates_green(data):
    seen = set()
    duplicates = set()
    # O(n) approach
    for item in data:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

def main():
    print("Generating data...")
    # Same N=5000 to be fair
    data = [random.randint(0, 10000) for _ in range(5000)]
    
    print("Starting green algorithm...")
    start = time.time()
    # Run it 1000 times to make it measurable, or just once?
    # To compare "per task", we run once. But for measurement, we might need more time.
    # Let's run it once to show the raw speed difference.
    # We can add a sleep to simulate "system overhead" if needed, but raw is better.
    dupes = find_duplicates_green(data)
    end = time.time()
    
    print(f"Found {len(dupes)} duplicates in {end - start:.4f} seconds.")

if __name__ == "__main__":
    main()
