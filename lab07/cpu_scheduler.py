import copy

def simulate_fcfs(processes):
    print("--- Running FCFS Scheduler ---")
    current_time = 0
    total_waiting_time = 0
    total_turnaround_time = 0
    
    for proc in processes:
        if current_time < proc['arrival']:
            current_time = proc['arrival']
        
        waiting_time = current_time - proc['arrival']
        total_waiting_time += waiting_time
        
        print(f"[Time {current_time:02d}] Process {proc['id']} starts. (Wait time: {waiting_time})")
        current_time += proc['burst']
        
        turnaround_time = current_time - proc['arrival']
        total_turnaround_time += turnaround_time
        print(f"[Time {current_time:02d}] Process {proc['id']} finishes. (Turnaround time: {turnaround_time})")
        
    avg_wait = total_waiting_time / len(processes)
    avg_turnaround = total_turnaround_time / len(processes)
    print(f">> FCFS Average Waiting Time: {avg_wait:.2f}")
    print(f">> FCFS Average Turnaround Time: {avg_turnaround:.2f}")
    return avg_wait

def simulate_round_robin(processes, quantum):
    print(f"\n--- Running Round Robin Scheduler (Quantum = {quantum}) ---")
    procs = copy.deepcopy(processes)
    queue = []
    current_time = 0
    total_waiting_time = 0
    total_turnaround_time = 0
    completed = 0
    n = len(procs)
    
    for p in procs:
        p['remaining'] = p['burst']
        p['completion'] = 0

    queue.append(procs[0])
    visited = [False] * n
    visited[0] = True

    while completed < n:
        if not queue:
            for i in range(n):
                if procs[i]['remaining'] > 0:
                    queue.append(procs[i])
                    visited[i] = True
                    if current_time < procs[i]['arrival']:
                        current_time = procs[i]['arrival']
                    break

        curr = queue.pop(0)
        exec_time = min(quantum, curr['remaining'])
        
        print(f"[Time {current_time:02d}] Process {curr['id']} runs for {exec_time} units.")
        
        current_time += exec_time
        curr['remaining'] -= exec_time

        for i in range(n):
            if not visited[i] and procs[i]['arrival'] <= current_time and procs[i]['remaining'] > 0:
                queue.append(procs[i])
                visited[i] = True

        if curr['remaining'] > 0:
            queue.append(curr)
        else:
            completed += 1
            curr['completion'] = current_time
            print(f"[Time {current_time:02d}] Process {curr['id']} finishes.")
            turnaround = curr['completion'] - curr['arrival']
            waiting = turnaround - curr['burst']
            total_waiting_time += waiting
            total_turnaround_time += turnaround

    avg_wait = total_waiting_time / n
    avg_turnaround = total_turnaround_time / n
    print(f">> Round Robin Average Waiting Time: {avg_wait:.2f}")
    print(f">> Round Robin Average Turnaround Time: {avg_turnaround:.2f}")
    return avg_wait

def main():
    # กำหนดค่าตามรายงานเพื่อน: P1 = 10, P2 = 2, P3 = 3, ทุกตัว arrival = 0
    tasks = [
        {'id': 'P1', 'arrival': 0, 'burst': 10},
        {'id': 'P2', 'arrival': 0, 'burst': 2},
        {'id': 'P3', 'arrival': 0, 'burst': 3}
    ]
    
    simulate_fcfs(tasks)
    simulate_round_robin(tasks, quantum=3)

if __name__ == "__main__":
    main()