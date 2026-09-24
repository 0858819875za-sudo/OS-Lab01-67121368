# disk_scheduler.py
def simulate_fcfs_disk(requests, initial_head):
    print(f"\n--- FCFS Disk Scheduling (Start Head: {initial_head}) ---")
    current_head = initial_head
    total_head_movement = 0
    
    for req in requests:
        distance = abs(req - current_head)
        total_head_movement += distance
        print(f"Move from {current_head} to {req} (Seek Distance: {distance})")
        current_head = req
        
    print(f">> Total Head Movement (FCFS): {total_head_movement} tracks")
    return total_head_movement

def simulate_scan_disk(requests, initial_head, disk_size=200):
    print(f"\n--- SCAN (Elevator) Disk Scheduling (Start Head: {initial_head}) ---")
    total_head_movement = 0
    current_head = initial_head
    
    left = [r for r in requests if r < initial_head]
    right = [r for r in requests if r >= initial_head]
    
    left.sort(reverse=True)
    right.sort()
    
    # Moving right towards end of disk first
    sequence = right + [disk_size - 1] + left
    
    for req in sequence:
        distance = abs(req - current_head)
        total_head_movement += distance
        print(f"Move from {current_head} to {req} (Seek Distance: {distance})")
        current_head = req
        
    print(f">> Total Head Movement (SCAN): {total_head_movement} tracks")
    return total_head_movement

def main():
    io_requests = [98, 183, 37, 122, 14, 124, 65, 67]
    start_track = 53
    
    simulate_fcfs_disk(io_requests, start_track)
    simulate_scan_disk(io_requests, start_track)

if __name__ == "__main__":
    main()
