# dataset_io_sim.py
import time
import os

def simulate_small_files_io(num_files=1000):
    start_time = time.time()
    folder = "small_images"
    os.makedirs(folder, exist_ok=True)
    
    # Writing many small files (High Metadata & Seek Overhead)
    for i in range(num_files):
        with open(f"{folder}/img_{i}.bin", "wb") as f:
            f.write(b"\x00" * 1024) # 1 KB small image
            
    # Reading them back
    for i in range(num_files):
        with open(f"{folder}/img_{i}.bin", "rb") as f:
            _ = f.read()
            
    # Cleanup
    for i in range(num_files):
        os.remove(f"{folder}/img_{i}.bin")
    os.rmdir(folder)
    
    return time.time() - start_time

def simulate_chunked_file_io(num_files=1000):
    start_time = time.time()
    archive_file = "dataset_archive.bin"
    
    # Writing one big monolithic/chunked file (Sequential I/O)
    with open(archive_file, "wb") as f:
        for _ in range(num_files):
            f.write(b"\x00" * 1024)
            
    # Reading back sequentially
    with open(archive_file, "rb") as f:
        _ = f.read()
        
    os.remove(archive_file)
    return time.time() - start_time

def main():
    print("--- Simulating Dataset Loading Speed (1,000 Samples) ---")
    
    print("\n1. Scenario A: Loading thousands of individual small files...")
    small_files_time = simulate_small_files_io()
    print(f"   -> Processing Time: {small_files_time:.4f} seconds")
    
    print("\n2. Scenario B: Loading single aggregated dataset archive...")
    chunked_time = simulate_chunked_file_io()
    print(f"   -> Processing Time: {chunked_time:.4f} seconds")
    
    speedup = small_files_time / chunked_time
    print(f"\n>>> SYSTEM IMPACT: Aggregated File I/O is {speedup:.1f} TIMES faster!")

if __name__ == "__main__":
    main()
