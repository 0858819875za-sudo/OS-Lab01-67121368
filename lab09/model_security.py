# model_security.py
import os
import stat

def create_and_lock_model(filename="model_weights.bin"):
    print(f"--- 1. Creating AI Model Weights File: {filename} ---")
    
    # Create dummy model file
    with open(filename, "wb") as f:
        f.write(b"SECRET_MODEL_WEIGHTS_DATA_V1")
    
    # Check default permissions
    initial_mode = os.stat(filename).st_mode
    print(f"Initial Permissions (Octal): {oct(initial_mode & 0o777)}")

    print("\n--- 2. Lock permissions: Owner Read-Only (0o400 / chmod 400) ---")
    # Set permission to Read-Only for Owner only (0o400)
    os.chmod(filename, stat.S_IRUSR)
    
    locked_mode = os.stat(filename).st_mode
    print(f"Locked Permissions (Octal): {oct(locked_mode & 0o777)}")

    print("\n--- 3. Testing System Behavior ---")
    # Test Read Access
    try:
        with open(filename, "rb") as f:
            data = f.read()
            print(f"[SUCCESS] Read Model Data: {data.decode()}")
    except Exception as e:
        print(f"[FAIL] Read Error: {e}")

    # Test Write/Modify Access (Should fail)
    try:
        with open(filename, "ab") as f:
            f.write(b"\nTAMPERED_DATA")
            print("[UNEXPECTED] Successfully modified model file!")
    except PermissionError as e:
        print(f"[PROTECTED] OS Blocked Write Attempt: {e}")

if __name__ == "__main__":
    create_and_lock_model()
