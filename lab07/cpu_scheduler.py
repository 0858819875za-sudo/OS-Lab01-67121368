# cpu_scheduler.py
import copy

def simulate_fcfs(processes):
    print("\n--- FCFS (First-Come, First-Served) Scheduling ---")
    current_time = 0
    total_waiting_time = 0
    
    for proc in processes:
        if current_time < proc['arrival']:
            current_time = proc['arrival']
        
        waiting_time = current_time - proc['arrival']
        total_waiting_time += waiting_time
        
        print(f"Process {proc['id']} (Burst: {proc['burst']}ms) -> Start: {current_time}ms | Waiting Time: {waiting_time}ms")
        current_time += proc['burst']
        
    avg_wait = total_waiting_time / len(processes)
    print(f">> FCFS Average Waiting Time: {avg_wait:.2f} ms")
    return avg_wait

def simulate_round_robin(processes, quantum):
    print(f"\n--- Round Robin Scheduling (Quantum: {quantum}ms) ---")
    procs = copy.deepcopy(processes)
    queue = []
    current_time = 0
    total_waiting_time = 0
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
        
        print(f"Time {current_time}ms: Running Process {curr['id']} for {exec_time}ms")
        
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
            turnaround = curr['completion'] - curr['arrival']
            waiting = turnaround - curr['burst']
            total_waiting_time += waiting

    avg_wait = total_waiting_time / n
    print(f">> Round Robin Average Waiting Time: {avg_wait:.2f} ms")
    return avg_wait

def main():
    ai_tasks = [
        {'id': 'Task_1 (Heavy Train)', 'arrival': 0, 'burst': 20},
        {'id': 'Task_2 (Quick Infer)', 'arrival': 1, 'burst': 2},
        {'id': 'Task_3 (Quick Infer)', 'arrival': 2, 'burst': 2}
    ]
    
    simulate_fcfs(ai_tasks)
    simulate_round_robin(ai_tasks, quantum=4)

if __name__ == "__main__":
    main()
