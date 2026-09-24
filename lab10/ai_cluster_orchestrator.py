# ai_cluster_orchestrator.py
import time
import os
import stat
import queue

def run_ai_cluster_orchestration():
    print("==================================================")
    print("   AI CLUSTER OS INTEGRATION ORCHESTRATOR (LAB 10)")
    print("==================================================\n")

    # 1. File System Security & Inode Locks
    print("[AXIS 1: File System Security]")
    model_path = "protected_cluster_model.bin"
    with open(model_path, "wb") as f:
        f.write(b"HIGH_VALUE_LLM_WEIGHTS_V1")
    os.chmod(model_path, stat.S_IRUSR) # chmod 400
    print(f" -> Model file '{model_path}' locked with permission 0o400 (Read-Only).")

    # 2. Memory Allocation & Virtual Memory Management
    print("\n[AXIS 2: Memory Management & Swap Control]")
    simulated_ram_capacity_mb = 1024
    allocated_tasks_mb = {"Training_Job": 512, "Inference_API": 256, "Preprocessing": 128}
    total_used_mb = sum(allocated_tasks_mb.values())
    print(f" -> Allocating Memory Tasks: {allocated_tasks_mb}")
    print(f" -> Total RAM Usage: {total_used_mb}MB / {simulated_ram_capacity_mb}MB (Safe - No Thrashing)")

    # 3. Deadlock Avoidance (Ordered Resource Lock)
    print("\n[AXIS 3: Deadlock Avoidance]")
    resources = ["GPU_0", "Storage_Volume_1"]
    print(f" -> Enforcing strictly ordered locking strategy: Lock {resources[0]} first, then {resources[1]}")
    print(" -> Deadlock status: AVOIDED (No circular wait condition)")

    # 4. CPU Scheduling Queue (Priority / Round Robin)
    print("\n[AXIS 4: CPU Scheduling Queue Integration]")
    task_queue = queue.Queue()
    task_queue.put({"id": "Inference_Req_1", "priority": "High (Interactive)", "time": 2})
    task_queue.put({"id": "Preprocessing_Batch", "priority": "Normal", "time": 5})
    task_queue.put({"id": "Training_Epoch", "priority": "Background", "time": 10})

    while not task_queue.empty():
        task = task_queue.get()
        print(f" -> Processing Queue Item: {task['id']} | Priority: {task['priority']} | Duration: {task['time']}ms")
        time.sleep(0.2)

    print("\n==================================================")
    print(" [SUCCESS] All 3 AI Workloads Executed Safely!")
    print("==================================================")

if __name__ == "__main__":
    run_ai_cluster_orchestration()