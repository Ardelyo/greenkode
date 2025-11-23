import random
import time

def find_duplicates_dirty(data):
    duplicates = []
    # O(n^2) approach
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] == data[j]:
                if data[i] not in duplicates:
                    duplicates.append(data[i])
    return duplicates

def main():
    print("Generating data...")
    # N=5000: 5000^2 = 25,000,000 comparisons. Should take a few seconds.
    data = [random.randint(0, 10000) for _ in range(5000)]
    
    print("Starting dirty algorithm...")
    start = time.time()
    dupes = find_duplicates_dirty(data)
    end = time.time()
    
    print(f"Found {len(dupes)} duplicates in {end - start:.4f} seconds.")

if __name__ == "__main__":
    main()
